import pandas
import math

df_2011 = pandas.read_csv('./Data_csv/data_2011.csv')
df_2012 = pandas.read_csv('./Data_csv/data_2012.csv')
df_2013 = pandas.read_csv('./Data_csv/data_2013.csv')
df_2014 = pandas.read_csv('./Data_csv/data_2014.csv')
df_2015 = pandas.read_csv('./Data_csv/data_2015.csv')
df_2016 = pandas.read_csv('./Data_csv/data_2016.csv')
df_2017 = pandas.read_csv('./Data_csv/data_2017.csv')
df_2018 = pandas.read_csv('./Data_csv/data_2018.csv')


def check_empty(variable, row, df1, df2=0):
    if not df2 == 0:
        if df1[df1['nid'] == row['nid']][variable].empty or df2[df2['nid'] == row['nid']][variable].empty:
            return False
    else:
        if df1[df1['nid'] == row['nid']][variable].empty:
            return False
    return True


def create_dataframe(variable):
    df = pandas.DataFrame([[row['name'], row['location'], row[variable] if check_empty(variable, row, df_2011) else math.nan,
                                    df_2012[df_2012['nid'] == row['nid']][variable].iloc[0] if check_empty(variable, row, df_2012) else math.nan,
                                    df_2013[df_2013['nid'] == row['nid']][variable].iloc[0] if check_empty(variable, row, df_2013) else math.nan,
                                    df_2014[df_2014['nid'] == row['nid']][variable].iloc[0] if check_empty(variable, row, df_2014) else math.nan,
                                    df_2015[df_2015['nid'] == row['nid']][variable].iloc[0] if check_empty(variable, row, df_2015) else math.nan,
                                    df_2016[df_2016['nid'] == row['nid']][variable].iloc[0] if check_empty(variable, row, df_2016) else math.nan,
                                    df_2017[df_2017['nid'] == row['nid']][variable].iloc[0] if check_empty(variable, row, df_2017) else math.nan,
                                    df_2018[df_2018['nid'] == row['nid']][variable].iloc[0] if check_empty(variable, row, df_2018) else math.nan]
                        for i, row in df_2011.iterrows()], columns=['name', 'location', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])
    return df


create_dataframe('rank_order').to_csv('./Data_csv/rank_order.csv')
create_dataframe('scores_citations_rank').to_csv('./Data_csv/citations_rank.csv')
create_dataframe('scores_industry_income_rank').to_csv('./Data_csv/industry_income_rank.csv')
create_dataframe('scores_international_outlook_rank').to_csv('./Data_csv/international_outlook_rank.csv')
create_dataframe('scores_research_rank').to_csv('./Data_csv/research_rank.csv')
create_dataframe('scores_teaching_rank').to_csv('./Data_csv/teaching_rank.csv')
