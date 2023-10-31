# ------------------------------------------------------------
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
country_table_name= 'Country'
country_columns = {'CountryName':'name', 'Currency': 'currency', 'Language': 'language',
                    'TelCode':'telephone_code', 'FlagImageURL':'flag_image_url', 'TimeStamp':'time_stamp'}
country_types = {country_columns['CountryName']:'TEXT PRIMARY KEY', country_columns['Currency']:'TEXT', country_columns['Language']:'TEXT',
            country_columns['TelCode']:'TEXT', country_columns['FlagImageURL']:'TEXT', country_columns['TimeStamp']:'DATETIME'}

# ------------------------------------------------------------
event_table_name= 'LoungeEvent'
event_columns = {'EventID':'event_id', 'EventOwner': 'event_owner', 'EventName': 'event_name',
                    'EventPartners':'event_partners', 'EventDuration':'event_duration', 
                    'EventDescription':'event_description', 'Event_DateTime':'event_datetime', 'LastUpdate':'last_update'}
event_types = {
            event_columns['EventID']:'TEXT PRIMARY KEY', event_columns['EventOwner']:'TEXT', event_columns['EventName']:'TEXT',
            event_columns['EventPartners']:'TEXT', event_columns['EventDuration']:'TEXT', event_columns['EventDescription']:'TEXT',
            event_columns['TimeStamp']:'DATETIME'
            }

# ------------------------------------------------------------
amenity_table_name= 'Amenities'
amenity_columns = {'AmenityID':'amenity_id', 'AmenityStatus': 'amenity_status', 'AmenityName': 'amenity_name',
                    'ImageURL':'image_url', 'LastUpdate':'last_update'}
amenity_types = {amenity_columns['AmenityID']:'TEXT PRIMARY KEY', amenity_columns['AmenityStatus']:'TEXT', amenity_columns['AmenityName']:'TEXT',
            amenity_columns['ImageURL']:'TEXT',  amenity_columns['LastUpdate']:'DATETIME'}

# ------------------------------------------------------------
airport_table_name= 'Airport'
airport_columns = {'IATACode':'IATA_code', 'AirportName':'airport_name' ,'Country': 'country', 'City': 'city',
                    'Coordinates':'coordinates', 'Region': 'region', 'ImageURL':'image_url',
                    'LocationTimeZone':'time_zone'}
airport_types = {airport_columns['IATACode']:'TEXT PRIMARY KEY', airport_columns['AirportName']:'TEXT', airport_columns['Country']:'TEXT',
            airport_columns['City']:'TEXT',  airport_columns['Coordinates']:'TEXT', airport_columns['Region']:'TEXT',
            airport_columns['ImageURL']:'TEXT', airport_columns['LocationTimeZone']:'TEXT'}
