from flask import Flask, jsonify, request
from utils.utils import insert_data_generic, fetch_table, fetch_columns, image_azure_blob_download
from utils.db_initialize import db_initializer
import urllib.parse
from utils.authentication import login, token_required, premium_token_required
from database.schema_metadata import  (
    user_table_name, lounge_table_name, tx_table_name, 
    country_table_name, event_table_name, amenity_table_name, 
    airport_table_name, order_table_name)

#initialize flask 
app = Flask(__name__)

#initialize database
db_initializer()


@app.route('/login', methods= ['POST'])
def user_login():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        token = login(username, password)
        if token:
            return jsonify({'token': token})
    return {'message': 'Invalid username or password'}, 401


@app.route('/get_table/<table_name>')
@token_required
def fetch_data(table_name):
    try:
        table_name = table_name.capitalize()
        fetched_data = fetch_table(table_name)
        fetch_info = []
        for record in fetched_data:
            fetch_info.append(record)
    except:
        fetch_info = 'Unsuccessful'
    
    return jsonify({'data':fetch_info})


@app.route('/get_columns/<table_name>')
@premium_token_required
def fetch_structure(table_name):
    table_name = table_name.capitalize()
    structure_info = fetch_columns(table_name)
    
    return jsonify({'data':structure_info})


@app.route('/upload/user', methods= ['POST'])
@token_required
def user_post():
       
    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))
    
    try:
        insert_data_generic(user_table_name, data)      

        fetched_data = fetch_table(user_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'
    
    return jsonify({'data': message})
    

@app.route('/upload/lounge', methods= ['POST'])
@token_required
def lounge_post():

    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))

    try:
        insert_data_generic(lounge_table_name, data)        

        fetched_data = fetch_table(lounge_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'

    return jsonify({'data':message})

@app.route('/upload/transaction', methods= ['POST'])
def tx_post():

    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))

    try:
        insert_data_generic(tx_table_name, data)        

        fetched_data = fetch_table(tx_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'
    
    return jsonify({'data':message})


@app.route('/upload/country', methods=  ['POST'])
@token_required
def country_post():

    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))
    try:
        insert_data_generic(country_table_name, data)        

        fetched_data = fetch_table(country_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'
    
    return jsonify({'data':message})


@app.route('/upload/event', methods= ['POST'])
@token_required
def event_post():
    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))

    try:
        insert_data_generic(event_table_name, data)        

        fetched_data = fetch_table(event_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'

    return jsonify({'data':message})


@app.route('/upload/amenity', methods= ['POST'])
@token_required
def amenity_post():

    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))

    try:
        insert_data_generic(amenity_table_name, data)        

        fetched_data = fetch_table(amenity_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'
    return jsonify({'data':message})


@app.route('/upload/airport', methods= ['POST'])
@token_required
def airport_post():

    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))

    try:
        insert_data_generic(airport_table_name, data)        

        fetched_data = fetch_table(airport_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'
    
    return jsonify({'data':message})


@app.route('/upload/order', methods= ['POST'])
@token_required
def order_post():

    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))

    try:
        insert_data_generic(order_table_name, data)        

        fetched_data = fetch_table(order_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'
    
    return jsonify({'data':message})


@app.route('/lounge/image', methods= ['POST', 'GET'])
# @token_required
def lounge_image():

    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))

    response = image_azure_blob_download(container_name= data['container'],
                                         blob_name= data['blob_name'])

    return jsonify({'data': response})



if __name__ == "__main__":
    app.run()