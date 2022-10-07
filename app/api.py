import requests
import json

class Api:
    def list_user(self):
        BASE_URL = 'https://jsonplaceholder.typicode.com'
        res = requests.get(BASE_URL+'/users')
        return res
    

if __name__ == "__main__":
    api = Api()
    print(api.list_user().json())
