from database.schema_metadata import  user_columns, lounge_columns, tx_columns
                               

user_id = 'user4'
lounge_id = 'item4'
transaction_id ='trans4'


user_data = {
            user_columns['UserID']: user_id,
            user_columns['Email']: 'user1@example.com',
            user_columns['Password']: 'password1',

            user_columns['Username']: 'username1',
            user_columns['FirstName']: 'Ed',
            user_columns['LastName']: 'Jackson',

            user_columns['Tel']: '1234567890',
            user_columns['CreationDateTime']: '22-10-2023 10:55:11',

            }

lounge_data = {lounge_columns['LoungeID']: lounge_id, 
            lounge_columns['Name']: 'YYL int',
            lounge_columns['AirportID']: 'YYL'}

tx_data = {tx_columns['TxID']: transaction_id,
                     tx_columns['UserID']: user_id, 
                     tx_columns['LoungeID']: lounge_id}

