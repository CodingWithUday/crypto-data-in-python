import requests

coinname = str(input("Which Crypto Coin Do You Want To Retrive Data Of: "))

response = requests.get("https://api.coincap.io/v2/assets/"+coinname.lower())


if response.status_code != 200:
    print("Error: Unable To Retrive Data For Your Crypto!")



else:
    print("Coin Name -", response.json() ['data'] ['name'])
    print("Price (USD) -", response.json() ['data'] ['priceUsd'])
    print("Market Cap (USD) -", response.json() ['data'] ['marketCapUsd'])
    print("Volume (USD) 24 hr -", response.json() ['data'] ['volumeUsd24Hr'])