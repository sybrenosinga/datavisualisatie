import pandas

def check_empty(df, row):
    # print(df[df['nid'] == row['nid']]['rank_order'].empty)
    if df[df['nid'] == row['nid']]['rank_order'].empty:
        return False
    return True
df_2011 = pandas.read_csv('./Data_csv/data_2011.csv')
df_2012 = pandas.read_csv('./Data_csv/data_2012.csv')
df_2013 = pandas.read_csv('./Data_csv/data_2013.csv')
df_2014 = pandas.read_csv('./Data_csv/data_2014.csv')
df_2015 = pandas.read_csv('./Data_csv/data_2015.csv')
df_2016 = pandas.read_csv('./Data_csv/data_2016.csv')
df_2017 = pandas.read_csv('./Data_csv/data_2017.csv')
df_2018 = pandas.read_csv('./Data_csv/data_2018.csv')

df_list = [df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018]

# for i, row in df_2011.iterrows():
#     if not df_2012[df_2012['nid'] == row['nid']]['rank_order'].empty:
#         print(df_2012[df_2012['nid'] == row['nid']]['rank_order'].iloc[0]


# print([1 if not df_2012[df_2012['nid'] == row['nid']]['rank_order'].empty else 99999 for i, row in df_2011.iterrows()])
    # print(row['rank_order'] - df_2012[df_2012['name'] == row['name']]['rank_order'])

df = pandas.DataFrame([[row['name'], row['rank_order'] - df_2012[df_2012['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(df_2012, row) else 9999,
                                    df_2012[df_2012['nid'] == row['nid']]['rank_order'].iloc[0] - df_2013[df_2013['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(df_2013, row) and check_empty(df_2012, row) else 9999,
                                    df_2013[df_2013['nid'] == row['nid']]['rank_order'].iloc[0] - df_2014[df_2014['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(df_2014, row) and check_empty(df_2013, row) else 9999,
                                    df_2014[df_2014['nid'] == row['nid']]['rank_order'].iloc[0] - df_2015[df_2015['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(df_2015, row) and check_empty(df_2014, row) else 9999,
                                    df_2015[df_2015['nid'] == row['nid']]['rank_order'].iloc[0] - df_2016[df_2016['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(df_2016, row) and check_empty(df_2015, row) else 9999,
                                    df_2016[df_2016['nid'] == row['nid']]['rank_order'].iloc[0] - df_2017[df_2017['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(df_2017, row) and check_empty(df_2016, row) else 9999,
                                    df_2017[df_2017['nid'] == row['nid']]['rank_order'].iloc[0] - df_2018[df_2018['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(df_2018, row) and check_empty(df_2017, row) else 9999]
                        for i, row in df_2011.iterrows()], columns=['name', '2011-2012', '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017', '2017-2018'])

print(df[df['name'] == "University of Amsterdam"])
