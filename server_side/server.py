from flask import Flask, jsonify, request, session
from utils.utils import insert_data_generic, fetch_table, fetch_columns
from utils.db_initialize import db_initializer
import urllib.parse
from utils.authentication import login, token_required, premium_token_required
from database.schema_metadata import  (
    user_table_name, lounge_table_name, tx_table_name, 
    country_table_name, event_table_name, amenity_table_name, 
    airport_table_name,)


#initialize flask 
app = Flask(__name__)

#initialize database
db_initializer()


@app.route('/login', methods=['POST'])
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
    structure_info = fetch_columns(table_name)
    
    return jsonify({'data':structure_info})



@app.route('/upload/user', methods=['POST'])
@token_required
def user_post():
       
    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))
    # print('data', data_dict)
    # print('type', type(data_dict))
    try:


        insert_data_generic(user_table_name, data)      


        fetched_data = fetch_table(user_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = f'Data Upload failed due to: {e}'
    
    return jsonify({'response': message})
    
@app.route('/upload/lounge', methods=['POST'])
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
        message = e
    finally:
        print(message)
        return jsonify({'response':message})

@app.route('/upload/transaction', methods=['POST'])
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
        message = e
    finally:
        print(message)
        return jsonify({'response':message})

@app.route('/upload/country', methods=['POST'])
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
        message = e
    finally:
        print(message)
        return jsonify({'response':message})

@app.route('/upload/event', methods=['POST'])
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
        message = e
    finally:
        print(message)
        return jsonify({'response':message})

@app.route('/upload/amenity', methods=['POST'])
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
        message = e
    finally:
        print(message)
        return jsonify({'response':message})

@app.route('/upload/airport', methods=['POST'])
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
        message = e
    finally:
        print(message)
        return jsonify({'response':message})

if __name__ == "__main__":
    app.run()