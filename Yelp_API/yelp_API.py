import requests
import json
import pprint


def Yelp_API(term_choice):
    # Define the API Key and define the Endpoint and define the Header
    api_key =''
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization' : 'Bearer %s' %  api_key}

    # Define the parameters
    PARAMETERS = {'term':'food',
                'limit': 5,
                'radius' : 1000,
                'location': '%s' % term_choice}

    # Make a 
    reponse = requests.get(url = ENDPOINT, params= PARAMETERS, headers = HEADERS)


    # Convert the JSON string to a Dictionary
    business_data = reponse.json()

    # Returns the name rating and the zip code for the 5 closest resturants

    biz_data = []
    print(f'Here are some resturants near {term_choice}')
    for biz in business_data['businesses']:
        biz_datas = (biz['name'], biz ['rating'], biz['location']['country'])
        biz_data.append(biz_datas)
        print('Resturant : ',biz['name'] ,'\nRating : ',biz ['rating'],'\n')
    print(biz_data)
    return biz_data