##############################################################################
#                Socio- Economic Indicators Portal                           #
##############################################################################

# Importing all the packages and functions needed 


import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# Function name is country_profile1 
# it takes the name of the country as a paramter 
# it prints the country profile 
def country_profile1(country_name):
    # Retrieving the data 
    profile_page = requests.get("https://www.britannica.com/place/"+ ''.join(country_name).title())
    profile_page.status_code
    # Parsing the data 
    profile_soup = BeautifulSoup(profile_page.content,'html.parser')
    profile_intro = profile_soup.find(class_="grid-sm")
    Country_Profile =[]
    for para in profile_intro.find_all('p'):
        Country_Profile.append(para.text)
    # Parsing the country profile 
    print(Country_Profile[0])
    




# Function name is country_profile2
# it takes the name of the country as a paramter 
# it prints area, languages spoken, location, income group of the country.  
def country_profile2(country):    
    #Getting the data 
    headers = {"Content-Type": "application/json"}    
    url = "http://apps.who.int/gho/athena/api/GHO/WHOSIS_000001.json?filter=COUNTRY:" + ''.join(country[0])
    response = requests.get(url, headers = headers)    
    # Checking for response and organinzing the data 
    if response.status_code == 200:        
        data = json.loads(response.content.decode("utf-8"))
        y = pd.io.json.json_normalize(data['dimension'])
        z = y["code"]
        e = pd.DataFrame(z[4])
        country_name = e['display'].loc[0]
        f = pd.DataFrame(e['attr'].loc[0])
        fl = list(f["category"])
        g = f.rename(index = {i:fl[i] for i in range(len(fl))})
        g.drop('category', axis = 1, inplace = True)
        region = g.loc['WHO_REGION']['value']
        land_area = int(g.loc['LAND_AREA_KMSQ_2012']['value'].replace(',',''))
        income_group = g.loc['WORLD_BANK_INCOME_GROUP']['value']
        
        # printing the returned data 
        print('Land Area of %s in KM Square: %d' % (country_name, land_area))
        print('Languages spoken in %s: %s' % (country_name, g.loc['LANGUAGES_EN_2012']['value']))
        print('%s is located in Region: %s' % (country_name, region))
        print('According to World Bank, %s comes in the Income Group: %s' % (country_name, income_group))
        print('--------------------------------------------------------------------------------------')
    return()
    