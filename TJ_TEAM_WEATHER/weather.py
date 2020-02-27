#reference to relevant module
import requests
import os
from datetime import datetime



''' 
function to get country extension code. 
consume API with list of countries and corresponding codes
'''
def get_connection_status():
    #list of countries and code's API url
    url ='https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json'
    data = requests.get(url) # fetched data stored in JSON format
    if data.status_code == 200:
        data = data.json()
        return data
    elif data.status_code == 404:
        return 'connection not established!'
        

def get_country_and_city(country, city):
    #iterate through list to check if user input(country) is on list
    data = get_connection_status()
    country = input('Enter country: ')
    city = input('Enter city of choice: ')

    for i in range(len(data)): 
        value = data[i]['Name']
        if value.lower() == country.lower():
            #return data[i]['Code'] #return country code
            code = data[i]['Code']
            return city +','+ code


check = True     
while check:
    city_country_extension = get_country_and_city('','')
    query = {'q': city_country_extension, 'units': 'imperial', 'appid':'141312562055da1f2e747a4441ac1e17'} #url query created
    url = 'http://api.openweathermap.org/data/2.5/forecast'
   
    data = requests.get(url, params=query) #API data stored in JSON format
    if data.status_code == 200:
        data = data.json()

        forecast_items = data['list']
        print(f'\nTHE WEATHER FORECAST FOR {city_country_extension}\n_______________________________________ ')
        for forecast in forecast_items: #iterate through received data
            timestamp = forecast['dt']
            date = datetime.fromtimestamp(timestamp) # Unix timestamp
            dateFormated = date.strftime("%b %d %Y %H:%M") #strftime for date formatting-CR
            temp = forecast['main']['temp']
            #display date and temprature of specified city
           
            print(f'| At {dateFormated} - Temp is {temp:.1f}°F | \n----------------------------------------') 
            check = False #terminate process
    else:
        print(f'{city_country_extension} Not found! \n Either the country or city is wrongly spelt')
    print('\n')