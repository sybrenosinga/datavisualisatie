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

# compare international students and international outlook
    # want meer international students, meer international outlook?

output_file("data_analysatie/international.html")

# amount of international students
pcintlstud = df18['stats_pc_intl_students']
pcintlstudnieuw = []
for entry in pcintlstud:
    entry = int(entry[:-1])
    pcintlstudnieuw.append(int(entry))

# values
intout = df18['scores_international_outlook_rank']
intstud = pcintlstudnieuw

f = figure()

# Axes
f.xaxis.axis_label="international outlook"
f.yaxis.axis_label="percentage international students"

f.x_range=DataRange1d(start=0, end=1000)

# Plot the line
f.circle(intout, intstud)
show(f)
