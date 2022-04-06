# This program converts USD to CAD with realtime data
import requests
import json

amountusd = float(input('How much USD?: '))
request = requests.get('https://openexchangerates.org/api/latest.json?app_id=3c110069a18f4bdfbb56773165b57fed')
data = request.text
parse_json = json.loads(data)
currentcad = parse_json['rates']['CAD']
amountcad = amountusd * currentcad
print(f'{amountusd} is equal to {amountcad}')
