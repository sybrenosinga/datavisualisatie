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

output_file("outlook_vs_industry_income.html")

# values
outlook = df18['scores_international_outlook']
income = df18['scores_international_income']

# Create a figure
f = figure()

# Axes
f.xaxis.axis_label="score research"
f.yaxis.axis_label="score citations"


# Plot the line
f.circle(research, citations)
show(f)
