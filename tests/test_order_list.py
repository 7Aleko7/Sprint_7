import pytest
import json
from api_methods import ApiMethods
from data import CourierData

class TestOrderList:
    def test_get_courier_order_list(self, create_login_delete_courier):
        order_payload= {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
        "GREY", "BLACK"]}
        courier_id=create_login_delete_courier[3]

        create_order_response=ApiMethods.create_order(json.dumps(order_payload))
        order_track=create_order_response.json()['track']
        track_payload = {"track": (create_order_response.json()['track'])}

        get_order_response = ApiMethods.get_order_by_track(order_track)
        order_id = get_order_response.json()['order']['id']

        ApiMethods.order_accepted(order_id, courier_id)

        get_order_list_response = ApiMethods.get_courier_order_list(courier_id)

        assert get_order_list_response.status_code == 200 and  get_order_list_response.json()['orders'][0]['id'] == order_id

        ApiMethods.cancel_order(track_payload)