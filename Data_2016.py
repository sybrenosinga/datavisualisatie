import pandas as pd
import json
import requests
import math

# Get json data
file = requests.get('https://www.timeshighereducation.com//sites//default//files//the_data_rankings//world_university_rankings_2016_limit0_a38b8fe86b742996f9ea3df4b4ca09f3.json').text
data = json.loads(file)

# Put data in data frame and drop irrelevant columns
df = pd.DataFrame(data['data']).drop(['aliases', 'member_level', 'record_type', 'scores_overall_rank'], axis=1)

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

print(df)

print(df.columns.tolist())
