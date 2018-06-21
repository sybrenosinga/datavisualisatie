# zorgen dat je  op land kan klikken
# zorgen dat percentages goed zijn

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

# get table of all universities per country
alles = pd.read_csv('./Data_csv/all_universities.csv')

#  landen en unis in de top 1000
hoi = df18[df18.location != 'Northern Cyprus']
top = hoi['location'].value_counts()

# print(hoi)

# landen en alle unis, met de landen in de zelfde volgorde als top
all_unis = []
some_unis = []
# print(hoi['location'].unique())
for i in hoi['location'].unique():
    # all unis
    koelheid = alles['countries'] == i
    uni = alles[koelheid]
    if i == 'United States':
        all_unis.append(3281)
    else:
        for j in uni['universities']:
            all_unis.append(j)

    # some unis
    yoyo = hoi['location']== i
    lkj = yoyo.value_counts()
    some_unis.append(lkj[True])


# definieer voor numpy
array_all_unis = np.asarray(all_unis)
array_top = np.asarray(some_unis)

# bereken percentage en rond af op een heel getal
percentage_in_top = []
getal = np.divide(array_top, array_all_unis)
for i in getal*100:
    percentage_in_top.append(i)

pc_in_top_smooth = []
array_all_unis_smooth = array_all_unis + 1
getal = np.divide(array_top,array_all_unis_smooth)
for i in getal*100:
    pc_in_top_smooth.append(i)


sorted_pc = np.sort(percentage_in_top)
sorted_pc_smooth = np.sort(pc_in_top_smooth)
# print(sorted_pc)

unidb= pd.DataFrame()
unidb['country'] = hoi['location'].unique()
unidb = unidb.assign(pc = percentage_in_top)
unidb = unidb.assign(some = some_unis)
unidb = unidb.assign(all = all_unis)
unidb = unidb.assign(pc_smooth = pc_in_top_smooth)

print(unidb)

# maak plotje
output_file('./data_analysatie/percountry.html')

unidb_sorted = unidb.sort_values(by=['pc'])

# print(unidb_sorted['country'])
xas=unidb_sorted.country.unique()
yas=unidb_sorted['pc']
yas_smooth=unidb_sorted['pc_smooth']

p = figure(x_range=xas, plot_width=1800 ,title="landjes")
p.vbar(x=xas, top=yas, width=0.9)

p.xgrid.grid_line_color = 'lightgrey'
p.xaxis.major_label_orientation = 1
p.y_range.start = 0

show(p)

output_file('./data_analysatie/percountry1.html')

f = figure(x_range=xas, plot_width=1800 ,title="landjes")
f.vbar(x=xas, top=yas_smooth, width=0.9)

f.xgrid.grid_line_color = 'lightgrey'
f.xaxis.major_label_orientation = 1
f.y_range.start = 0

show(f)
