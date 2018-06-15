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

# give minimal student staff ratio per country
groupby_country = df18['stats_student_staff_ratio'].groupby(df18['location'])
min_student_staff_ratio = groupby_country.min()
print("MINIMAL STUDENT STAFF RATIO '18")
print(min_student_staff_ratio.sort_values().to_string())
print()

# ~try~ to make bar chart for min student staff ratio per country
countries = []
values = []
finalvalues = []

output_file('data_analysatie/locations.html')

for country, value in groupby_country:
    countries.append(str(country))

for value in min_student_staff_ratio.to_string().split('\n'):
    values.append(value)

for entry in values:
    entry = entry[-5:]
    if entry != 'ation':
        finalvalues.append(float(entry))

f = figure(x_range=countries, plot_height=50, title="studentstaffratio per country")

f.vbar(x=countries, top=finalvalues ,width=0.5)

f.xgrid.grid_line_color = 'yellow'
f.y_range.start = 0

# # N.B. show geeft geen bar chart (terwijl die dat wel zou moeten doen)
# show(f)

# # min student staff ratio '17
# groupby_country = df17['stats_student_staff_ratio'].groupby(df17['location'])
# min_student_staff_ratio = groupby_country.min()
# print("MINIMAL STUDENT STAFF RATIO '17")
# print(min_student_staff_ratio.sort_values().to_string())
# print()

# # min student staff ratio '16
# groupby_country = df16['stats_student_staff_ratio'].groupby(df16['location'])
# min_student_staff_ratio = groupby_country.min()
# print("MINIMAL STUDENT STAFF RATIO '16")
# print(min_student_staff_ratio.sort_values().to_string())
# print()
