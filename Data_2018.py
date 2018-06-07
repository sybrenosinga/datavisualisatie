import pandas as pd
import json
import requests

# Get json data
file = requests.get('https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2018_limit0_369a9045a203e176392b9fb8f8c1cb2a.json').text
data = json.loads(file)

# Put data in data frame and drop irrelevant columns
df = pd.DataFrame(data['data']).drop(['apply_link', 'aliases', 'member_level', 'record_type', 'scores_overall_rank'], axis = 1)

# check columns for missing data
# for colname in df.columns.tolist():
#     print('contains None: {}'.format(df[colname].apply(lambda val: str(val)).str.contains('None').any()))

print(df)