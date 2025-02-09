import requests
from urls import Urls

class ApiMethods:
    @staticmethod
    def create_courier(payload):
        return requests.post(Urls.CREATE_COURIER_API, data=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(Urls.LOGIN_COURIER_API, data=payload)

    @staticmethod
    def create_order(payload):
        return requests.post(Urls.CREATE_ORDER_API, data=payload)

    @staticmethod
    def cancel_order(payload):
        return requests.put(Urls.CANCEL_ORDER_API, data=payload)

    @staticmethod
    def order_accepted(order_id, courier_id):
        return requests.put(f'{Urls.ORDER_ACCEPTED}{order_id}', params={'courierId': courier_id})

    @staticmethod
    def get_courier_order_list(courier_id):
        return requests.get(Urls.LIST_ORDER_API, {'courierId': courier_id})

    @staticmethod
    def get_order_by_track(track):
        return requests.get(Urls.GET_ORDER_BY_TRACK, {'t': track})
