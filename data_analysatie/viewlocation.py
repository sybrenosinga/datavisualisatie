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

# kies land die je wilt bewonderen
country = df18['location'] == 'Japan' # verwissel hier land naar keuze

# verkrijg axis waarden met gekozen land
rank = df18[country]['rank_order']
studentstaff = df18[country]['stats_student_staff_ratio']
size = df18[country]['stats_number_students']
boiz = df18[country]['percentage_male']
preinternational = df18[country]['stats_pc_intl_students']
international = [i[:-1] for i in df18[country]['stats_pc_intl_students']]

# plot 1: rank vs student staff ratio
output_file("data_analysatie/viewlocation1.html")

f = figure()

# Axes
f.xaxis.axis_label="rank"
f.yaxis.axis_label="student staff ratio"

f.x_range=DataRange1d(start=0, end=1103)
f.y_range=DataRange1d(start=0, end=150)

# Plot the line
f.circle(rank, studentstaff)
show(f)

# plot 2: size university vs percentage man
output_file("data_analysatie/viewlocation2.html")
g = figure()

# Axes
g.xaxis.axis_label="number of students"
g.yaxis.axis_label="percentage man"

g.y_range=DataRange1d(start=0, end=100)

# Plot the line
g.circle(size, boiz)
show(g)

# plot 3: percentage international vs percentage man (omdat size handig met t bolletje zelf kan)
output_file("data_analysatie/viewlocation3.html")

h = figure()

# Axes
h.xaxis.axis_label="percentage international"
h.yaxis.axis_label="percentage man"

h.x_range=DataRange1d(start=0, end=50)
h.y_range=DataRange1d(start=0, end=100)

# Plot the line
h.circle(international, boiz)
show(h)
