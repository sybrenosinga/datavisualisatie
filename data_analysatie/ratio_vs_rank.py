import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import DataRange1d

import pandas

# get tables of all years
df11 = pd.read_csv('./Data_csv/data_2011.csv')
df12 = pd.read_csv('./Data_csv/data_2012.csv')
df13 = pd.read_csv('./Data_csv/data_2013.csv')
df14 = pd.read_csv('./Data_csv/data_2014.csv')
df15 = pd.read_csv('./Data_csv/data_2015.csv')
df16 = pd.read_csv('./Data_csv/data_2016.csv')
df17 = pd.read_csv('./Data_csv/data_2017.csv')
df18 = pd.read_csv('./Data_csv/data_2018.csv')

# compare student staff ratio and overall rank
    # want meer leraren is wellicht beter onderwijs?

country = df18['location']
rank = df18['rank_order']
studentstaff = df18['stats_student_staff_ratio']

output_file("data_analysatie/ratio_vs_rank.html")

f = figure()

# Axes
f.xaxis.axis_label="rank"
f.yaxis.axis_label="student staff ratio"

f.y_range=DataRange1d(start=0, end=150)

# Plot the line
f.circle(rank, studentstaff)
show(f)
