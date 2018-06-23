import pandas

df18 = pandas.read_csv('./Data_csv/data_2018.csv')


# count unique courses, calculate increase over years and compare

df18.subjects_offered.count

# df18[1].apply(lambda x: x.count(12))
