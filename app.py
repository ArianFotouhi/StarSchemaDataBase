import sqlite3

def create_database_schema():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('my_new_database.db')  # Create a new database file
    cursor = conn.cursor()

    # Create User table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        user_id TEXT PRIMARY KEY,
        user_email TEXT,
        user_password TEXT
    )''')

    # Create Item table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Item (
        item_id TEXT PRIMARY KEY,
        item_price REAL,
        item_image_url TEXT
    )''')

    # Create Transaction table with foreign keys to User and Item
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Transaction" (
        transaction_id TEXT PRIMARY KEY,
        user_id TEXT,
        item_id TEXT,
        FOREIGN KEY (user_id) REFERENCES User(user_id),
        FOREIGN KEY (item_id) REFERENCES Item(item_id)
    )''')

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
create_database_schema()

# Insert data
user_id = 'user3'
item_id = 'item3'
transaction_id='trans3'

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
