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

output_file("research_vs_citations.html")

# amount of international students
pcintlstud = df18['stats_pc_intl_students']
pcintlstudnieuw = []
for entry in pcintlstud:
    entry = int(entry[:-1])
    pcintlstudnieuw.append(int(entry))

# values
outlook = df18['scores_international_outlook']
intstud = pcintlstudnieuw

# Create a figure
f = figure()

# Axes
f.xaxis.axis_label="score international outlook"
f.yaxis.axis_label="percentage international students"

# Plot the line
f.circle(outlook, intstud)
show(f)
