import numpy as np
import pandas as pd

print('numpy:', np.__version__)
print(pd.__version__)

bikes = pd.read_csv('D:/IOD/Data/Datasets 1/bikeshare.csv')
print(bikes.head())


#from pandas import ExcelFile  # why we need this one? the code didn't run this one
#df = pd.read_excel('D:/IOD/Data/Datasets 1/Iris.xlsx', sheet_name='Data')
#print(df)
#
#df_web = pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.csv')
#print(df_web.head())
#
#url = 'https://www.ccra.com/airport-codes/'
#df_url = pd.read_html(url)
#print(df_url)
#
#url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json'
#df_json= pd.read_json(url, orient = 'columns')
#df.head()

