# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:59:26 2021

@author: evesp
"""
#This file is meant to clean up all the excel files of National Survey Drug Use
#First, I used file 2019 to make sure we can drop and skip certain rows and rename the index_column

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


marijuana_2019 = pd.read_excel('2019NSDUHsaeExcelTabs.xlsx', 
                            sheet_name='Table 2', 
                            skiprows=4, 
                            index_col="State")
regions = ["Northeast", "Midwest", "South", "West", "Total U.S."]
marijuana_2019 = marijuana_2019.drop("Order", axis=1)
marijuana_2019 = marijuana_2019.drop(regions,axis=0)
#%%
def excel_read(file1):
    df1 = pd.read_excel(file1,index_col="State")
    df2 = df1.drop(regions, axis=0)
    return df2

marijuana_2014 = excel_read("NSDUHsaePercents2014.xlsx")
marijuana_2015 = excel_read("NSDUHsaePercents2015.xlsx")

#%%
mj_1415 = {'2014': marijuana_2014, '2015': marijuana_2015}

mj_t_1415 = pd.concat(mj_1415)

new_rows = mj_t_1415.drop(['12+\n(95% Confidence Interval)','12-17\n(95% Confidence Interval)', '18-25\n(95% Confidence Interval)', '26+\n(95% Confidence Interval)', '18+\n(95% Confidence Interval)'],axis=1)

new_rows.columns = [c.replace('\n(Estimate)', '') for c in new_rows.columns]

varnames = {'12+ ': '12+', '12-17 ': '12-17', '18-25 ': '18-25', '26+ ': '26+', '18+ ': '18+'}
new_1415 = new_rows.rename(varnames, axis=1)

#%%
def excel_read2(file1, sheet1):
    df1 = pd.read_excel(file1, sheet1,skiprows=4, index_col="State")
    df2 = df1.drop("Order", axis=1)
    df2 = df2.drop(regions, axis=0)
    return df2

marijuana_2016 = excel_read2('NSDUHsaeExcelTabs2016.xlsx', sheet1="Table 2")
marijuana_2017 = excel_read2("NSDUHsaeExcelTabs2017.xlsx", sheet1="Table 2")
marijuana_2018 = excel_read2("NSDUHsaeExcelTabs2018.xlsx", sheet1="Table 2")

#%%
mj_trends = {'2016': marijuana_2016, 
             '2017': marijuana_2017,
             '2018': marijuana_2018,
             '2019': marijuana_2019}

mj_trends_c = pd.concat(mj_trends)

mj_trends_c.columns = [c.replace('\nEstimate', '') for c in mj_trends_c.columns]
mj_trends_c.columns = [c.replace('\n95% CI (Upper)', ' CI U') for c in mj_trends_c.columns]
mj_trends_c.columns = [c.replace('\n95% CI (Lower)', ' CI L') for c in mj_trends_c.columns]

new_rows2 = mj_trends_c.drop(['12 or Older CI L', '12 or Older CI U', '12-17 CI L', '12-17 CI U', '18-25 CI L', '18-25 CI U', '26 or Older CI L', '26 or Older CI U','18 or Older CI L', '18 or Older CI U'], axis=1)

print(new_rows2)

varnames2 = {'12 or Older': '12+', '26 or Older': '26+', '18 or Older': '18+'}
mj_trends_1619 = new_rows2.rename(varnames2, axis=1)
mj_trends_1619 = mj_trends_1619*100
print(mj_trends_1619)

#%%
#Append both datasets now that they have the same column names and percentage values

total_mj = new_1415.append(mj_trends_1619)

#%%
#Creating specific table consisting of particular columns
#Setting index of the by_age table and then renaming the index to year
by_age = total_mj[['12-17','18-25','26+']]
mj_db = by_age.reset_index()
mj_db = mj_db.rename({'level_0':'year'}, axis=1)

tax_state = ['California', 'Washington', 'Oregon', 'Massachusetts', 'New Jersey']
selected = mj_db[ mj_db['State'].isin(tax_state) ]

#%%
fig, ax1 = plt.subplots(dpi=300)
fig.suptitle("Marijuana Usage from 2014 to 2019")
sns.lineplot(data=selected, x='year', y='12-17',  hue='State', ax=ax1)
ax1.set_xlabel("Estimate of Ages: 12-17")
ax1.set_ylabel("Percentage of Marijuana Usage")
fig.tight_layout()
fig.savefig("Trends of Marijuana.png")

#%%
fig, ax1 = plt.subplots(dpi=300)
fig.suptitle("Marijuana Usage from 2014 to 2019")
sns.lineplot(data=selected, x='year', y='18-25', hue='State', ax=ax1)
ax1.set_xlabel("Estimate of Ages: 18-25")
ax1.set_ylabel("Percentage of Marijuana Usage")
fig.tight_layout()
fig.savefig("Trends of Marijuana.png")

#%%
fig, ax1 = plt.subplots(dpi=300)
fig.suptitle("Marijuana Usage from 2014 to 2019")
sns.lineplot(data=selected, x='year', y='26+', hue='State', ax=ax1)
ax1.set_xlabel("Estimate of Ages: 26+")
ax1.set_ylabel("Percentage of Marijuana Usage")
fig.tight_layout()
fig.savefig("Trends of Marijuana.png")
#%%


