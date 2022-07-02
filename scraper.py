import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://food.grab.com/sg/en/restaurants'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def 
r = requests.get(url,headers = headers)
soup = BeautifulSoup(r.content,'html.parser')

data = json.loads(soup.find('script', id='__NEXT_DATA__').text)

restaurant_list = data['props']['initialReduxState']['pageRestaurantsV2']['entities']['restaurantList']

position_data=[]
for restaurant in restaurant_list:
    restaurant_data = restaurant_list[restaurant]
    latitude  = restaurant_data['latitude']
    longitude = restaurant_data['longitude']
    geo_data = {
        'latitude': latitude,
        'longitude': longitude
    }
    position_data.append(geo_data)
position_data

result = pd.DataFrame(position_data)
result