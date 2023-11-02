import requests


# url = 'http://127.0.0.1:8000/geo/'
# url= 'https://iegapp.pythonanywhere.com/geo/'
url = 'http://127.0.0.1:5000/req/user'

payload = {
    'data':'Hi'
}

response = requests.post(url, data=payload)
# response = requests.get(url)

print(response.json())