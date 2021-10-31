from locust import HttpUser

from product_route import ProductLoadTest
from user_route import UserLoadTest


class WebsiteUser(HttpUser):

    tasks = [
        UserLoadTest,
        ProductLoadTest
    ]
