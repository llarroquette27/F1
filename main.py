import requests

def main():
    response = requests.get("https://api.openf1.org/v1/drivers")
    print(response.json())


if __name__ == "__main__":
    main()