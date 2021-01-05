##############################################################################
#                Socio- Economic Indicators Portal                           #
##############################################################################
import pandas as pd
import requests
import json
from pandas.io.json import json_normalize
from urllib.request import urlretrieve as retrieve 
import re

# Function Name: getWBCountries
# Parameters: None 
# Return value: None
# Function description: Fetches the list of countries from the World bank website and outputs to an excel file for further processing. 

def getWBCountries():
    locations = requests.get("http://api.worldbank.org/v2/country?format=json&source=6&per_page=300")
    locationsJSON = locations.json()
    global location_df
    location_df = pd.DataFrame()
    # Parse through the response to see the location IDs and names
    locationList =[]
    for location in locationsJSON[1]:
        locationList.append([location["id"],location["name"]])
        location_df = pd.DataFrame(locationList,columns = ["ID","Country_Name"])
        location_df['Country_Upper'] = location_df['Country_Name'].str.upper()
    #print(location_df)
    # Download the list of countries in World Bank database to excel
    location_df.to_excel(r'C:\Users\preme\WBCountriesDF.xlsx')

# Function Name: getWBIndicators
# Parameters: None 
# Return value: None
# Function description: Fetches the list of indicators from the World bank website and outputs to an excel file for further processing. 

def getWBIndicators():
    # Get the list of indicator categories in World bank website
    wb_sources = requests.get("http://api.worldbank.org/v2/sources?per_page=100&format=json") 
    wb_sourcesjson = wb_sources.json()
    category_id_list =[]
    category_name_list =[]
    for item in wb_sourcesjson[1]:
        category_id_list.append(item["id"])
        category_name_list.append(item["name"])
    category_dict = dict(zip(category_id_list,category_name_list))
    indicator_category_df = pd.DataFrame(data = category_dict.items(), columns = ('category_ID', 'Category_Name'))
    ind_category_list = indicator_category_df['category_ID'].tolist()
    #print(indicator_category_df)
    
    # Get the list of indicators in World Bank website
    global indicators_df
    indicators_df = pd.DataFrame()
    for i in ind_category_list:
        indicators_req = requests.get("http://api.worldbank.org/v2/indicator?format=json&source="+str(i))
        indicatorsJSON = json.loads(indicators_req.content.decode('utf-8'))
        for j in indicatorsJSON[1]: 
            indicators_df= indicators_df.append(pd.io.json.json_normalize(j)[['id','name','sourceNote','source.id','source.value','sourceOrganization']])   
    indicators_df.reset_index(inplace = True)
    del indicators_df['index']
    indicators_df.columns = ['Indicator_ID', 'Indicator_Name','Indicator_Desc','Category_ID','Category_Name','Data_Source']
    indicators_df['Name_Upper'] = indicators_df['Indicator_Name'].str.upper()
    #print(indicators_df)   
    
    # Download the list of World Bank indicators to excel
    indicators_df.to_excel(r'C:\Users\preme\WBIndicatorsDF.xlsx')

# Function Name: getCountryInput
# Parameters: None 
# Return value: name_index - list of 3 digit country code, countries_entered - list of countries entered by the user
# Function description: Get the user input for a country for which socio economic indicators are required from World Bank site. 

def getCountryInput():
    i = 0
    while i != 1:
        Country_Input = input("Enter a country name: ").strip()
        Country_Input = Country_Input.title()
        #print(Country_Input)
        if Country_Input not in location_df['Country_Name'].values:
            print("You entered an incorrect country name. If you are unsure of the spelling, please enter first 3 characters")
            Country_Input_2 = input("Enter 3 characters of the country name: ").strip()
            country_list = location_df['Country_Upper'].values.tolist()
            #print(country_list)
            for item in country_list:
                r = re.findall(rf"\w*{Country_Input_2}\w*", item, re.IGNORECASE)
                if r:
                    print(item)
            print("Please select the correct country name from the above list")
        else:
            print('The country entered is '+Country_Input+'. The data for '+Country_Input+' is available in World Bank Database')
            i = 1
            Country_ID = location_df.loc[location_df.Country_Name == Country_Input,'ID'].tolist()[0]
            #Country_ID = location_df.loc[location_df['Country_Name'] == Country_Input,'ID'].iloc[0]
           
    name_index = []
    countries_entered = []
    name_index.append(Country_ID)
    countries_entered.append(Country_Input)
    return name_index, countries_entered 

