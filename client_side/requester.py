import requests
from input_data import (user_data, lounge_data, tx_data,
                        country_data, event_data, amenity_data,
                        airport_data)


# url= 'https://iegapp.pythonanywhere.com/geo/'

# url = 'http://127.0.0.1:5000/upload/user'
# payload = user_data

# url = 'http://127.0.0.1:5000/upload/lounge'
# payload = lounge_data

# url = 'http://127.0.0.1:5000/upload/transaction'
# payload = tx_data

# url = 'http://127.0.0.1:5000/upload/country'
# payload = country_data

# url = 'http://127.0.0.1:5000/upload/event'
# payload = event_data

# url = 'http://127.0.0.1:5000/upload/amenity'
# payload = amenity_data

url = 'http://127.0.0.1:5000/upload/airport'
payload = airport_data

response = requests.post(url, data=payload)

url = 'http://127.0.0.1:5000/'
# response = requests.get(url)

print(response.json())