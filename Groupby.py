
''' //here dataset is movie//
Aryan=movies.groupby('Genre')
Aryan.sum() // can apply more aggregate functions on groupby

//find the top 3 genres by total earning
movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3)

//find genre with highest imdb rating
movies.groupby('Genre')['IMDB'].mean().sort_values(ascending=False).head(3)

// most voted director
movies.groupby('Director')['Votes].sort_values(ascending=False).head()

// no of movies by actor
->movies['star1'].value_counts() //easyyy
movies.groupby('Star1')['Series'].count().sort_values(ascending=False).head()

len(movies.groupby('Genre'))

movies.groupby('Genre').size()

genres=movies.groupby('Genre')
genres.first()

genres.nth(x)

genres.get_group('Horror')

//object.group returns dictionary 

genres.describe()
//returns all info

genres.sample //returns random data
'''

'''
//passing dict 
genres,agg(
    {
        'Runtime' : 'mean',
        'IMDB : 'mean' ,
        'Gross ': 'sum'
        'Metascore' : 'min'
    }
)
//passing list
genres.agg (['min' 'max' 'mean'])

//combining both
genres,agg(
    {
        'Runtime' : ['mean','min' ]
        'IMDB :'mean' ,
        'Gross ': ['sum','max']
        'Metascore' : 'min'
    }
)

//looping for groups
df=p
for group,data in genres:
df=df.append(data[data['IMDB']== data['IMDB'].max())
df

//apply functions
->genre.apply(min) 

def foo(group):
return group['serial'].str.startswith('a').sum()
genre.apply(foo)


def ranking(group):
group['rankingg']= group['imdb'].rank(ascending=False)
return group
genre.apply(ranking)

duo = movies.groupby(['Director','Star1'])
duo.size()
duo.get_group('Amir khan' ,'Anmole')

duo['Gross'].sum().sort_values(ascending=False).head()

movies.groupby(['star1','genre'])['Metascore'].mean().reset_index().sort_values(ascending=false).head()

duo.agg(['min' 'max' 'mean'])



'''
'''
//questions
ipl.groupby('batsman')['runs'].sum().sort_values(ascending=False).head()


six=ipl[ipl['runs']==6]
six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head()

temp= ipl[ipl['over']>15]
temp = temp[(temp['runs] == 4) | (temp['runs] == 6)]
temp.groupby('batsman')['batsman'].count().sort_values(ascending=False).head()

temp = ipl[ipl['batsman']] == 'v-kohli']
temp.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head()
'''


