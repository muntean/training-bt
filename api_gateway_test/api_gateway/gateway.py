from functools import singledispatch
from multipledispatch import dispatch

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

    @dispatch()
    def get_endpoints(self):
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

    @dispatch(int)
    def get_endpoints(self, user_id):
        result = self.get_endpoints()
        if result.get('users', False):
            result['users']['user'] = f'{self.get_base_url()}/users/{user_id}'
        return DictToObj(result)


    def __init__(self, environment=False):
        self.env = environment

    def get_user(self, user_id=False):
        endpoints = self.get_endpoints(user_id)
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
