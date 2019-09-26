import requests

def main():
    response = requests.get("https://www.google.com")
    print('Status Code:', response.status_code)

if __name__ == "__main__":
    main()
