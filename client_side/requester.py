import requests
from input_data import user_data

# url = 'http://127.0.0.1:8000/geo/'
# url= 'https://iegapp.pythonanywhere.com/geo/'
url = 'http://127.0.0.1:5000/upload/user'

# payload = {
#     'data':'Hi'
# }
payload = user_data

response = requests.post(url, data=payload)
# response = requests.get(url)

print(response.json())