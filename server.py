from utils import create_database_schema, insert_data_generic, fetch_transaction_data
from schema_metadata import  (user_table_name, item_table_name, tx_table_name,
                               user_columns, item_columns, tx_columns,
                               user_types, item_types, tx_types)

user_id = 'user2'
item_id = 'item2'
transaction_id ='trans2'


user_data = {user_columns['UserID']: user_id, 
            user_columns['Email']: 'user1@example.com', 
            user_columns['Password']: 'password1'}

item_data = {item_columns['ItemID']: item_id, 
            item_columns['Price']: 19.99,
            item_columns['ImageURL']: 'item1.jpg'}

transaction_data = {tx_columns['TxID']: transaction_id,
                     tx_columns['UserID']: user_id, 
                     tx_columns['ItemID']: item_id}


# Create the database schema
create_database_schema(
    table_name= user_table_name,
    columns={user_columns['UserID']: user_types[user_columns['UserID']], 
             user_columns['Email']: user_types[user_columns['Email']], 
             user_columns['Password']: user_types[user_columns['Password']]}
)

create_database_schema(
    table_name= item_table_name,
    columns={item_columns['ItemID']: item_types[item_columns['ItemID']],
            item_columns['Price']: item_types[item_columns['Price']],
            item_columns['ImageURL']: item_types[item_columns['ImageURL']]}
)

create_database_schema(
    table_name= tx_table_name,
    columns={tx_columns['TxID']: tx_types[tx_columns['TxID']], 
             tx_columns['UserID']: tx_types[tx_columns['UserID']], 
             tx_columns['ItemID']: tx_types[tx_columns['ItemID']]},
             
    foreign_keys={tx_columns['UserID']: f'User({user_columns["UserID"]})', 
                  tx_columns['ItemID']: f'Item({item_columns["ItemID"]})'}
)



# Insert data
insert_data_generic(user_table_name, user_data)
insert_data_generic(item_table_name, item_data)
insert_data_generic(tx_table_name, transaction_data)

# Fetch and print transaction data
transaction_records = fetch_transaction_data()

for record in transaction_records:
    print(record)