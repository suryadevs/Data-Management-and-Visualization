# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
import pandas as pd
import numpy as np

income_groups = ['high_income_group', 'upper_middle_income_group', 'lower_middle_income_group', 'low_income_group']
# Creating income classes - Reference used: https://en.wikipedia.org/wiki/List_of_countries_by_GNI_(nominal)_per_capita
# high_income_group = Countries with incomeperperson > 6000
# upper_middle_income_group = 6000 > Countries with incomeperperson > 2200
# lower_middle_income_group = 2200 > Countries with incomeperperson > 600
# low_income_group = Countries with incomeperperson < 600
def get_economic_status(incomeperperson):
    high_limit = 6000
    upper_middle_limit = 2200
    lower_middle_limit = 600
    if incomeperperson > high_limit:
        return income_groups[0]
    elif incomeperperson < high_limit and incomeperperson > upper_middle_limit:
        return income_groups[1]
    elif incomeperperson < upper_middle_limit and incomeperperson > lower_middle_limit:
        return income_groups[2]
    elif incomeperperson < lower_middle_limit:
        return income_groups[3]
    else:
        return 'undefined'

orig_data = pd.read_csv('gapminder.csv', skipinitialspace=True)
# creating new dataframe with only the required variables from orig_data
data = orig_data[['incomeperperson', 'employrate', 'urbanrate', 'suicideper100th']].copy()
# some of the the data is missing in the codebook, removing those rows
data.dropna(inplace=True)
#adding new column economicstatus based on incomeperperson
data['economicstatus'] = [get_economic_status(x) for x in data['incomeperperson']]
print (len(data)) #number of observations for cleaner data (rows)
print (len(data.columns)) # number of variables for cleaner data (columns)

#counts and percentages (i.e. frequency distributions) for all income groups
print('\nCount of {} countries'.format(income_groups[0]))
count_high_income_countries = (data['economicstatus'] == income_groups[0]).sum()
print (count_high_income_countries)
print('Percentage of {} countries'.format(income_groups[0]))
percentage_high_income_countries = count_high_income_countries/len(data)
print (percentage_high_income_countries)

print('\nCount of {} countries'.format(income_groups[1]))
count_upper_middle_income_countries = (data['economicstatus'] == income_groups[1]).sum()
print (count_upper_middle_income_countries)
print('Percentage of {} countries'.format(income_groups[1]))
percentage_upper_middle_income_countries = count_upper_middle_income_countries/len(data)
print (percentage_upper_middle_income_countries)

print('\nCount of {} countries'.format(income_groups[2]))
count_lower_middle_income_countries = (data['economicstatus'] == income_groups[2]).sum()
print (count_lower_middle_income_countries)
print('Percentage of {} countries'.format(income_groups[2]))
percentage_lower_middle_income_countries = count_lower_middle_income_countries/len(data)
print (percentage_lower_middle_income_countries)

print('\nCount of {} countries'.format(income_groups[3]))
count_low_income_countries = (data['economicstatus'] == income_groups[3]).sum()
print (count_low_income_countries)
print('Percentage of {} countries'.format(income_groups[3]))
percentage_low_income_countries = count_low_income_countries/len(data)
print (percentage_low_income_countries)

