import pandas as pd
import json
import requests
import math

def file_to_dataframe(file):
    # load file
    data = json.load(file)

    # Put data in data frame and drop irrelevant columns
    df = pd.DataFrame(data['data']).drop(['aliases', 'member_level', 'record_type', 'scores_overall_rank'], axis=1)
    print(df.iloc[0].type)
    

file_to_dataframe(open('./Data_json/overall_2011.json'))