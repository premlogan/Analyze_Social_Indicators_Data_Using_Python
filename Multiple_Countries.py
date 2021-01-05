##############################################################################
#                Socio- Economic Indicators Portal                           #
##############################################################################
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from pandas.io.json import json_normalize

#Function name is multiple_countries()
# it takes no parameter 
#It prompts the user to enter the name of a country  
# It compares the name of the country to the names of the country in the dictionary
# if the name of the country is not present in the list it returns the  error message
# Error message and directs the user to enter a correct country name 
# It enables user to enter names of the countries sequentially 
# if the names of the countries are present in the list, it returns index and list of countries entered  

def multiple_countries():
    # Present the names of the countries present 
    countries_possible = {'Afghanistan':'AFG', 'Bhutan':'BTN', 'Bangladesh':'BGD', 'China':'CHN', 'Nepal':'NPL', 'India':'IND', 'Pakistan': 'PAK', 'Sri Lanka':'LKA', 'Myanmar':'MMR', 'Japan':'JPN'}     
    print('Select a country (or countries) from this list: ')
    for a in countries_possible.keys():
        print(a)
        
    name_index = []    
    countries_entered = []
    # Prompt the user to enter the name of the coutry and give error if the name is not correct 
    name = input('Enter Country name here: ')
    # Check if the name in possible countries  give error message and prompt to enter another country 
    if name.title() not in countries_possible.keys():
        name = input('Error: Not a valid Country Name. Want to try again? If yes, enter Yes, otherwise enter no: ')
        # if user enters yes then prompt to enter the name of the country 
        if name.title() == 'Yes':
            name1 = input('Enter Another Country Name. Enter End to end program: ')
            name1t = name1.title()
            while name1t != 'End':
                # if the country is already entered 
                if name1t in countries_possible.keys():
                    if name1t not in countries_entered:
                        name_index.append(countries_possible[name1t])
                        countries_entered.append(name1t)
                        print('\nCountries already entered: \n')
                        for i in range(len(countries_entered)):
                            print(countries_entered[i])
                    else:
                        print('Error: country altered picked')
                        print('\nCountries already entered:\n')
                        for i in range(len(countries_entered)):
                            print(countries_entered[i])
                else:
                    print('Error: Enter a valid country name')
                    print('\nCountries already entered:\n')
                    for i in range(len(countries_entered)):
                        print(countries_entered[i])
                # Prompt the user again 
                name1 = input('Enter Another Country Name if needed. Otherwise enter End: ')
                name1t = name1.title()
    # if name in the list of specified countries 
    else:
        namet = name.title()
        countries_entered.append(namet)
        print('\nCountries already entered:\n')
        for i in range(len(countries_entered)):
            print(countries_entered[i])
        name_index.append(countries_possible[namet])
        name1 = input('Enter Another Country Name if needed. Otherwise enter End: ')
        name1t = name1.title()
        while name1t != 'End':
            if name1t in countries_possible.keys():
                if name1t not in countries_entered:
                    name_index.append(countries_possible[name1t])
                    countries_entered.append(name1t)
                    print('\nCountries already entered: \n')
                    for i in range(len(countries_entered)):
                        print(countries_entered[i])
                else:
                    print('Error: country altered picked')
                    print('\nCountries already entered:\n')
                    for i in range(len(countries_entered)):
                        print(countries_entered[i])
            else:
                print('Error: Enter a valid country name')
                print('\nCountries already entered:\n')
                for i in range(len(countries_entered)):
                    print(countries_entered[i])
            name1 = input('Enter Another Country Name is needed: ')
            name1t = name1.title()    
    # return name and index of the country that is entered 
    return name_index, countries_entered

