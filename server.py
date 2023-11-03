from flask import Flask, jsonify, request
from utils.utils import insert_data_generic, fetch_table
from utils.db_initialize import db_initializer
import urllib.parse

from database.schema_metadata import  (
    user_table_name, lounge_table_name, tx_table_name, 
    country_table_name, event_table_name, amenity_table_name, 
    airport_table_name,)


#initialize flask 
app = Flask(__name__)

#initialize database
db_initializer()



@app.route('/get_table/<table_name>')
def fetch_data(table_name):
    try:
        fetched_data = fetch_table(table_name)
        fetch_info = []
        for record in fetched_data:
            fetch_info.append(record)
    except:
        fetch_info = 'Unsuccessful'
    
    return jsonify({'data':fetch_info})

@app.route('/authentication', methods=['POST'])
def authentication():
    username = 'admin'
    password = '123456'
    form_username = request.form['username']
    form_password = request.form['password']
    

    if username == form_username and password == form_password:
        message = 'generatedtoken'
        status = True
    else:
        message = 'Username and Password do not match!'
        status = False
    return jsonify({'message':message, 'status':status})

@app.route('/upload/user', methods=['POST'])
def user_post():

    data = request.get_data()
    data = dict(urllib.parse.parse_qsl(data.decode()))
    token =data.pop('token')
    # print('data', data_dict)
    # print('type', type(data_dict))
    try:
        if token != 'generatedtoken':
            raise Exception('Unauthorized access!')

        insert_data_generic(user_table_name, data)      


        fetched_data = fetch_table(user_table_name)
        for record in fetched_data:
            print(record)
        message = 'Successful'
    except Exception as e:
        message = 'Unauthorized access'
    
    print(message)
    return jsonify({'response':message})
    
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