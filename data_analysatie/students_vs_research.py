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

# make table of number of students compared to research rank
    # want meer studenten is meer geschreven papers;
        # meer geschreven papers betekent meer research?

f = figure()

output_file("data_analysatie/students_vs_research.html")

researchrank = df18['scores_research_rank']
nrstudents = df18['stats_number_students']

# Axes
f.xaxis.axis_label="research rank"
f.yaxis.axis_label="students"

f.y_range=DataRange1d(start=0, end=300000)

# Plot the line
f.circle(researchrank, nrstudents)
show(f)
