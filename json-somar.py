import requests
import json


response = requests.get('https://nimbus.somar.io/forecast/7days?city=SaoPaulo-SP&reference=Somar',headers={'x-api-key':'*******'}).json()
print(json.dumps(response))
