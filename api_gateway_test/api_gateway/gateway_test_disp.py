from functools import singledispatchmethod

import requests
from requests import api

class DictToObj:
    def __init__(self, dict_data):
        for key, value in dict_data.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObj(value))  # recursiv
            else:
                setattr(self, key, value)

class UserApiGateway(object):
    API_VERSION = "V1"
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @singledispatchmethod
    def get_endpoints(self, arg=None):
        endpoints = {}
        if arg is None:
            endpoints = {
                'auth': {
                    'login': f'/{self.API_VERSION}/auth/login',
                    'logout': f'/{self.API_VERSION}/auth/logout',
                },
                'users': {
                    'list': f'{self.get_base_url()}/users',
                }
            }
        return endpoints

    @get_endpoints.register
    def _(self, user_id: int):
        result = self.get_endpoints(None)
        if bool(user_id) and result.get('users', False):
            result['users']['user'] = f'{self.get_base_url()}/users/{user_id}'
        return DictToObj(result)

    @get_endpoints.register
    def _(self, arg: str):
        print("NO implementation")


    def __init__(self, environment=False):
        self.env = environment

    def get_user(self, user_id=False):
        res = self.get_endpoints("user_id")
        endpoints = self.get_endpoints(user_id)
        print("Endpoints: ", endpoints.users.__dict__)
        try:
            if user_id:
                response = api.get(endpoints.users.user)
            else:
                response = api.get(endpoints.users.list)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            raise err

    def get_base_url(self):
        return self.BASE_URL

class DisplayUser:
    def __init__(self, gateway: UserApiGateway):
        self.gateway = gateway

    def get_user_info(self, user_id):
        user_info = self.gateway.get_user(user_id)
        return user_info

    def get_users(self):
        user_info = self.gateway.get_user()
        return user_info


# Example usage
# instance = DisplayUser(UserApiGateway())
# print(instance.get_user_info(2))
# print(instance.get_users())
if __name__ == '__main__':
    DisplayUser(UserApiGateway()).get_users()
    DisplayUser(UserApiGateway()).get_user_info(2)