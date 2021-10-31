from json import dumps
from logging import info

from locust import events, task, TaskSet

from jtl_listener import JtlListener


default_header = {"monitor": "false"}


class ProductLoadTest(TaskSet):

    def _get_user(self):
        response = self.client.get(
            "/usuarios",
            name="Get User",
            params={"email": "xpto_qa@pagar.me"},
            headers=default_header
        )
        info(f"CREATE USER - Response Status Code: {response.status_code}")
        info(f"CREATE USER - Response Content: {response.content}")
        return response

    def _do_login(self):
        self.id = self._get_user().json().get("_id")
        response = self.client.post(
            "/login",
            name="Do Login",
            json={
                "email": "xpto_qa@pagar.me",
                "password": "teste",
            },
            headers=default_header
        )
        info(f"DO LOGIN - Response Status Code: {response.status_code}")
        info(f"DO LOGIN - Response Content: {response.content}")
        return response

    def on_start(self):
        auth_token = self._do_login().json().get("authorization")
        default_header.update({"authorization": auth_token})

    @task()
    def test_creat_product(self):
        response = self.client.post(
            "/usuarios",
            name="Create Product",
            headers=default_header,
            json={
                    "nome": "Logitech MX Vertical",
                    "preco": 470,
                    "descricao": "Mouse",
                    "quantidade": 381
                }
            )

        info(f"LISTAR USUARIOS - Response Status Code: {response.status_code}")
        info(f"LISTAR USUARIOS - Response Content: {response.content}")


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    JtlListener(env=environment,  project_name="locust_jtl_reporter_test",
                scenario_name="product_route",
                environment="will_environment_test",
                backend_url="http://localhost")
