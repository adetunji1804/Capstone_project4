

# create an instance of a database, establish connection and enforce foreignkey constraints
#db = SqliteDatabase('visitor_db.sqlite', pragmas={'foreign_keys': 1})

class Visitor:
    #visitor class attributes
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name   

    def get_email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    def __str__(self):
        return f'Fullname: {self.first_name} {self.last_name}, email: {self.get_email()} '



class Visit_record:
    #visitor_record class attributes
    def __init__(self, info_request, date_request, currency, visitor_id):
        self.info_request = info_request
        self.date_request = date_request
        self.visitor_id = visitor_id
        self.currency = currency
    
   
    def __str__(self):
        return f'Requested Info: {self.info_request} \nDate: {self.date_request}\n'


    
class Weather_info:
    #API weather information attribute to bookmark
    def __init__(self, forecast_date, temp, weather_id):
        self.forecast_date = forecast_date
        self.temp = temp
        self.weather_id = weather_id 



class Country_request:
    #visitor choice of counry and city attribute to bookmark
    def __init__(self, country, code_ext, city):
        self.country = country
        self.code_ext = code_ext
        self.city = city
    

    def get_country_code_info(self):
        return '{} {},{}'.format(self.city, self.country, self.code_ext)

    def __str__(self):
        pass