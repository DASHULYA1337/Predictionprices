import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from googletrans import Translator

pd.options.display.max_columns = None
desired_width = 320
pd.set_option('display.width', desired_width)

data = pd.read_excel('common.xlsx')
data.pop('ID')
data.pop('Окна')

data = data.loc[data['Адрес'] != 'Москва']
translator = Translator()
for i in data['Адрес']:
    res = translator.translate(i, src='ru', dest='en')
    print(res.text)

geolocator = Nominatim(user_agent="my_request")
location = geolocator.geocode("Moscow Slavyanskaya square 2")
print((location.latitude, location.longitude))

#print(data.info)
print(data.head())