# Function Name: getIndicatorInput
# Parameters: None 
# Return value: Indicator_ID_selected - list of indicator code, Indicator_Name- list of indicators entered by the user
# Function description: Get the user input for the indicators for which data is required from World Bank site. 

def getIndicatorInput():
    j = 0
    while j != 1:
        Indicator_Input = input("Enter an indicator name: ").strip()
        print(Indicator_Input)
        Indicator_Input= Indicator_Input.upper()
        indicators_user_sel_df = indicators_df.loc[indicators_df.Name_Upper.str.contains(rf"\w*{Indicator_Input}\w*"), :]
        Num_Indicators = len(indicators_user_sel_df)
        indicators_user_sel_df.reset_index(inplace = True)
        if Num_Indicators == 1:
            #print(indicators_user_sel_df[['Indicator_ID','Indicator_Name','Data_Source']])
            Indicator_ID_selected, Indicator_Name = indicators_user_sel_df[['Indicator_ID','Indicator_name']]
            j = 1
        elif Num_Indicators == 0:
            print('There is no indicator with the search word' +Indicator_Input+' in World bank database')
        else:
            print(f'Your search for "{Indicator_Input}" from World Bank database has {Num_Indicators} indicators. Which indicator would you like to check?')
            print('\n')
            print(indicators_user_sel_df[['Indicator_ID','Indicator_Name']])
            Indicator_Sno = int(input("Select an indicator from the above list (Please enter the Serial number): "))
            Indicator_ID_selected = indicators_user_sel_df.iloc[Indicator_Sno,1]
            Indicator_Name = indicators_user_sel_df.iloc[Indicator_Sno,2]
            j = 1
    return Indicator_ID_selected, Indicator_Name
        
# Function Name: getDateInput
# Parameters: None 
# Return value: date_input- the date range 
# Function description: Get the user input for the date range for which data is required from World Bank site. 

def getDateInput():
    date_option = int (input("""How many years of data would you like to see: 
        1. Last 10 years (2009:2018)
        2. Last 20 years (1999:2018)
        3. Last 50 years (1969:2019)
        4. Choose a range
        """))
    if date_option == 1:
        date_input = '2009:2018'
        return date_input
    elif date_option == 2:
        date_input = '1999:2018'
        return date_input
    elif date_option == 3:
        date_input = '1969:2018'
        return date_input
    elif date_option == 4:
        date_option_start = input("Enter starting year: ")
        date_option_end = input("Enter ending year: ")
        date_input = date_option_start + ':' + date_option_end
        return date_input

# Function Name: getData
# Parameters: countries - list of countries for which data is required, indicator - list of indicators
# Return value: data_df1 - the data from World bank site in data frame 
# Function description: Get the data from World bank site based on user input of country name, indicators and date. 

def getData(countries, indicator):
    # Make a list of countries 
    countrylist = []
    counter = 0
    for country in countries: 
        if counter == 0:
            countrylist.append(country)
            counter += 1
        else:
            countrylist.append(';')
            countrylist.append(country)
    countrylists = ''.join(countrylist)
    # Making the dataframe for the indicators 
    data_req = requests.get("http://api.worldbank.org/v2/country/"+countrylists+"/indicator/"+indicator+"?format=json&per_page=16000&date=1991:2019")
    data_parsed = json.loads(data_req.content.decode('utf-8'))
    if data_parsed[0].get('page') == 0:
        print("No records are available for this combination of indicator and country. Please try for different combination")
    else:
        data_df = pd.DataFrame()
        for i in data_parsed[1]:
            data_df= data_df.append(pd.io.json.json_normalize(i)[['country.value','date','value']])
    
    #print(data_df)
    data_df1 = data_df.pivot(index='date', columns='country.value', values='value')

    #print(data_df1)
    #print(data_df1.isnull().sum())
    # Download indicator data to Excel
    data_df1.to_excel(r'C:\Users\preme\IndicatorDF.xlsx')   
    return(data_df1)