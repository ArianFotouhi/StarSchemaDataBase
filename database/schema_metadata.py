# ------------------------------------------------------------
user_table_name = 'User'
user_columns = {'UserID':'user_id', 'Email':'user_email', 'Password':'user_password', 'Username':'username',
                'FirstName':'first_name','LastName':'last_name', 'Tel':'telephone', 'CreationDateTime':'creation_datetime',
                'UserStatus':'user_status','LastUpdate':'last_update'}
user_types = {
            user_columns['UserID']:'INTEGER PRIMARY KEY AUTOINCREMENT', 
            user_columns['Email']:'TEXT', 
            user_columns['Password']:'TEXT',
            user_columns['Username']:'TEXT', 
            user_columns['FirstName']:'TEXT', 
            user_columns['LastName']:'TEXT',
            user_columns['Tel']:'TEXT', 
            user_columns['CreationDateTime']:'DATETIME', 
            user_columns['UserStatus']:'TEXT',
            user_columns['LastUpdate']:'DATETIME'
              }

# ------------------------------------------------------------
lounge_table_name = 'Lounge'
lounge_columns = {'LoungeID':'lounge_id', 'Name':'lounge_name', 'Country':'country',
                'Coordinates':'coordinates', 'AirportID':'airport_id', 'Description':'description',
                'TimeZone':'time_zone', 'LoungeType':'lounge_type','LoungeCapacityStatus':'capacity_status',
                'AccessRequirements':'access_requirements', 'OperatingHours':'operate_hours','Amenities':'amenities',
                'AccessibilityFeatures':'accessibility_features', 'Capacity':'capacity','EntryFee':'entry_fee',
                'Email':'email', 'Tel':'tel_no','WebsiteURL':'website',
                'SecurityInfo':'security_info', 'Reservation':'reservation','ActivityStatus':'activity_status',
                'LastUpdate':'last_update', 'ImageURL':'image_url','SocialMediaLink':'social_media_link',
                'Owner':'owner', 'OnSiteTransportation':'onsite_transportation'

                    }
lounge_types = {
            lounge_columns['LoungeID']:'INTEGER PRIMARY KEY AUTOINCREMENT', 
            lounge_columns['Name']:'TEXT', 
            lounge_columns['Country']:'TEXT',
            lounge_columns['Coordinates']:'TEXT', 
            lounge_columns['AirportID']:'TEXT',

            lounge_columns['Description']:'TEXT',
            lounge_columns['TimeZone']:'TEXT', 
            lounge_columns['LoungeType']:'TEXT',
            lounge_columns['LoungeCapacityStatus']:'TEXT',
            lounge_columns['AccessRequirements']:'TEXT',
            lounge_columns['OperatingHours']:'TEXT',
            lounge_columns['Amenities']:'TEXT',
            lounge_columns['AccessibilityFeatures']:'TEXT',
            lounge_columns['Capacity']:'INTEGER',
            lounge_columns['EntryFee']:'NUMERIC',
            lounge_columns['Email']:'TEXT',
            lounge_columns['Tel']:'TEXT',
            lounge_columns['WebsiteURL']:'TEXT',
            lounge_columns['SecurityInfo']:'TEXT',
            lounge_columns['Reservation']:'TEXT',
            lounge_columns['ActivityStatus']:'TEXT',
            lounge_columns['LastUpdate']:'DATETIME',
            lounge_columns['ImageURL']:'TEXT',
            lounge_columns['SocialMediaLink']:'TEXT',
            lounge_columns['Owner']:'TEXT',
            lounge_columns['OnSiteTransportation']:'TEXT',
            }

# ------------------------------------------------------------
tx_table_name= 'Transaction'
tx_columns = {'TxID':'tx_id', 'UserID': user_columns['UserID'], 'LoungeID': lounge_columns['LoungeID'],
              'Status':'tx_status', 'TimeStamp':'time_stamp'}
tx_types = {
            tx_columns['TxID']:'INTEGER PRIMARY KEY AUTOINCREMENT', 
            tx_columns['UserID']:'INTEGER', 
            tx_columns['LoungeID']:'INTEGER',
            tx_columns['Status']:'TEXT', 
            tx_columns['TimeStamp']:'DATETIME'
            }

# ------------------------------------------------------------
country_table_name= 'Country'
country_columns = {'CountryName':'name', 'Currency': 'currency', 'Language': 'language',
                    'TelCode':'telephone_code', 'FlagImageURL':'flag_image_url', 'TimeStamp':'time_stamp'}
country_types = {
                country_columns['CountryName']:'TEXT PRIMARY KEY', 
                country_columns['Currency']:'TEXT', 
                country_columns['Language']:'TEXT',
                country_columns['TelCode']:'TEXT', 
                country_columns['FlagImageURL']:'TEXT', 
                country_columns['TimeStamp']:'DATETIME'
                }

# ------------------------------------------------------------
event_table_name= 'LoungeEvent'
event_columns = {'EventID':'event_id', 'EventOwner': 'event_owner', 'EventName': 'event_name',
                    'EventPartners':'event_partners', 'EventDuration':'event_duration', 
                    'EventDescription':'event_description', 'Event_DateTime':'event_datetime', 'LastUpdate':'last_update'}
event_types = {
            event_columns['EventID']:'INTEGER PRIMARY KEY AUTOINCREMENT', 
            event_columns['EventOwner']:'TEXT', 
            event_columns['EventName']:'TEXT',
            event_columns['EventPartners']:'TEXT', 
            event_columns['EventDuration']:'TEXT', 
            event_columns['EventDescription']:'TEXT',
            event_columns['Event_DateTime']:'DATETIME', 
            event_columns['LastUpdate']:'DATETIME'
            }

# ------------------------------------------------------------
amenity_table_name= 'Amenities'
amenity_columns = {'AmenityID':'amenity_id', 'AmenityStatus': 'amenity_status', 'AmenityName': 'amenity_name',
                    'ImageURL':'image_url', 'LastUpdate':'last_update'}
amenity_types = {
            amenity_columns['AmenityID']:'INTEGER PRIMARY KEY AUTOINCREMENT', 
            amenity_columns['AmenityStatus']:'TEXT', 
            amenity_columns['AmenityName']:'TEXT',
            amenity_columns['ImageURL']:'TEXT',  
            amenity_columns['LastUpdate']:'DATETIME'
            }

# ------------------------------------------------------------
airport_table_name= 'Airport'
airport_columns = {'IATACode':'IATA_code', 'AirportName':'airport_name' ,'Country': 'country', 'City': 'city',
                    'Coordinates':'coordinates', 'Region': 'region', 'ImageURL':'image_url',
                    }
airport_types = {
            airport_columns['IATACode']:'TEXT PRIMARY KEY', 
            airport_columns['AirportName']:'TEXT', 
            airport_columns['Country']:'TEXT',
            airport_columns['City']:'TEXT',  
            airport_columns['Coordinates']:'TEXT', 
            airport_columns['Region']:'TEXT',
            airport_columns['ImageURL']:'TEXT', 
                }