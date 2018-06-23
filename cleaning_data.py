import pandas as pd
import json
import requests
import math

# Get json data
# file = requests.get('https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2017_limit0_94aa8e595206a1cd1284e2808330a79c.json').text

def file_to_dataframe(file):
    # load file
    data = json.load(file)

    # Put data in data frame and drop irrelevant columns
    df = pd.DataFrame(data['data']).drop(['aliases', 'member_level', 'record_type', 'scores_overall_rank'], axis=1)
    if 'apply_link' in df:
        df = df.drop('apply_link', axis=1)

    for i, row in df.iterrows():
        df['rank_order'][i] = i + 1

    if 'stats_female_male_ratio' in df:
        # Change Female:Male ratio to percentage Male
        df = df.rename({'stats_female_male_ratio':'percentage_male'}, axis=1)
        df['percentage_male'] = df['percentage_male'].apply(lambda val: int(val.split(' : ')[1]) if val is not None else val)
        df['stats_number_students'] = df['stats_number_students'].apply(lambda val: int(val.replace(',', '')))

        # Create new column with number of male students
        df['male_students'] = ((df.percentage_male / 100) * df.stats_number_students).apply(lambda val: int(val) if not math.isnan(val) else val)

        # Calculate percentage male per country and put in new data frame
        sf = (df.groupby(['location'])['male_students'].sum() / df.groupby(['location'])['stats_number_students'].sum() * 100).apply(lambda val: int(val))
        mean_df = pd.DataFrame({'location': sf.index, 'mean': sf.values})

        # Replace missing values in the percentage male column with the respective country's percentage male value
        for i, row in df.iterrows():
            if math.isnan(row['percentage_male']):
                df['percentage_male'][i] = mean_df[mean_df['location'] == row['location']]['mean'].values[0]
    return df


file_to_dataframe(open('./Data_json/overall_2018.json')).to_csv('./Data_csv/data_2018.csv')
file_to_dataframe(open('./Data_json/overall_2017.json')).to_csv('./Data_csv/data_2017.csv')
file_to_dataframe(open('./Data_json/overall_2016.json')).to_csv('./Data_csv/data_2016.csv')
file_to_dataframe(open('./Data_json/overall_2015.json')).to_csv('./Data_csv/data_2015.csv')
file_to_dataframe(open('./Data_json/overall_2014.json')).to_csv('./Data_csv/data_2014.csv')
file_to_dataframe(open('./Data_json/overall_2013.json')).to_csv('./Data_csv/data_2013.csv')
file_to_dataframe(open('./Data_json/overall_2012.json')).to_csv('./Data_csv/data_2012.csv')
file_to_dataframe(open('./Data_json/overall_2011.json')).to_csv('./Data_csv/data_2011.csv')
