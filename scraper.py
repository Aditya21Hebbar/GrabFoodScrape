import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headers')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver 
  
url = 'https://food.grab.com/sg/en/restaurants'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def get_locs(driver):
  driver.get(url)
  while True:
    try:
      loadMoreButton = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[5]/div[4]/div/div/div[4]/div/button")
      time.sleep(2)
      loadMoreButton.click()
      time.sleep(5)
    except Exception as e:
      print (e)
      break
      print ("Complete")
      time.sleep(10)
      driver.quit()

if __name__ == "__main__":
  # print("creating driver")
  driver = get_driver()
  # print('fetching the top list restaurants')
  driver.get(url)
  # while True:
  #   try:
  #     print("hello")
  #     loadMoreButton = driver.find_element(By.CSS_SELECTOR,'#page-content > div:nth-child(4) > div > div > div:nth-child(5) > div > button')
  #     time.sleep(2)
  #     loadMoreButton.click()
  #     time.sleep(5)
  #   except Exception as e:
  #     print (e)
  #     break
  #     print ("Complete")
  #     time.sleep(10)
  #     driver.quit()
  r= driver.page_source
  soup = BeautifulSoup(r,'html.parser')
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
  print(position_data)
 