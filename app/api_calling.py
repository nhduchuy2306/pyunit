import api

def call_api():
    resp = api.Api.list_user()
    return resp.json()

if __name__ == '__main__':
    a = call_api()
    print(a)