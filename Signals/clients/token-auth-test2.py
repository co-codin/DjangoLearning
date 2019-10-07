import requests

def client():
    # data = {
    #     "username": "resttest",
    #     "email": "test@rest.com",
    #     "password1": "changeme123",
    #     "password2": "changeme123"
    #     }
    #
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                          data=data)

    token_h = "Token 5062b9efa7ad8f6f71cf9bd0f8f0c9d6da3b4526"
    headers = {"Authorization": token_h}
    response = requests.get('http://127.0.0.1:8000/api/profiles', headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()