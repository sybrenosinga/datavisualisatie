import pandas as pd
import json
import requests

# Get json data
file = requests.get('https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2018_limit0_369a9045a203e176392b9fb8f8c1cb2a.json').text
data = json.loads(file)

# Put data in data frame and drop irrelevant columns
df = pd.DataFrame(data['data']).drop(['apply_link', 'aliases', 'member_level', 'record_type', 'scores_overall_rank'], axis=1)

# Change Female:Male ratio to percentage Male
df = df.rename({'stats_female_male_ratio':'percentage_male'}, axis=1)
df['percentage_male'] = df['percentage_male'].apply(lambda val: int(val.split(' : ')[1]) if val is not None else val)


print(df)



########
# Random test prints

# print(df['percentage_male'])  # Print percentage male column
# print(df[df['percentage_male'].isnull()][['percentage_male', 'location', 'name']])  # print rows where 'percentage male' has no value
# print(df.groupby(['location'])['percentage_male'].mean().sort_values())  # print mean average of 'percentage male' per country sorted by value
