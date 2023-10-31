from utils import create_database_schema, insert_data_generic, fetch_transaction_data


user_id = 'user4'
item_id = 'item4'
transaction_id='trans4'

user_data = {'user_id': user_id, 'user_email': 'user1@example.com', 'user_password': 'password1'}
item_data = {'item_id': item_id, 'item_price': 19.99, 'item_image_url': 'item1.jpg'}
transaction_data = {'transaction_id': transaction_id, 'user_id': user_id, 'item_id': item_id}



# Create the database schema
create_database_schema(
    table_name='User',
    columns={'user_id': 'TEXT PRIMARY KEY', 'user_email': 'TEXT', 'user_password': 'TEXT'}
)

create_database_schema(
    table_name='Item',
    columns={'item_id': 'TEXT PRIMARY KEY', 'item_price': 'REAL', 'item_image_url': 'TEXT'}
)

create_database_schema(
    table_name='Transaction',
    columns={'transaction_id': 'TEXT PRIMARY KEY', 'user_id': 'TEXT', 'item_id': 'TEXT'},
    foreign_keys={'user_id': 'User(user_id)', 'item_id': 'Item(item_id)'}
)




# Insert data
insert_data_generic('User', user_data)
insert_data_generic('Item', item_data)
insert_data_generic('Transaction', transaction_data)

# Fetch and print transaction data
transaction_records = fetch_transaction_data()

for record in transaction_records:
    print(record)