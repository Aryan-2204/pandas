'''
#concatenation(vertically stack)
pd.concate([nov,dec],ignore_index=True)#for unique indexes

ALTERNATE
nov.append(dec,ignore_index=True) 


pd.concat([nov,dec],keys=['Nov','Dec'])
#multiindex Dataframe
multi.loc[('Dec',4)]


pd.concat([nov,dec],axis=1)



#JOIN
inner-join: (common things)
students.merge(regs,how='inner',on='student_id')

left-join:(common plus left table things)
courses.merge(regs,how='left',on='corse_id')

right-join:(common plus right table things)
students.merge(regs,how='right',on='student_id')

outer-join:
students.merge(regs,how='outer',on='student_id')


'''

'''
QUESTIONS
regs.merge(course,how='inner',on='course_id')['price'].sum()

Q.find month by month earning
aryn=pd.concat([nov,dec],keys=['Nov','Dec']).reset_index()
aryn.merge(courses,on='course_id').groupby('level_0)['price'].sum()

Q.
regs.merge(students,on='student_id').merge(courses,on='course_id')[['name','course_id','price']]

Q.
 regs.merge(courses,on='course_id').groupby('course_name')['price'].sum().plot(kind=bar)

Q.
common=np.intersect1d(nov['student_id'],dec['student_id'])
students[students['student_id'].isin(common)]

find course not got enrolment
np.setdiff(courses['course_id'],regs['course_id'])

students.merge(students,how='inner',left_on='partner',right_on='sdtudent_id')[['name_x' 'name_y']]

regs.merge(students,on='student_id').groupby(['student
_id' ,'name'])['name'].count().sort_values(ascending=False).head(3)

ALTERNATE MERGE
pd.merge(students,reg,how='inner',on='course_id')

IPL DATASET
Q1. Six isto match ratio
temp_df=delivery.merge(matches,left_on='match_id',right_on='id)
six_df=temp_df[temp_df['batsman_runs']== 6]

num_sixes =six_df.groupby('venue)['venue'].count()
num_matches=matches['venue'].value_counts()
(num_sixes/num_matches).sort_values(ascending=False).head(3)

Q2. Orange cap holder each season
temp_df.groupby(['season','batsman_runs']).rest_index().sort_values(batsman_runs ascending= False).drop_duplicates(subset=['season'],keep='first')


'''
