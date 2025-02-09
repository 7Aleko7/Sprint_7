import pytest

from api_methods import ApiMethods
from data import CourierData

class TestLoginCourier:
    def test_successful_login_courier(self, create_login_delete_courier):
        assert create_login_delete_courier[1].status_code == 200 and 'id' in create_login_delete_courier[1].json()

    payloads = ({
                    "login": '',
                    "password": CourierData.password
                },
                {
                    "login": CourierData.login,
                    "password": ''
                }
    )
    @pytest.mark.parametrize('payload', payloads)
    def test_login_courier_without_required_parameter(self, create_login_delete_courier, payload):
        response =  ApiMethods.login_courier(payload)

        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'


    def test_login_courier_with_incorrect_login(self, create_login_delete_courier):
        payload = {
                    "login": CourierData.login,
                    "password": create_login_delete_courier[2][1]
                  }
        response = ApiMethods.login_courier(payload)

        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    def test_login_courier_with_incorrect_password(self, create_login_delete_courier):
        payload = {
                    "login": create_login_delete_courier[2][0],
                    "password": CourierData.password
                  }
        response = ApiMethods.login_courier(payload)

        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'
