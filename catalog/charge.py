import requests

# send the request with the data
API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
API_KEY = 'YOUR_API_KEY_GOES_HERE'
r = requests.post(API_URL, data={
  'apiKey': API_KEY,
  'currency': 'usd',
  'amount': '5.99',
  'type': 'Visa',
  'number': '4732817300654',
  'exp_month': 10,
  'exp_year': 14,
  'cvc': 411,
  'name': 'Cosmo Limesandal',
  'descripMon': 'Charge for cosmo@is411.byu.edu',
})

# just for debugging, print the response text
print(r.text)

# parse the response to a dictionary
resp = r.json()
print(resp['ID'])