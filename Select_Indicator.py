##############################################################################
#                Socio- Economic Indicators Portal                           #
##############################################################################
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from pandas.io.json import json_normalize

#Function name is select indicator
# it has no parameter 
# it prompts the user to enter an indicator from a list 
# if the indicator is not in the list it directs the user to enter a correct indicator name 
# when the correct indicator name is entered it returns indicator number and the name of the indicator 
def select_indicator():
    # Print the names of the indicators 
    indicator_dict = {'1': 'Sl.UEM.TOTL.ZS', '2': 'NE.EXP.GNFS.CD', '3': 'NY.GDP.PCAP.CD', '4': 'SH.DYN.MORT', '5': 'SE.PRM.ENRR', '6': 'SP.DYN.LE00.IN', '7':'SP.POP.TOTL', '8':'BX.KLT.DINV.WD.GD.ZS', '9':'EG.ELC.ACCS.ZS', '10':'MORT_MATERNALNUM'}     
    print('Select an indicator from this list: ')
    indicator_list = ['Unemployment rate (in percentage)', 'Exports of goods and services (current US$)', 'GDP per capita (current US$)', 'Mortality rate, under-5 (per 1,000 live births)', 'School enrollment, primary (% gross)', 'Life expectancy at birth, total (years)', 'Country Population', 'Foreign direct investment, net inflows (% of GDP)', 'Access to electricity (% of population)', 'Maternal Mortality (yearly)']
    for a in range(len(indicator_list)):
        print('%d: %s' % (a+1, indicator_list[a]))
    # Prompt the user to select an indicator 
    indicator_index = []
    ind = input('Enter Indicator number here: ')
    # if the indicator number entered not in the specified list, print an erro 
    if ind not in indicator_dict.keys():
        name = input('Error: Not a valid Indicator Number. Want to try again? If yes, enter Yes, otherwise enter no: ')
        if name.title() == 'Yes':
            ind1 = 11
            # prompt for the second indicator 
            while len(indicator_index) < 1 and ind1 != '0':
                ind1 = input('Enter Another Indicator Number. Otherwise enter 0: ')
                if ind1 in indicator_dict.keys():
                    indicator_index.append(ind1)
                elif ind1 == '0':
                    continue
                else:
                    # print error if indicator not in the specified indicator list 
                    print('Error: Enter a valid indicator number')
    
    else:
        indicator_index.append(ind)
    indicator_number = int(''.join(indicator_index))
    # return the indicator number and name of the indicator 
    return indicator_number, indicator_list[indicator_number-1]


