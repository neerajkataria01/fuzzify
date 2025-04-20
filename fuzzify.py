import requests
import os

print("\033[93mWarning: Do not put / in the end\033[0m")
api = input("Enter the API > ")
wordlist = input("Enter the Wordlist > ")


if not os.path.isfile(wordlist):
    print("\033[91mError: Wordlist file not found!\033[0m")
    exit(1)



def function():
    with open(wordlist, "r") as file:
        words = [i.strip() for i in file.readlines()]
        print("Getting Response.......\n")
        for word in words:
            endpoint = f"{api}/{word}"
            print(f"Testing endpoint: \033[93m{endpoint}\033[0m")
            try:
                response = requests.get(url=endpoint, timeout=10)
                if response.status_code == 404:
                    print(f"Response Code => \033[91m'{response.status_code}'\033[0m")
                    continue
                else:
                    try:
                        data = response.json()
                        print("\033[92m" + f"Response Code => \033[91m'{response.status_code}'\033[0m")
                        print(data)
                    except ValueError:
                        print(f"\033[93mWarning: Response is not in JSON format!\033[0m")
                        print(response.text)
            except requests.exceptions.Timeout:
                print(f"\033[91mError: The request to {endpoint} timed out after 10 seconds.\033[0m")
            except requests.exceptions.RequestException as e:
                print(f"\033[91mError: Request failed for {endpoint}. Details: {e}\033[0m")
                print(f"Error Details: {e}")
function()