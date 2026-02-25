import numpy as np
import pandas as pd
#MULTIINDEX SERIES
#from tuples
index=[('cse',2019),('cse',2018),('ece',2030)]
multi=multiindex=pd.MultiIndex.from_tuples(index)
print(multi)
print(multi.levels[0])
#from product
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