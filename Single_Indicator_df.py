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

#Name of the function is single_indicator_df
# It takes country code and indicator number as a paramter 
# it returns a data frame with data on an indicator for a countries selected by the user
def single_indicator_df(countries, indicator_number):
    indicator_dict = {1: 'Sl.UEM.TOTL.ZS', 2 : 'NE.EXP.GNFS.CD', 3 : 'NY.GDP.PCAP.CD', 4 : 'SH.DYN.MORT', 5 : 'SE.PRM.ENRR', 6 : 'SP.DYN.LE00.IN', 7:'SP.POP.TOTL', 8:'BX.KLT.DINV.WD.GD.ZS', 9:'EG.ELC.ACCS.ZS', 10:'MORT_MATERNALNUM'}
    indicator = indicator_dict[indicator_number]
    
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
    if indicator_number < 10:    
        pop_req_2 = requests.get("http://api.worldbank.org/v2/country/"+countrylists+"/indicator/"+indicator+"?format=json&per_page=16000&date=2008:2017")
        pop_data_2 = json.loads(pop_req_2.content.decode('utf-8'))
        pop_data_df_2 = pd.DataFrame()
        for i in pop_data_2[1]:
            pop_data_df_2= pop_data_df_2.append(pd.io.json.json_normalize(i)[['country.value','date','value']])   
            pop_data_df2 = pop_data_df_2.pivot(index='date', columns='country.value', values='value')
    if indicator_number == 10:            
        pop_data_df2 = WHO_data(countries)
    # returning the dataframe 
    return pop_data_df2
