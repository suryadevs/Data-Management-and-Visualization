# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np

income_groups = ['high_income', 'upper_middle_income', 'lower_middle_income', 'low_income']
income_limits = [6000, 2200, 600]
employrate_groups = ['75% - 100%', '50% - 75%', '25% - 50%', 'less than 25%']
employrate_limits = [75, 50, 25]
urbanrate_groups = ['75% - 100%', '50% - 75%', '25% - 50%', 'less than 25%']
urbanrate_limits = [75, 50, 25]
# Creating income classes - Reference used: https://en.wikipedia.org/wiki/List_of_countries_by_GNI_(nominal)_per_capita
# high_income_group = Countries with incomeperperson > 6000
# upper_middle_income_group = 6000 > Countries with incomeperperson > 2200
# lower_middle_income_group = 2200 > Countries with incomeperperson > 600
# low_income_group = Countries with incomeperperson < 600
def divide_in_groups(variable, limits, groups):
    # high_limit = 6000
    # upper_middle_limit = 2200
    # lower_middle_limit = 600
    if variable > limits[0]:
        return groups[0]
    elif variable < limits[0] and variable > limits[1]:
        return groups[1]
    elif variable < limits[1] and variable > limits[2]:
        return groups[2]
    elif variable < limits[2]:
        return groups[3]
    else:
        return 'undefined'

orig_data = pd.read_csv('gapminder.csv', skipinitialspace=True)
# creating new dataframe with only the required variables from orig_data
data = orig_data[['country', 'incomeperperson', 'employrate', 'urbanrate', 'suicideper100th']].copy()
# some of the the data is missing in the codebook, removing those rows
data.dropna(inplace=True)
#adding new column economicstatus based on incomeperperson
data['economicstatus'] = [divide_in_groups(x, income_limits, income_groups) for x in data['incomeperperson']]
data['employmentstatus'] = [divide_in_groups(x, employrate_limits, employrate_groups) for x in data['employrate']]
data['urbanisationstatus'] = [divide_in_groups(x, urbanrate_limits, urbanrate_groups) for x in data['urbanrate']]

print (len(data)) #number of observations for cleaner data (rows)
print (len(data.columns)) # number of variables for cleaner data (columns)


# %%
#counts and percentages (i.e. frequency distributions) for 3 variables
def print_freq_distribution(variable, groups):
    for i in range(4):
        count = (data[variable] == groups[i]).sum()
        percent = count/len(data)
        print('{:<20} Count: {:<5} Percentage: {:05.2f}'.format(groups[i], count, percent*100))

print('\nFrequency Distribution for incomeperperson')
print_freq_distribution('economicstatus', income_groups)
print('\nFrequency Distribution for employrate')
print_freq_distribution('employmentstatus', employrate_groups)
print('\nFrequency Distribution for urbanrate')
print_freq_distribution('urbanisationstatus', urbanrate_groups)


# %%
import seaborn
import matplotlib.pyplot as plt

# Univariate Quantitative Graphs
fig = plt.figure()
seaborn.distplot(data['incomeperperson'], kde=False)
plt.xlabel('Income Per Person')
plt.title('Quantitative Income Per Person distribution')

fig = plt.figure()
seaborn.distplot(data['employrate'], kde=False)
plt.xlabel('Employ Rate')
plt.title('Quantitative Employ Rate distribution')

fig = plt.figure()
seaborn.distplot(data['urbanrate'], kde=False)
plt.xlabel('Urban Rate')
plt.title('Quantitative Urban Rate distribution')


# %%
#Examining both their center and spread.
desc1 = data['incomeperperson'].describe()
print (desc1)
print('\n')
desc2 = data['employrate'].describe()
print (desc2)
print('\n')
desc3 = data['urbanrate'].describe()
print (desc3)
print('\n')


# %%
# Univariate Categorical Graphs
fig = plt.figure()
data['economicstatus'] = pd.Categorical(data['economicstatus'], income_groups[::-1])
seaborn.countplot(x='economicstatus', data = data)
plt.xlabel('Income Per Person')
plt.title('Categorical Income Per Person distribution')

fig = plt.figure()
data['employmentstatus'] = pd.Categorical(data['employmentstatus'], employrate_groups[::-1])
seaborn.countplot(x='employmentstatus', data = data)
plt.xlabel('Employ Rate')
plt.title('Categorical Employ Rate distribution')

fig = plt.figure()
data['urbanisationstatus'] = pd.Categorical(data['urbanisationstatus'], urbanrate_groups[::-1])
seaborn.countplot(x='urbanisationstatus', data = data)
plt.xlabel('Urban Rate')
plt.title('Categorical Urban Rate distribution')


# %%
#basic scatterplot:  Q->Q
fig = plt.figure()
scat2 = seaborn.regplot(x="incomeperperson", y="suicideper100th", data=data)
plt.xlabel('Income per Person')
plt.ylabel('Suicide Rate per 100 persons')
plt.title('Scatterplot for the Association Between Income per Person and Suicide Rate')

fig = plt.figure()
scat3 = seaborn.regplot(x="employrate", y="suicideper100th", data=data)
plt.xlabel('Employment Rate')
plt.ylabel('Suicide Rate per 100 persons')
plt.title('Scatterplot for the Association Between Employment Rate and Suicide Rate')

fig = plt.figure()
scat4 = seaborn.regplot(x="urbanrate", y="suicideper100th", data=data)
plt.xlabel('Urban Rate')
plt.ylabel('Suicide Rate per 100 persons')
plt.title('Scatterplot for the Association Between Urban Rate and Suicide Rate')


# %%
# bivariate bar graph C->Q
seaborn.catplot(x='economicstatus', y='suicideper100th', data=data, kind="bar", ci=None)
plt.xlabel('income group')
plt.ylabel('suicide rate')

# bivariate bar graph C->Q
seaborn.catplot(x='employmentstatus', y='suicideper100th', data=data, kind="bar", ci=None)
plt.xlabel('employ rate')
plt.ylabel('suicide rate')

# bivariate bar graph C->Q
seaborn.catplot(x='urbanisationstatus', y='suicideper100th', data=data, kind="bar", ci=None)
plt.xlabel('urban rate')
plt.ylabel('suicide rate')

