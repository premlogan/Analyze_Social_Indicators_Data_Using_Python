##############################################################################
#                Socio- Economic Indicators Portal                           #
##############################################################################
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from pandas.io.json import json_normalize

#Name of the function is single_country()
# It takes no parameter 
# It prompts the user to enter a name of the country 
# If the name is not in the specified list of countries function returns an error
# It then redirects the person to enter a correct country name 
# It return the name and index of the countries that are entered 
def single_country():
    countries_possible = {'Afghanistan':'AFG', 'Bhutan':'BTN', 'Bangladesh':'BGD', 'China':'CHN', 'Nepal':'NPL', 'India':'IND', 'Pakistan': 'PAK', 'Sri Lanka':'LKA', 'Myanmar':'MMR', 'Japan':'JPN'}     
    # Print the name of possible countries 
    print('Select a country from this list: ')
    for a in countries_possible.keys():
        print(a)
    name_index = []
    countries_entered = []
    # Prompt the user to enter the country name and give error if country not in the dictionary 
    name = input('Enter Country name here: ')
    if name.title() not in countries_possible.keys():
        name = input('Error: Not a valid Country Name. Want to try again? If yes, enter Yes, otherwise enter no: ')
        if name.title() == 'Yes':
            name1t = 1
            while len(name_index) < 1 and name1t != 'End':
                name1 = input('Enter Another Country Name if needed. Otherwise enter End: ')
                name1t = name1.title()
                if name1t in countries_possible.keys():
                    name_index.append(countries_possible[name1t])
                    countries_entered.append(name1t)
                else:
                    print('Error: Enter a valid country name')
        else:
            quit
    
    else:
        namet = name.title()
        countries_entered.append(namet)
        print('\nCountry entered:')
        for i in range(len(countries_entered)):
            print(countries_entered[i])
        name_index.append(countries_possible[namet])
    # return name_index and countrie_entered 
    return name_index, countries_entered

