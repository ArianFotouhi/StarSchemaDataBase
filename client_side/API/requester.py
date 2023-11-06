import requests
from input.input_data import ( lounge_data, tx_data,
                        country_data, event_data, amenity_data,
                        airport_data)
from input.input_data import data_csv_reader



#authorization
url = 'http://127.0.0.1:5000/'
table = 'lounge'
#tables:
#user, lounge, transaction, country, event, amenity, airport




# User credentials for logging in
username = 'user2'
password = 'password2'

# Login to obtain a JWT token
login_data = {
    'username': username,
    'password': password
}

################################### Login ##################################
login_response = requests.post(f'{url}/login', json=login_data)

if login_response.status_code == 200:
    token = login_response.json()['token']
    print('Login successful. Token obtained')
    # Set the Authorization header with the JWT token
    headers = {'Authorization': token}


################################### GET ##################################
    ## Read data
    #1
    # response = requests.get(f'{url}/get_table/{table}', headers=headers)
    
    ####################################

    # Read columns  
    #2.
    #response = requests.get(f'{url}/get_columns/{table}', headers=headers)
    
################################### POST ##################################

    #Write data by file
    # 3.
    # user_data = data_csv_reader(file_name='input/input.xlsx')
    # for record in user_data:
    #     response = requests.post(f'{url}/upload/{table}', data=record, headers=headers)

####################################

    # Write data by code
    # 4.

    payload = lounge_data
    response = requests.post(f'{url}/upload/{table}', data=payload, headers=headers)

    if response.status_code == 200:
        print('Successful Request:')
        for i in response.json()['data']:
            print(i)

    else:
        print('Request Failed:')
        print(response.status_code, response.text)
else:
    print('Login failed:')
    print(login_response.status_code, login_response.text)













