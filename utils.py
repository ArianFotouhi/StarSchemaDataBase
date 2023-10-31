import sqlite3
db_name = 'database1.db'
def create_database_schema(table_name, columns, foreign_keys=None):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)  # Create a new database file
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
    with sqlite3.connect(db_name) as conn:  # Use the new database file
        cursor = conn.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join([':' + key for key in data.keys()])
        insert_query = f'INSERT INTO "{table_name}" ({columns}) VALUES ({placeholders})'
        print(insert_query)
        cursor.execute(insert_query, data)
        conn.commit()

def fetch_transaction_data():
    with sqlite3.connect(db_name) as conn:  # Use the new database file
        cursor = conn.cursor()
        cursor.execute('''
            SELECT "T".transaction_id, "U".user_email, "I".item_price, "I".item_image_url
            FROM "Transaction" "T"
            JOIN "User" "U" ON "T".user_id = "U".user_id
            JOIN "Item" "I" ON "T".item_id = "I".item_id
        ''')
        data = cursor.fetchall()
        return data
