##############################################################################
#                Socio- Economic Indicators Portal                           #
##############################################################################


# Importing all the packages and functions needed 

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from pandas.io.json import json_normalize
from WHO_Data_csv import WHO_data


#Name of the function is two_indicator_df
#Parameters are name of the country, indicator 1 and 2 

# returns data to help in plotting 
def two_indicator_df(countries, indicator_number1, indicator_number2):
    
        # Dictionary of possible indicators and their codes 
    indicator_dict = {1: 'Sl.UEM.TOTL.ZS', 2 : 'NE.EXP.GNFS.CD', 3 : 'NY.GDP.PCAP.CD', 4 : 'SH.DYN.MORT', 5 : 'SE.PRM.ENRR', 6 : 'SP.DYN.LE00.IN', 7:'SP.POP.TOTL', 8:'BX.KLT.DINV.WD.GD.ZS', 9:'EG.ELC.ACCS.ZS', 10:'MORT_MATERNALNUM'}
    indicator1 = indicator_dict[indicator_number1]
    indicator2 = indicator_dict[indicator_number2]
    # Making list of countries 
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
    # Retrieving the data for each indicator entered 
    if indicator_number1 < 10:    
        pop_req_2 = requests.get("http://api.worldbank.org/v2/country/"+countrylists+"/indicator/"+indicator1+"?format=json&per_page=16000&date=2008:2017")
        pop_data_2 = json.loads(pop_req_2.content.decode('utf-8'))
        pop_data_df_2 = pd.DataFrame()
        for i in pop_data_2[1]:
            pop_data_df_2= pop_data_df_2.append(pd.io.json.json_normalize(i)[['country.value','date','value']])
            
        pop_data_df2 = pop_data_df_2.pivot(index='date', columns='country.value', values='value')
    if indicator_number1 == 10:
        pop_data_df3 = WHO_data(countries)
        
    if indicator_number2 < 10:    
        pop_req_3 = requests.get("http://api.worldbank.org/v2/country/"+countrylists+"/indicator/"+indicator2+"?format=json&per_page=16000&date=2008:2017")
        pop_data_3 = json.loads(pop_req_3.content.decode('utf-8'))
        pop_data_df_3 = pd.DataFrame()
        for i in pop_data_3[1]:
            pop_data_df_3= pop_data_df_3.append(pd.io.json.json_normalize(i)[['country.value','date','value']])
            
        pop_data_df3 = pop_data_df_3.pivot(index='date', columns='country.value', values='value')
    
    if indicator_number2 == 10:
        pop_data_df3 = WHO_data(countries)
    # returning the data 
    return pop_data_df2, pop_data_df3

two_indicator_df(['PAK'], 1, 2)

