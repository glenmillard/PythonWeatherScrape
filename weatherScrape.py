
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:10:14 2019

@author: Glen Millard
"""
#This is my attempt at scaping a web page for data using the Xpath fields on the page itself
# I wonder if there is an API or plugin for this instead.
# I chose Manchester NH becuase I live here.

#import requests,selenium, os, datetime
from selenium import webdriver

def main():

#create web connector for data
#res = requests.get('https://forecast.weather.gov/MapClick.php?lat=42.93452000000008&lon=-71.43705999999997')

# I included the logging module to see how long it took to execute.
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.debug('Start of program')

#first_now = datetime.datetime.now()

#print (first_now.isoformat())


    os.environ['MOZ_HEADLESS'] = '1' # keep Firefox headless - run in background
    driver = webdriver.Firefox()

#create web connector
    driver.get('https://forecast.weather.gov/MapClick.php?lat=42.93452000000008&lon=-71.43705999999997')

#these will scrape the NWS page for the data I need - xpath copied from the page sources
    location = driver.find_element_by_xpath('//*[@id="current-conditions"]/div[1]/div/h2')
    temp = driver.find_element_by_xpath('//*[@id="current_conditions-summary"]/p[2]')
    last_update = driver.find_element_by_xpath('//*[@id="current_conditions_detail"]/table/tbody/tr[6]/td[2]')
    table = driver.find_element_by_xpath('//*[@id="current_conditions_detail"]/table')
    forecast = driver.find_element_by_xpath('//*[@id="detailed-forecast-body"]/div[1]/div[2]')
    weekly = driver.find_element_by_xpath('//*[@id="detailed-forecast"]')

#these will extract the text from the page - various points
    print(temp.text)
    print(location.text)
    print(last_update.text)
    print(table.text)
    print(forecast.text)
    print(weekly.text)

# close things out correctly - don't leave any messes
# seems we need the last two or the Firefox executable stays running in the background.
    driver.close()
    driver.quit()
    driver.stop_client()
#second_now = datetime.datetime.now()
#print (second_now.isoformat())

#logging.debug('End of program')
#//*[@id="current_conditions_detail"]/table

if __name__ == "__main__":
    main()
