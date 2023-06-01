import requests
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
data = response.json()
cats_description = [cat['description'] for cat in data]
print(cats_description)

weights = [sum(list(map(lambda n: int(n), cat['weight']['metric'].split(' - '))))/2 for cat in data]
print(weights)

years = [sum(list(map(lambda n: int(n), cat['life_span'].split(' - '))))/2 for cat in data]
print(years)