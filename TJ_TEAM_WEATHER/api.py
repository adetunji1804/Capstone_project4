import requests
import os
from datetime import datetime
from visitor_class import *

""" 
    this module consume API to fetch country, corresponding extension code
    and the weather forecast for the user choice of city in specified country
"""


def get_country_and_code():
    # API url for list of countries and code's
    url = "https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json"
    response = requests.get(url)  # fetched data stored in JSON format
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        return "connection not established!"


def verify_country_and_city(country, code, city):
    try:
        country_code_list = get_country_and_code()
        country = input("Enter country: ")
        city = input("Enter city of choice: ")

        # iterate list from the API
        for i in range(len(country_code_list)):
            value = country_code_list[i]["Name"]

            # compare user input with country and code list from API
            if value.lower() == country.lower():  # value in lowercase and compare
                code = country_code_list[i]["Code"]  # country code found
                name = country_code_list[i]["Name"]  # country name found
                break
    except:
        return 'Error! country not found'
    # return an object of Country_request class
    obj_country = Country_request(name, code, city)
    return obj_country
    

def weather_details():
    try:
        # empty list variables to store date and temperature forecast from API
        rec_date = []
        rec_temp = []
        result = verify_country_and_city("country", "code", "city")
        user_city = result.city + ", " + result.code_ext
        query = {
            "q": user_city,
            "units": "imperial",
            "appid": "141312562055da1f2e747a4441ac1e17",
        }  # url query created
        url = "http://api.openweathermap.org/data/2.5/forecast"

        data = requests.get(url, params=query)
        if data.status_code == 200:
            data = data.json()  # API data stored in JSON format
            forecast_items = data["list"]
            for forecast in forecast_items:
                timestamp = forecast["dt"]
                date = datetime.fromtimestamp(timestamp)  # Unix timestamp
                temp = forecast["main"]["temp"]
                # append data to list
                rec_date.append(date)
                rec_temp.append(temp)
            return rec_date, rec_temp
        else:
            return None, None
    except:
        print("Either the country or city is wrongly spelt\n")
