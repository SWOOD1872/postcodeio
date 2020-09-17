# Sam Wood
# 17/09/2020
# Makes HTTP calls to the postcodes.io API

import requests
import json
import os
import sys
from tabulate import tabulate

# Retrive and validate the postcode
try:
  if len(sys.argv)-1 == 1:
    postcode = sys.argv[1]
  if len(sys.argv)-1 == 2:
    postcode = f"{sys.argv[1]} {sys.argv[2]}"
  if len(sys.argv)-1 < 1 or len(sys.argv)-1 > 2:
    raise IndexError
except IndexError as e:
  print("ERROR: You must supply a valid postcode")
  exit(1)

# Default endpoint
default_endpoint = "https://api.postcodes.io/"

# Postcode lookup
postcode_lookup = os.path.join(default_endpoint, f"postcodes/{postcode}")

# Parse JSON response to a dict
results = requests.get(postcode_lookup).json()
if results["status"] != 200:
  print(f"ERROR: Bad HTTP status ({results['status']})")
  exit(1)

# Extract out latitude and longitude
latitude = results["result"]["latitude"]
longitude = results["result"]["longitude"]

# Tabulate and print data
data = [[postcode, latitude, longitude]]
print(tabulate(data, headers=["Postcode", "Latitide", "Longitude"]))

exit(0)