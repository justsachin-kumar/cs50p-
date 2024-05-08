# import all the libraries
import requests
import sys
import json

# try for prompt in command line
try:
    # take 2 arguments from the user
    if len(sys.argv) != 2:
        sys.exit("missing command-line argument")

    # check for the second argument to be a  float else raise exception
    number = float(sys.argv[1])

except ValueError:
    sys.exit("command-line argument isn't a number")

# getting bitcoin price form API

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

x = response.json()
# getting only bitcoin usd price and storing it into a variable
rate = float(x["bpi"]["USD"]["rate_float"])
# multiplying the second command argument with the price cariable

amount = rate * number

# giving the user output in USD format with proper seperator
print(f"${amount:,.4f}")
