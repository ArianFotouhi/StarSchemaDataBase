
user_table_name = 'User'
user_columns = {'UserID':'user_id', 'Email':'user_email', 'Password':'user_password'}
user_types = {user_columns['UserID']:'TEXT PRIMARY KEY', user_columns['Email']:'TEXT', user_columns['Password']:'TEXT'}
# ------------------------------------------------------------
item_table_name = 'Item'
item_columns = {'ItemID':'item_id', 'Price':'item_price', 'ImageURL':'item_image_url'}
item_types = {item_columns['ItemID']:'TEXT PRIMARY KEY', item_columns['Price']:'REAL', item_columns['ImageURL']:'TEXT'}
# ------------------------------------------------------------
tx_table_name= 'Transaction'
tx_columns = {'TxID':'transaction_id', 'UserID': user_columns['UserID'], 'ItemID': item_columns['ItemID']}
tx_types = {tx_columns['TxID']:'TEXT PRIMARY KEY', tx_columns['UserID']:'TEXT', tx_columns['ItemID']:'TEXT'}
# ------------------------------------------------------------



