from utils import create_database_schema, insert_data_generic, fetch_transaction_data


user_id = 'user1'
item_id = 'item1'
transaction_id='trans1'

user_columns = {'UserID':'user_id', 'Email':'user_email', 'Password':'user_password'}
item_columns = {'ItemID':'item_id', 'Price':'item_price', 'ImageURL':'item_image_url'}
transaction_columns = {'TxID':'transaction_id', 'UserID': user_columns['UserID'], 'ItemID': item_columns['ItemID']}


user_data = {user_columns['UserID']: user_id, 
            user_columns['Email']: 'user1@example.com', 
            user_columns['Password']: 'password1'}

item_data = {item_columns['ItemID']: item_id, 
            item_columns['Price']: 19.99,
            item_columns['ImageURL']: 'item1.jpg'}

transaction_data = {transaction_columns['TxID']: transaction_id,
                     transaction_columns['UserID']: user_id, 
                     transaction_columns['ItemID']: item_id}


# Create the database schema
create_database_schema(
    table_name='User',
    columns={user_columns['UserID']: 'TEXT PRIMARY KEY', 
             user_columns['Email']: 'TEXT', 
             user_columns['Password']: 'TEXT'}
)

create_database_schema(
    table_name='Item',
    columns={item_columns['ItemID']: 'TEXT PRIMARY KEY',
            item_columns['Price']: 'REAL',
            item_columns['ImageURL']: 'TEXT'}
)

create_database_schema(
    table_name='Transaction',
    columns={transaction_columns['TxID']: 'TEXT PRIMARY KEY', 
             transaction_columns['UserID']: 'TEXT', 
             transaction_columns['ItemID']: 'TEXT'},
    foreign_keys={transaction_columns['UserID']: f'User({user_columns["UserID"]})', 
                  transaction_columns['ItemID']: f'Item({item_columns["ItemID"]})'}
)




# Insert data
insert_data_generic('User', user_data)
insert_data_generic('Item', item_data)
insert_data_generic('Transaction', transaction_data)

# Fetch and print transaction data
transaction_records = fetch_transaction_data()

for record in transaction_records:
    print(record)