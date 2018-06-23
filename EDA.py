import pandas
from bokeh.plotting import figure, output_file, show


df18 = pandas.read_csv('./Data_csv/data_2018.csv').set_index('nid')
df17 = pandas.read_csv('./Data_csv/data_2017.csv').set_index('nid')
df16 = pandas.read_csv('./Data_csv/data_2016.csv').set_index('nid')
df15 = pandas.read_csv('./Data_csv/data_2015.csv').set_index('nid')
df14 = pandas.read_csv('./Data_csv/data_2014.csv').set_index('nid')
df13 = pandas.read_csv('./Data_csv/data_2013.csv').set_index('nid')
df12 = pandas.read_csv('./Data_csv/data_2012.csv').set_index('nid')
df11 = pandas.read_csv('./Data_csv/data_2011.csv').set_index('nid')

df_dict = {2011:df11,2012:df12,2013:df13,2014:df14,2015:df15,2016:df16,2017:df17,2018:df18}

# print(df18.loc[:,['name', 'rank_order', 'scores_industry_income']].set_index('name').sort_values(by='rank_order'))

# frames = [df11,df12,df13,df14,df15,df16,df17,df18]
# result = pandas.concat(frames).sort_index()
# print(result)

# df = df11.loc[:,['name', 'subject']]
# result = df.append(df13)
# print(result.sort_index())

# print(df18.columns.tolist)

df = pandas.DataFrame()
for key in df_dict:
    temp = df_dict[key].loc[:,['name', 'rank']].set_index('name')
    print(temp)
print(df)

# df = df18[df18.rank_order < 201].loc[:,['name', 'rank', 'subjects_offered']].set_index('name')
# df['course_count'] = df['subjects_offered'].str.split(",").str.len()
# print(df.sort_values(by=['course_count']))


# df = df18[df18.rank_order < 201].loc[:,['name', 'subjects_offered']].set_index('name')
# df['course_count'] = df['subjects_offered'].str.split(",").str.len()
# print(df.sort_values(by=['course_count']))


# def count_courses(df):
#     df_subjects = df.loc[:,['name','subjects_offered']].set_index('name')
#     return df_subjects

# print(count_courses(df11))
# def count_courses(series):
#     return len
# output to static HTML file


# def course_count(df_dict):
#     for key in df_dict:
#          = value for key
#         df_subjects = df.loc[:,['name','subjects_offered']].set_index('name')
#     return df_subjects

# print(course_count(df_dict))

frames = []
total_courses = df_dict.get(2011)

# count unique courses, calculate increase over years and compare
# place following in new dataframe, where index is uni name and colums are: total courses YEAR, total growth rate YEAR, new courses YEAR, removed courses YEAR, yearly growth rate YEAR
# 1 fetch courses starting year
# 2 store course list, count courses
# 3 fetch courses following year
# 4 count new courses, count removed courses, count growth rate
# 5 update course list, count courses, calculate increase
# 6 repeat from 3

# print(df18.columns.tolist())

# def check_id(df):
#     return df.loc[:,['name', 'nid']]

# frames = [check_id(df) for df in df_dict]
# result = pandas.concat(frames).drop_duplicates(subset='name').reset_index(drop=True)
# print(result.sort_values(by='nid'))


# def course_expansion(df_list):
#     for i in range(1, len(df_list)):


#     for i in range(1, len(df_list)):
#         df_current = df_list[i].loc[:,['name', 'nid']]
#         df_id = pd.concat(df_id, df_current)
#     print(df_id)

# check_id(df_list)

# def subjects_over_time():

# for i in range(len(df_list)):
#     print(df_list[i].loc[:,['subjects_offered']])

# df18[1].apply(lambda x: x.count(12))
