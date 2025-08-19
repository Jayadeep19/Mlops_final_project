import requests

# conditions = {'AT':[20],
#         'V':[50],
#         'AP': [1015],
#         'RH': [75]}

conditions = {'% Iron Concentrate': [67],
         'Amina Flow': [560],
         'Ore Pulp pH':[11],
         'Average Air Flow': [265]
         }

url = "http://localhost:9696/predict"
response = requests.post(url, json=conditions)
print(response.json())
