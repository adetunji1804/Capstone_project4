import requests
# A python module for currencies. See https://pypi.org/project/ccy/
import ccy

import geonamescache

def Currency_API(country):
    # No API Key required.
    # Retrives the country code from the yelp data
    country = country[0][2]
    # Using the ccy module to conver the country code to a currency code.
    country_currency = ccy.countryccy(country)
    # Make a request
    reponse = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
    business_data = reponse.json()
    country_exchange_rate = (business_data['rates'][country_currency])
    return(f' {country_exchange_rate} {country_currency}'.format(country_exchange_rate, country_currency))


