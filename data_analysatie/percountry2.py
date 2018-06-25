import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import DataRange1d,FactorRange
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.transform import factor_cmap

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

# get table of all universities per country
alles = pd.read_csv('../Data_csv/all_universities.csv')

#  landen en unis in de top 1000
hoi = df18[df18.location != 'Northern Cyprus']
top = hoi['location'].value_counts()

# landen en alle unis, met de landen in de zelfde volgorde als top
all_unis = []
some_unis = []

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

unidb= pd.DataFrame()
unidb['country'] = hoi['location'].unique()
unidb = unidb.assign(pc = percentage_in_top)
unidb = unidb.assign(some = some_unis)
unidb = unidb.assign(all = all_unis)
unidb = unidb.assign(pc_smooth = pc_in_top_smooth)

# maak plot
output_file('./percountry.html')

# sort database
unidb_sorted = unidb.sort_values(by=['pc'], ascending = False)

# prepare data
xas=unidb_sorted.country.unique()
yas=unidb_sorted['pc']
yas_smooth=unidb_sorted['pc_smooth']
some_unis_sorted = unidb_sorted['some']
all_unis_sorted = unidb_sorted['all']

yas_list = []
for i in yas:
    yas_list.append(i)

yas_smooth_list = []
for i in yas_smooth:
    yas_smooth_list.append(i)

locations = xas
pcs = ['original', 'smooth']

data = {'locations':locations,
        'y':yas_list,
        'y smooth':yas_smooth_list}


x = [(location, pc) for location in locations[:18] for pc in pcs[:18] ]
counts = sum(zip(data['y'] ,data['y smooth']), ())

# prepare tooltip
source = ColumnDataSource(data=dict(
    x=x[:36],
    counts=counts[:36],
    locations=[i for i in xas for _ in (0, 1)][:36],
    pc=[i for i in yas for _ in (0, 1)][:36],
    pc_smooth=[i for i in yas_smooth for _ in (0, 1)][:36],
    some=[i for i in some_unis_sorted for _ in (0, 1)][:36],
    all=[i for i in all_unis_sorted for _ in (0, 1)][:36],
))

hover = HoverTool(tooltips=[
    ("country", "@locations"),
    ("# top 1000", "@some"),
    ("# alles", "@all"),
    ("original", "@pc"),
    ("smooth", "@pc_smooth")
])

f = figure(x_range=FactorRange(*x), plot_width=1800 , plot_height = 500, tools =[hover],title="percentage of universities in top 1000")
f.vbar(x='x', top='counts', legend = 'percentage of universities',line_color= 'white', fill_color=factor_cmap('x', palette=['#0066cc','#b3d9ff'], factors=pcs, start=1, end=2), width=0.85, source=source)

f.xgrid.grid_line_color = 'lightgrey'
f.xaxis.major_label_orientation = 1
f.y_range.start = 0
f.y_range=DataRange1d(start=0, end=35)

show(f)
