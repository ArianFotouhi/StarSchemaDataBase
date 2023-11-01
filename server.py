from utils.utils import create_database_schema, insert_data_generic, fetch_transaction_data, fetch_table
from database.schema_metadata import  (user_table_name, lounge_table_name, tx_table_name,
                               user_columns, lounge_columns, tx_columns,
                               user_types, lounge_types, tx_types)

from database.input_data import user_data, lounge_data, tx_data

# Create the database schema
columns= {}
for i in user_columns:
    columns[user_columns[i]] = user_types[user_columns[i]]
create_database_schema(
    table_name= user_table_name,
    columns= columns
)

columns= {}
for i in lounge_columns:
    columns[lounge_columns[i]] = lounge_types[lounge_columns[i]]
create_database_schema(
    table_name= lounge_table_name,
    columns=columns
)

columns= {}
for i in tx_columns:
    columns[tx_columns[i]] = tx_types[tx_columns[i]]
create_database_schema(
    table_name= tx_table_name,
    columns= columns,

    foreign_keys= {tx_columns['UserID']: f'User({user_columns["UserID"]})', 
                  tx_columns['LoungeID']: f'Item({lounge_columns["LoungeID"]})'}
)



# Insert data
insert_data_generic(user_table_name, user_data)
insert_data_generic(lounge_table_name, lounge_data)
insert_data_generic(tx_table_name, tx_data)

# Fetch and print transaction data
transaction_records = fetch_transaction_data()

for record in transaction_records:
    print(record)

print(30*'-')
fetched_data = fetch_table('User')
for record in fetched_data:
    print(record)

