import numpy as np
import pandas as pd

#value_counts(frequency)
marks= pd.DataFrame([[100,50,70],[90,70,5],[50,60,70]],columns=['id','marks','package'])
marks.value_counts()#(s and d)
'''
ipl=pd.read_csv('ipl.csv')
ipl[~ipl['matchnumber'].str.isdigit()]['playerofmatch'].value_counts()


ipl['TossDescision'].value_counts().plot(kind='pie')

(ipl['team1'].value_counts() + ipl['team1'].value_counts()).sort_values(ascending=false)
'''

'''
#Sort values on missing items in column =missing values goes to bottom by default
students.sort_values('name', na_position ='first' , ascending =False,inplace = True) #inplace does perm changes 

students.sort(['year',title],ascending[True False])


#Rank(s)
batsman['batsman_rank']=batsman['batsman_run'].rank(ascending=False)


#Sort_index(s and d)
marks[marks.sort_index(ascending=False)]

#set_index(d)
batsman.set_index('batter',inplace=True)

#reset_index(s and d)
batsman.reset_index()

It converts series to dataframes

#Rename (d)
movies.rename(columns={'imdb':'imdff' , 'poter':'link},inplace = True)
movies.rename(index={'uri':'uri': 'bhim':'nim" })

#unique(s)
movies.unique()
no.of =len

ipl['season'].nunique() # does not count nan.    (s and d)


students['name'].isnull() -> checks if missing value (s and d)

notnull is reverse of it. (s and d)
students['name'].notnull()

remove mssining value
students['name'].dropna() => if single value missing whole column dropped. (s and d)

students.dropna(subset=['name','college']) #removes where name is missing. 
(   OR function)

#fillna(s and d)
students[name].fillna('unkown')
students['package'].fillna(students['pckage].mean())

#drop_duplicates (s and d )
temp=pd.series([1,2,3,1,3,1,2,34,5,6])
temp.drop_duplicates()

marks.drop_duplicates(keep='last')

#drop(s and d)
temp.drop(index=[0,6])
students.drop(columns=['batch','side'])


#apply
custom function

'''






