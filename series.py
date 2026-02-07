import numpy as np
import pandas as pd

country=['india','sri-lanka','usa','nepal']
print(pd.Series(country))

marks=[23,45,67,89,100]
subjects=['maths','eng','hindi','spanish','sci-fi']
print(pd.Series(marks,index=subjects,name='Aryan'))


#Series using Dict

marks={
    'maths' : 67
    ,'eng': 45,
    'sci':56
}
marks_series = pd.Series(marks,name='Aryan')
print(marks_series)

#size
print(marks_series.size)
#data type
print(marks_series.dtype)
#name
print(marks_series.name)
#is it unique
print(marks_series.is_unique)
#index
print(marks_series.index)
#values
print(marks_series.values)

#Series using read_csv (with one col)
#pd.read_csv('xxx.csv',squeeze=True)/ sequeeze turns it to series actually it was dataframe

#pd.read_csv('xxx.csv',index_col='match',squeeze=True)

''' 
1>xxx.head()-top values
2>xxxs.tail()-bottom values
3>xxx.sample()-sample values
4>xxx.value_counts()- descending 0rder values printed(frequency)
5>xxx.sort_values()- sorts in ascending order
[To sort in descending : xxx.sort_values(ascending=False).head(1)] :head(1)-> top value
6>xxx.sort_values(ascending=False).head(1)].values[0]
7>xxx.sort_values(inplace=True) #doess permanent changess
'''

'''
xxx.coumt() - does not include nan values
xxx.sum()-total sum
xxx.product()-total prod
xxx.mean()- mean
xxx.median()-median
xxx.mode()- mode
xxx.std()-standard deviation
xxx.var()-variance
xxx.max()-maximum /xxx.min()-minimum
xxx.describe()-describe everything mathematically
'''




'''
#Series Indexing
x=pd.Series([23,45,67,88,96,43])
print(x[1])
#no negative slicing in Series of pandas
#slicing
xxx[5:16]

#slicing
xxx[::3]
#fancy
xxx[[1,23,4,5]]

#label
xxx['label']
'''



#editing
marks_series[1]=100
print(marks_series[1])
marks_series['evs']=100 #if item does not exist it adds
print('evs')
  
marks_series[2:4]=[100,100]
print(marks_series)
#can be done by fancy indexing too



''' (here xxx is series name)
len(xxx)
type(xxx)-series
dir(xxx)-attributes and magic methods
sorted(xxx)
max(xxx)
list(marks_series)(type conversion)

#membership operations
'label' in xxx - returns true or flse (search on index)
    for values 
    'label' in xxx.values

for i in xxx :
print(i) works on values    

for i in xxx.index:
print(i) works on index   

#Arithmetic Operators
100 + xxx

#relational
xxx >= 50 -> returns boolean series
'''
'''
#boolean indexing
marks[marks >= 50].size #for how much
marks[marks==0].size

nums=marks.value_counts()
nums[nums >20]

'''

#PLOTTING OF GRAPH
print(marks.plot()) #plotting the graph
print(marks.value_counts().head(20).plot(kind = 'pie')) #pie representation

