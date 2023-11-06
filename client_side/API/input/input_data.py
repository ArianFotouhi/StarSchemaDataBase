from schema_metadata_cl import (user_columns, lounge_columns, tx_columns,
                                        country_columns, event_columns,amenity_columns, 

                                        airport_columns)
import pandas as pd

# user_id = 'user4'
# lounge_id = 'item4'
# transaction_id ='trans4'


user_data = {
            # user_columns['UserID']: user_id,
            user_columns['Email']: 'user1@example.com',
            user_columns['Password']: 'password1',
            user_columns['Username']: 'username1',
            user_columns['FirstName']: 'Ed',
            user_columns['LastName']: 'Jackson',
            user_columns['Tel']: '1234567890',
            user_columns['CreationDateTime']: '22-10-2023 10:55:11',
            user_columns['UserStatus']: 'Active',
            user_columns['LastUpdate']: '28-10-2023 14:15:10',
            }

lounge_data = {
            # lounge_columns['LoungeID']: lounge_id, 
            lounge_columns['Name']: 'YYZ int',
            lounge_columns['Country']:'Canada',
            lounge_columns['Coordinates']: '49.68 -79.61',
            lounge_columns['AirportID']: 'YYZ',

            lounge_columns['Description']:'international lounge of Toronto Airport',
            lounge_columns['TimeZone']:'-4', 
            lounge_columns['LoungeType']:'Departure Business Class',
            lounge_columns['LoungeCapacityStatus']:'Available',
            lounge_columns['AccessRequirements']:'Open to everyone',
            lounge_columns['OperatingHours']:'9:00 - 23:00',
            lounge_columns['Amenities']:'1,4,2,5,7',
            lounge_columns['Events']:'1,2',
            lounge_columns['AccessibilityFeatures']:'Wheelchair-accessible',
            lounge_columns['Capacity']:50,
            lounge_columns['EntryFee']:39.99,
            lounge_columns['Email']:'lounge_yyz_int@yyz.com',
            lounge_columns['Tel']:'+16471238899',
            lounge_columns['WebsiteURL']:'a@abc.com',
            lounge_columns['SecurityInfo']:'Baggage Checking',
            lounge_columns['Reservation']:'required',
            lounge_columns['ActivityStatus']:'Active',
            lounge_columns['LastUpdate']:'15-02-2023 10:00:04',
            lounge_columns['ImageURL']:'https://example.com',
            lounge_columns['SocialMediaLink']:'https://facebook.com/lounge',
            lounge_columns['Owner']:'YYZ',
            lounge_columns['OnSiteTransportation']:'Shuttle Service',
            }


tx_data = {
            # tx_columns['TxID']: transaction_id,
            tx_columns['UserID']: 1, 
            tx_columns['LoungeID']: 1,
            tx_columns['Status']: 'Successful',
            tx_columns['TimeStamp']: '30-10-2023 08:15:15',
            }


country_data = {
            country_columns['CountryName']: 'Canada',
            country_columns['Currency']: 'CAD', 
            country_columns['Coordinates']: '62.22, -105.38',
            country_columns['Language']: 'English/French',
            country_columns['TelCode']: '+1',
            country_columns['FlagImageURL']: 'https://example.com',
            country_columns['TimeStamp']: '30-10-2023 08:15:15',
            }


event_data = {
            # event_columns['EventID']:'1234512345', 
            event_columns['EventOwner']:'YYZ int lounge', 
            event_columns['EventName']:'Canada Day',
            event_columns['EventPartners']:'YUL airport', 
            event_columns['EventDuration']:'90min', 
            event_columns['EventDescription']:'Special meals for Canada Day',
            event_columns['Event_DateTime']:'01-07-2024 10:00:00', 
            event_columns['LastUpdate']:'30-10-2023 12:11:11'
            }

amenity_data = {
            # amenity_columns['AmenityID']:'987654321', 
            amenity_columns['AmenityStatus']:'Active', 
            amenity_columns['AmenityName']:'Hot Meal',
            amenity_columns['ImageURL']:'https://exampleurl.com',  
            amenity_columns['LastUpdate']:'15-10-2023 18:30:04'        
            }

airport_data = {
            airport_columns['IATACode']:'YYZ', 
            airport_columns['AirportName']:'Toronto Pearson International Airport', 
            airport_columns['Country']:'Canada',
            airport_columns['City']:'Toronto',  
            airport_columns['Coordinates']:'49.68, -79.60', 
            airport_columns['Region']:'North America',
            airport_columns['ImageURL']:'https://example.com', 
            }

def data_csv_reader(file_name='input/input.xlsx'):

    # Replace 'your_excel_file.xlsx' with the actual file path of your Excel file
    excel_file = file_name

    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file)

    # Convert the DataFrame into a list of dictionaries
    data_list = df.to_dict(orient='records')
    return data_list