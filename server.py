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



# @app.route('/')
# def index():
#     # Insert data
    
#     # ----------------------------------------
#     insert_data_generic(lounge_table_name, lounge_data)
#     # ----------------------------------------
#     insert_data_generic(tx_table_name, tx_data)
#     # ----------------------------------------
#     insert_data_generic(country_table_name, country_data)
#     # ----------------------------------------
#     insert_data_generic(event_table_name, even_data)
#     # ----------------------------------------
#     insert_data_generic(amenity_table_name, amenity_data)
#     # ----------------------------------------
#     insert_data_generic(airport_table_name, airport_data)
#     # ----------------------------------------




#     print(15*'-'+f'{lounge_table_name}'+15*'-')
#     fetched_data = fetch_table(lounge_table_name)
#     for record in fetched_data:
#         print(record)

#     print(15*'-'+f'{tx_table_name}'+15*'-')
#     fetched_data = fetch_table(tx_table_name)
#     for record in fetched_data:
#         print(record)

#     print(15*'-'+f'{country_table_name}'+15*'-')
#     fetched_data = fetch_table(country_table_name)
#     for record in fetched_data:
#         print(record)

#     print(15*'-'+f'{event_table_name}'+15*'-')
#     fetched_data = fetch_table(event_table_name)
#     for record in fetched_data:
#         print(record)

#     print(15*'-'+f'{amenity_table_name}'+15*'-')
#     fetched_data = fetch_table(amenity_table_name)
#     for record in fetched_data:
#         print(record)

#     print(15*'-'+f'{airport_table_name}'+15*'-')
#     fetched_data = fetch_table(airport_table_name)
#     for record in fetched_data:
#         print(record)

#     return jsonify({'data':'Successful!'})

@app.route('/upload/user', methods=['POST'])
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
        message = e
    finally:
        print(message)
        return jsonify({'response':message})
    
if __name__ == "__main__":
    app.run()