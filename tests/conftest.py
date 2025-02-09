import pytest
import random
import string
import requests

from api_methods import ApiMethods
from urls import Urls

@pytest.fixture
def create_login_delete_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    login_pass = []
    create_response = ApiMethods.create_courier(payload)
    if create_response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    login_payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    login_response = ApiMethods.login_courier(login_payload)
    courier_id = login_response.json()['id']

    yield create_response, login_response, login_pass, courier_id

    requests.delete(Urls.DELETE_COURIER_API + str(courier_id))