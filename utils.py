import sqlite3
from schema_metadata import user_columns, item_columns, transaction_columns


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

    cursor.execute(create_table_sql)

    conn.commit()


def insert_data_generic(table_name, data):
    with sqlite3.connect(db_name) as conn:  # Use the new database file
        cursor = conn.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join([':' + key for key in data.keys()])
        insert_query = f'INSERT INTO "{table_name}" ({columns}) VALUES ({placeholders})'
        
        cursor.execute(insert_query, data)
        conn.commit()


def fetch_transaction_data():
    with sqlite3.connect(db_name) as conn:  # Use the new database file
        cursor = conn.cursor()
        cursor.execute(f'''
            SELECT "T".{transaction_columns['TxID']}, "U".{user_columns['UserID']}, "I".{item_columns['Price']}, "I".{item_columns['ImageURL']}
            FROM "Transaction" "T"
            JOIN "User" "U" ON "T".{transaction_columns['UserID']} = "U".{user_columns['UserID']}
            JOIN "Item" "I" ON "T".{transaction_columns['ItemID']} = "I".{item_columns['ItemID']}
        ''')
        data = cursor.fetchall()
        return data
