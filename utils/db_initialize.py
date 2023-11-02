from utils.utils import create_database_schema
from database.schema_metadata import  (
    user_table_name, lounge_table_name, tx_table_name, country_table_name, event_table_name, amenity_table_name, airport_table_name,
                               user_columns, lounge_columns, tx_columns, country_columns, event_columns, amenity_columns, airport_columns,
                               user_types, lounge_types, tx_types,country_types, event_types, amenity_types, airport_types,
                               )
def db_initializer():
    # Create the database schema
    columns= {}
    for i in user_columns:
        columns[user_columns[i]] = user_types[user_columns[i]]
    create_database_schema(
        table_name= user_table_name,
        columns= columns
    )
    # ----------------------------------------
    columns= {}
    for i in lounge_columns:
        columns[lounge_columns[i]] = lounge_types[lounge_columns[i]]
    create_database_schema(
        table_name= lounge_table_name,
        columns=columns
    )
    # ----------------------------------------
    columns= {}
    for i in tx_columns:
        columns[tx_columns[i]] = tx_types[tx_columns[i]]
    create_database_schema(
        table_name= tx_table_name,
        columns= columns,

        foreign_keys= {tx_columns['UserID']: f'User({user_columns["UserID"]})', 
                    tx_columns['LoungeID']: f'Item({lounge_columns["LoungeID"]})'}
    )
    # ----------------------------------------
    columns= {}
    for i in country_columns:
        columns[country_columns[i]] = country_types[country_columns[i]]
    create_database_schema(
        table_name= country_table_name,
        columns= columns
    )
    # ----------------------------------------
    columns= {}
    for i in event_columns:
        columns[event_columns[i]] = event_types[event_columns[i]]
    create_database_schema(
        table_name= event_table_name,
        columns= columns
    )
    # ----------------------------------------
    columns= {}
    for i in amenity_columns:
        columns[amenity_columns[i]] = amenity_types[amenity_columns[i]]
    create_database_schema(
        table_name= amenity_table_name,
        columns= columns
    )
    # ----------------------------------------
    columns= {}
    for i in airport_columns:
        columns[airport_columns[i]] = airport_types[airport_columns[i]]
    create_database_schema(
        table_name= airport_table_name,
        columns= columns
    )
    # ----------------------------------------