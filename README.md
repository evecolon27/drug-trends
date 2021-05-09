# drug-trends
Graphing marijuana use trends from 2014-2019

#Executive Summary:
In recent years, polcies towards marijuana use has grown to have
a mixture of perceptions and opinions.According to the National Institute on,
Drug Abuse, marijuana is a commonly used drug after alcohol and tobacco. Despite 
retaining its infamous drug classification, several of states in the United
States have legalized marijuana whether a specific amount or medical-use. The purpose
of this analysis is to study marijuana use trends among different age groups. 

#Instructions
1) Install Anaconda Jupyter
Download and Clone the directory from :
Run Script 1 (function.py)

#Input Data
Firstly, it is imperative to gather and clean up the data. Download the Excel files
from 2019-2017 National Survey On Drug Use And Health: Model-Based Prevalence Estimates. 
These will be in percentages. Download PDF files for 2013-2016 National Survey 
On Drug Use And Health: Model-Based Prevalence Estimates. 

https://www.samhsa.gov/data/nsduh/state-reports-NSDUH-2019
The above link is the general page to retrieve all the yearly reports of Prevalence Estimates.
https://www.samhsa.gov/data/report/2015-2016-nsduh-state-prevalence-estimates-pdf-tables-printing
The above link is an example of the type of PDF file that needs to be downloaded. 

#Instructions
Note: Covert PDF files to an Excel file beforehand. 

1) Import pandas, matplotlib.pyplot, and seaborn

2) Create two different functions to read each Excel file. Make sure to go through
each Excel to see how many rows do you have skip (National Survey on Drug Use and Health has written notes
within the Excel tables and so, it is import to see how many need to be skipped in the beginning)

3) The Excel files (2014-2015) that were converted from PDF will need to have their own function because you don't have to skip any rows, only rename the columns.

4) The Excel files (2016-2019) that do not require any convertion, rename the columns and multiply by 100 to make sure 
the values align with the other database after you join the excel files together. 

5) After renaming the columns in both datasets to be exactly the same, append both datasets. 

6) Create a specific table that has particular columns to start the graph plotting. 

7) Create a list of states you would like to use in the table. 

8) Start ploting them using seaborne. 

#Delieverables 
Python script called function.py and 3 pngs showing the plotted graphs 