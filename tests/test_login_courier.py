import pytest
import allure
from api_methods import ApiMethods
from data import CourierData

class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    @allure.description('Авторизация курьера, с валидными данными, во всех параметрах')
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

    @allure.title('Авторизация курьера без одного из обязательных параметров')
    @allure.description('При попытке авторизации, без одного из обязательных параметров, возвращается 400 ошибка и в теле ответа указано: Недостаточно данных для входа')
    @pytest.mark.parametrize('payload', payloads)
    def test_login_courier_without_required_parameter(self, create_login_delete_courier, payload):
        response =  ApiMethods.login_courier(payload)

        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Авторизация с некорректным логином')
    @allure.description('При попытке авторизации с некорректным логином возвращается 404 ошибка и в еле ответа указано: Учетная запись не найдена')
    def test_login_courier_with_incorrect_login(self, create_login_delete_courier):
        payload = {
                    "login": CourierData.login,
                    "password": create_login_delete_courier[2][1]
                  }
        response = ApiMethods.login_courier(payload)

        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Авторизация с корректным логином и некорректным паролем')
    @allure.description('При попытке авторизации с корректным логином, но некорректным логином возвращается 404 ошибка и в еле ответа указано: Учетная запись не найдена')
    def test_login_courier_with_incorrect_password(self, create_login_delete_courier):
        payload = {
                    "login": create_login_delete_courier[2][0],
                    "password": CourierData.password
                  }
        response = ApiMethods.login_courier(payload)

        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'
