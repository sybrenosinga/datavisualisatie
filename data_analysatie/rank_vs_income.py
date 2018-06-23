import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import DataRange1d

import pandas

# get tables of all years
df11 = pd.read_csv('../Data_csv/data_2011.csv')
df12 = pd.read_csv('../Data_csv/data_2012.csv')
df13 = pd.read_csv('../Data_csv/data_2013.csv')
df14 = pd.read_csv('../Data_csv/data_2014.csv')
df15 = pd.read_csv('../Data_csv/data_2015.csv')
df16 = pd.read_csv('../Data_csv/data_2016.csv')
df17 = pd.read_csv('../Data_csv/data_2017.csv')
df18 = pd.read_csv('../Data_csv/data_2018.csv')

# compare international students and rank
    # want trekt een betere uni meer internationale mensen aan?

output_file("rank_vs_income.html")

# values
rank = df18['rank_order']
income = df18['scores_industry_income']

# Create a figure
f = figure()

# Axes
f.xaxis.axis_label="rank"
f.yaxis.axis_label="industry income"


# Plot the line
f.circle(rank, income)
show(f)
