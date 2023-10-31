import sqlite3

def create_database_schema(table_name, columns, foreign_keys=None):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('my_new_database.db')  # Create a new database file
    cursor = conn.cursor()

    # Create the table with the provided name and columns
    create_table_sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ('
    create_table_sql += ', '.join([f'{col} {data_type}' for col, data_type in columns.items()])
    if foreign_keys:
        create_table_sql += ', '
        create_table_sql += ', '.join([f'FOREIGN KEY ({col}) REFERENCES {reference}' for col, reference in foreign_keys.items()])
    create_table_sql += ')'
    print(create_table_sql)
    cursor.execute(create_table_sql)

    conn.commit()


def insert_data_generic(table_name, data):
    with sqlite3.connect('my_new_database.db') as conn:  # Use the new database file
        cursor = conn.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join([':' + key for key in data.keys()])
        insert_query = f'INSERT INTO "{table_name}" ({columns}) VALUES ({placeholders})'
        print(insert_query)
        cursor.execute(insert_query, data)
        conn.commit()

def fetch_transaction_data():
    with sqlite3.connect('my_new_database.db') as conn:  # Use the new database file
        cursor = conn.cursor()
        cursor.execute('''
            SELECT "T".transaction_id, "U".user_email, "I".item_price, "I".item_image_url
            FROM "Transaction" "T"
            JOIN "User" "U" ON "T".user_id = "U".user_id
            JOIN "Item" "I" ON "T".item_id = "I".item_id
        ''')
        data = cursor.fetchall()
        return data

# Create the database schema
# Example usage
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
user_id = 'user1'
item_id = 'item1'
transaction_id='trans1'

user_data = {'user_id': user_id, 'user_email': 'user1@example.com', 'user_password': 'password1'}
item_data = {'item_id': item_id, 'item_price': 19.99, 'item_image_url': 'item1.jpg'}
transaction_data = {'transaction_id': transaction_id, 'user_id': user_id, 'item_id': item_id}



insert_data_generic('User', user_data)
insert_data_generic('Item', item_data)
insert_data_generic('Transaction', transaction_data)

# Fetch and print transaction data
transaction_records = fetch_transaction_data()

for record in transaction_records:
    print(record)
