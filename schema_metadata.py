
user_table_name = 'User'
user_columns = {'UserID':'user_id', 'Email':'user_email', 'Password':'user_password', 'Username':'username',
                'FirstName':'first_name','LastName':'last_name', 'Tel':'telephone', 'CreationDateTime':'creation_datetime',
                'UserStatus':'user_status','LastUpdate':'last_update'}
user_types = {user_columns['UserID']:'TEXT PRIMARY KEY', user_columns['Email']:'TEXT', user_columns['Password']:'TEXT',
              user_columns['Username']:'TEXT', user_columns['FirstName']:'TEXT', user_columns['LastName']:'TEXT',
              user_columns['Tel']:'TEXT', user_columns['CreationDateTime']:'DATETIME', user_columns['UserStatus']:'TEXT',
              user_columns['LastUpdate']:'DATETIME'}
# ------------------------------------------------------------
item_table_name = 'Lounge'
item_columns = {'LoungeID':'lounge_id', 'Name':'lounge_name', 'Country':'country',
                'Coordinates':'coordinates', 'AirportID':'airport_id', }
item_types = {item_columns['LoungeID']:'TEXT PRIMARY KEY', item_columns['Name']:'TEXT', item_columns['Country']:'TEXT',
              item_columns['Coordinates']:'TEXT', item_columns['AirportID']:'TEXT'}
# ------------------------------------------------------------
tx_table_name= 'Transaction'
tx_columns = {'TxID':'tx_id', 'UserID': user_columns['UserID'], 'ItemID': item_columns['ItemID'],
              'Status':'tx_status', 'TimeStamp':'time_stamp'}
tx_types = {tx_columns['TxID']:'TEXT PRIMARY KEY', tx_columns['UserID']:'TEXT', tx_columns['ItemID']:'TEXT',
            tx_columns['Status']:'TEXT', tx_columns['TimeStamp']:'DATETIME'}
# ------------------------------------------------------------



