user_columns = {'UserID':'user_id', 'Email':'user_email', 'Password':'user_password'}
item_columns = {'ItemID':'item_id', 'Price':'item_price', 'ImageURL':'item_image_url'}
transaction_columns = {'TxID':'transaction_id', 'UserID': user_columns['UserID'], 'ItemID': item_columns['ItemID']}
