import numpy as np
import pandas as pd

student_data=[
    [1100,2000],
    [4000,500],
    [2000,400]
]
print(pd.DataFrame(student_data,columns=['package','rupees']))


dict={ 'id':[100,200,],
      'gb':[500,5500]      }
print(pd.DataFrame(dict))

#pd.read_csv('movies.csv')

#--------------------------------------------------#
'''
SOME FUNCTIONS

#shape
dataframe.shape

#dtypes
dataframe.dtypes

#index
dataframe.index

#columns
dataframe.columns

#values
dataframe.values

#top data (head)
dataframe.head()

bottom data(tail)
dataframe.tail()

#random data
dataframe.sample

#info
datframe.info()

#describe
dataframe.describe() #gives numerical column data of the table 

#isnull
dataframe.isnull().sum()


#duplicated
dataframe.duplicated()

#rename
dataframe.rename(columns={'old value':'new value'})

MATHS FUNCTION
#sum
dataframe.sum() [provide axis to do row wise sum

#mean
dataframe.mean()

#min/max
dataframe.max/min()

#median
dataframe.median()

#var
dataframe.var()

#SINGLE COL
dataframe['column name']

#SET_INDEX : TO SET A COL TO INDEX


#HOW TO FETCH ROWS
iloc- searches using index position
loc- searches using index label

dataframe.iloc[0:5]
dataframe.iloc[0:3,0:3]

Through fancy indexing
dataframe.iloc[[1,2,3]]

BY LOC 
DATAFRAME.LOC['COLUMN NAME']
dataframee.loc[0:2,'column name':'column name']

----------------------------------------------------
ipl[ipl['SuperOver']== 'Y'].shape[0]

ipl[(ipl['city']=='Kolkata') & (ipl['Winning Team]='csk')].shape[0]

apply(custom function)
-----------------------------------------------------

TO ADDD NEW COLUMN
dataframe['column new']='value'

FROM EXISTING COLUMN
dataframe['new column']=dataframe['column existing'].str.split('|').apply(lamda x : x[0])

--------------------------------------------------
IMPORTANTY FUNCTIONSS








'''