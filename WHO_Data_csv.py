##############################################################################
#                Socio- Economic Indicators Portal                           #
##############################################################################
import pandas as pd
from urllib.request import urlretrieve as retrieve

#take a list of countries 
# Access WHO data
# return the data after 2008 

def WHO_data(countries):
    # list of possible countries 
    countries_possible2 = {'AFG' : 'Afghanistan', 'BTN':'Bhutan', 'BGD':'Bangladesh', 'CHN' :'China', 'NPL':'Nepal', 'IND':'India', 'PAK':'Pakistan', 'LKA' : 'Sri Lanka', 'MMR' : 'Myanmar', 'JPN' :'Japan'}
    # retrieve the data from WHO 
    counter = 0
    for a in countries:
        URL = 'http://apps.who.int/gho/athena/api/GHO/MORT_MATERNALNUM.csv?filter=COUNTRY:'+ ''.join(a)
        retrieve(URL,'test.csv')
        data = pd.read_csv('test.csv')
        if counter == 0:
            data1 = data[["YEAR","COUNTRY","Numeric"]]
            data2 = data1.pivot(index='YEAR', columns='COUNTRY', values='Numeric')
            data2.rename(columns = {a: countries_possible2[a]}, inplace = True)
            
            counter += 1
        else:
            data1 = data[["YEAR","COUNTRY","Numeric"]]
            data3 = data1.pivot(index='YEAR', columns='COUNTRY', values='Numeric')
            data4 = pd.Series(data3[a])
            data2[a] = data4
            data2.rename(columns = {a: countries_possible2[a]}, inplace = True)
            
    data_final = data2.loc[2008:]
    # Return the data 
    return data_final

