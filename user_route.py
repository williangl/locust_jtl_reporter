from logging import info

from faker import Faker
from locust import events, task, TaskSet

from jtl_listener import JtlListener

faker = Faker("pt_br")

default_header = {"monitor": "false"}


class UserLoadTest(TaskSet):

    @task()
    def test_list_users(self):
        response = self.client.get(
            "/usuarios",
            name="Listar usuários",
            headers=default_header,
        )

        info(f"LISTAR USUARIOS - Response Status Code: {response.status_code}")
        info(f"LISTAR USUARIOS - Response Content: {response.content}")

    @task()
    def test_create_user(self):
        response = self.client.post(
            "/usuarios",
            name="Criar usuário",
            json={
                "nome": faker.name(),
                "email": faker.email(),
                "password": "teste",
                "administrador": "false"
            },
            headers=default_header
        )

        info(f"CRIAR USUARIO - Response Status Code: {response.status_code}")
        info(f"CRIAR USUARIO - Response Content: {response.content}")


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    JtlListener(env=environment,  project_name="locust_jtl_reporter_test",
                scenario_name="user_route",
                environment="will_environment_test",
                backend_url="http://localhost")
