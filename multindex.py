import numpy as np
import pandas as pd
#MULTIINDEX SERIES
#from tuples
index=[('cse',2019),('cse',2018),('ece',2030)]
multi=multiindex=pd.MultiIndex.from_tuples(index)
print(multi)
print(multi.levels[0])
#from product (cartesian product)
prod=pd.MultiIndex.from_product([('cse',2019),('cse',2018),('ece',2030)])
print(prod)

a=(pd.Series([1,2,3],index=multi))
print(a['cse'])

#bto create it in dataframe
#print(a.unstack())
# print(a.stack()) to revert back

#MULTIINDEX DATAFRAME

send= pd.DataFrame(
    [
        [1,2],
        [1,2],
        [4,2],
    ],
    index= multi,
    columns=['avg_package','students']
)
print(send)

branch=pd.DataFrame(
    [
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
    ],
    index=[2019,2020,2021,2022],
    columns=pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)
print(branch)

'''stack() makes inner column into row and unstack makes inner row into column '''

print(branch.head())
print(branch.shape)
print(branch.info())
print(branch.duplicated())
#rows-> print(branch.loc[('cse',2019):('cse,2020'):2])

print(branch.iloc[0:4:2])

print(branch['delhi']['students'])

print(branch.iloc[:,1:3])

print(branch.iloc[[0,2],[1,2]]) 
# 0 and 4 row and 1 and 2 column will be extracted by fancy indexing which we did just now

print(branch.sort_index(ascending=False))


print(branch.sort_index(ascending=[False,True]))

print(branch.sort_index(level=1,ascending=False))


print(branch.transpose())

#print(branch.swaplevel()) axis=1 for columns here


'''
wide format-singli row for data points
long- many rows
'''
mind=pd.DataFrame(
    {
        'cse':[120]
    }
).melt()
print(mind)

mind2=pd.DataFrame(
    {
        'cse':[120],
        'ece':[200],
        'mech':[123]
    }
).melt(var_name='branch',value_name='students')
print(mind2)

mind3=pd.DataFrame({
    'branch':['cse','ece'],
    '2020':[120,34],
    '2021':[10,304],
    '2022':[1200,0],
    
}
).melt(id_vars =['branch'],var_name='year',value_name='students')
print(mind3)