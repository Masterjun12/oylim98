import requests import json

url = "https://yts.mx/api/v2/list_movies.json" 
response = requests.get(url) 
html = json.loads(response.text) 
data = html['data'] 
movies = data['movies'] 

for m in range(10): 
    print(movies[m]['title'],movies[m]['rating'],movies[m]['year'])

import requests import json

url = "https://yts.mx/api/v2/list_movies.json" 
response = requests.get(url) 
html = json.loads(response.text) 
data = html['data'] 
movies = data['movies'] 
for m in range(10): 
    print(movies[m]['title'],movies[m]['rating'],movies[m]['year'])