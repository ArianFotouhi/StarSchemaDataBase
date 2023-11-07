import sqlite3

from sqlalchemy import inspect
from sqlalchemy import create_engine

# from database.schema_metadata import ( user_table_name, lounge_table_name, tx_table_name,
#                               user_columns, lounge_columns, tx_columns)

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


# def fetch_transaction_data():
#     with sqlite3.connect(db_name) as conn:  # Use the new database file
#         cursor = conn.cursor()
#         cursor.execute(f'''
#             SELECT "T".{tx_columns['TxID']}, "U".{user_columns['UserID']}, 
#             "I".{lounge_columns['Name']}, "I".{lounge_columns['AirportID']}
#             FROM "{tx_table_name}" "T"
#             JOIN "{user_table_name}" "U" ON "T".{tx_columns['UserID']} = "U".{user_columns['UserID']}
#             JOIN "{lounge_table_name}" "I" ON "T".{tx_columns['LoungeID']} = "I".{lounge_columns['LoungeID']}
#         ''')
#         data = cursor.fetchall()
#         return data
    
def fetch_table(table_name):
    with sqlite3.connect(db_name) as conn:  # Use the new database file
        cursor = conn.cursor()
        cursor.execute(f'''
            SELECT * FROM "{table_name}" 
        ''')
        data = cursor.fetchall()
        return data
    

def fetch_columns(table_name):
    engine = create_engine('sqlite:///' + db_name)
    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        return 'Error: Table not found'
    
    columns = inspector.get_columns(table_name)
    column_info = [{'name': col['name'], 'type': str(col['type'])} for col in columns]

    return column_info


def image_azure_blob_download(container_name, blob_name):
    from azure.storage.blob import BlobServiceClient, generate_container_sas, ContainerSasPermissions, ResourceTypes
    import datetime 
    
    import json
    with open("config/config.json") as config_file:
        config = json.load(config_file)

    connection_string = config["connection_string"]
    access_key = config["access_key"]
    
    

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get the container client
    container_client = blob_service_client.get_container_client(container_name)

    # Check if the blob exists
    if container_client.get_blob_client(blob_name).exists():
        # Define the permissions and expiration time for the SAS token
        sas_container_permissions = ContainerSasPermissions(read=True)  # Adjust permissions as needed
        sas_resource_types = ResourceTypes(object=True)

        sas_token = generate_container_sas(
            container_name=container_name,
            account_name=blob_service_client.account_name,
            account_key= access_key,
            permission=sas_container_permissions,
            expiry=datetime.datetime.utcnow() + datetime.timedelta(hours=1),  
            resource_types=sas_resource_types
        )

        # Construct the URL with the SAS token
        sas_url = f"https://{container_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
        return sas_url
    else:
        return 'Image not found'
