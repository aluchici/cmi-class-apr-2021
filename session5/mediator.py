# 
# Mediator - interactionam cu API (get, put), incarcam datele sub forma de DataFrame, mean, plot

# clasa Mediator
# proprietatile
# - url -> unde fac acele call-uri
# - data -> dataframe 
# - field_city_id = 'city_id'
# - field_city = 'city'
# - field_population = 'population'
# actiuni
# - get_data
# - update_data
import pandas 
import requests 

class Mediator:

    def __init__(self, url):
        self.base_url = url
        self.get_all_url = self.base_url + 'get-all'
        self.put_url = self.base_url + 'city-info/'

        self.field_city_id = 'city_id'
        self.field_city = 'city'
        self.field_population = 'population'
        
        self.data = None
        
    def get_data(self):
        response = requests.get(self.get_all_url).json()
        self.data = pandas.DataFrame(response)

    def update_data(self, city_id, city, population):
        data = {
            "city": city,
            "population": population
        }
        update_url = self.put_url + str(city_id)
        print(update_url)
        response = requests.put(update_url, data)


url = 'https://turbo-octo-fortnight-1.herokuapp.com/'
med = Mediator(url)
med.get_data()

med.update_data(1, 'test oras', 1223)
med.get_data()

print(med.data.mean())
print(med.data[med.field_population].mean())
