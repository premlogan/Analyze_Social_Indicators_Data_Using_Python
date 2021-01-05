import pandas as pd
import requests
import json
from pandas.io.json import json_normalize
from urllib.request import urlretrieve as retrieve 
import re
import matplotlib.pyplot as plt
import seaborn as sns

def checkNA():
    indicator = 'SP.POP.TOTL'
    countries = ['IND']
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
    data_req = requests.get("http://api.worldbank.org/v2/country/ALL/indicator/"+indicator+"?format=json&per_page=16000&date=1969:2018")
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
        print(data_df1.isnull().sum())
        
        
        country_list = list(data_df1.columns.values)
        for country in country_list[:5]:
            sns.lineplot(data_df1.index.astype(int),data_df1[country].astype(int),label=str(country))
            #plot_1.set(xlabel="Years", ylabel = label)
        plt.show()