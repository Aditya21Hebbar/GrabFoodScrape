import requests
import json
from bs4 import BeautifulSoup

url = 'https://food.grab.com/sg/en/restaurants'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

r = requests.get(url,headers = headers)
soup = BeautifulSoup(r.content,'html.parser')
script = soup.find_all('script')[0]


data = json.loads(soup.find('script', id='__NEXT_DATA__').text)
print(data)