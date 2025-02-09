import pytest

from api_methods import ApiMethods
from data import CourierData

class TestCreateCourier:
    def test_successful_create_courier(self, create_login_delete_courier):
        assert create_login_delete_courier[0].status_code == 201 and create_login_delete_courier[0].json() == {'ok': True}

    payloads=({
        "login": '',
        "password": CourierData.password,
        "firstName": CourierData.first_name
    },
    {
        "login": CourierData.login,
        "password": '',
        "firstName": CourierData.first_name
    }
    )
    @pytest.mark.parametrize('payload', payloads)
    def test_create_courier_without_required_parameter(self, payload):
        response = ApiMethods.create_courier(payload)

        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    def test_create_two_identical_courier(self,create_login_delete_courier):
        payload = {
        "login":  create_login_delete_courier[2][0],
        "password": CourierData.password,
        "firstName": CourierData.first_name
        }
        response = ApiMethods.create_courier(payload)

        assert response.status_code == 409 and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'