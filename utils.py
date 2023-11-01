import sqlite3
from schema_metadata import ( user_table_name, lounge_table_name, tx_table_name,
                              user_columns, lounge_columns, tx_columns)

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
            SELECT "T".{tx_columns['TxID']}, "U".{user_columns['UserID']}, 
            "I".{lounge_columns['Name']}, "I".{lounge_columns['AirportID']}
            FROM "{tx_table_name}" "T"
            JOIN "{user_table_name}" "U" ON "T".{tx_columns['UserID']} = "U".{user_columns['UserID']}
            JOIN "{lounge_table_name}" "I" ON "T".{tx_columns['LoungeID']} = "I".{lounge_columns['LoungeID']}
        ''')
        data = cursor.fetchall()
        return data
    
def fetch_table(table_name):
    with sqlite3.connect(db_name) as conn:  # Use the new database file
        cursor = conn.cursor()
        cursor.execute(f'''
            SELECT * FROM "{table_name}" 
        ''')
        data = cursor.fetchall()
        return data