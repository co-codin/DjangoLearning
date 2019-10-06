import requests

def client():
    token_h = "Token 5062b9efa7ad8f6f71cf9bd0f8f0c9d6da3b4526"
    headers = {"Authorization": token_h}
    # credentials = {"username": "elijah", "password": "hellojava"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
    response = requests.get('http://127.0.0.1:8000/api/profiles', headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()