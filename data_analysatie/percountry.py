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
top = df18['location'].value_counts()

# landen en alle unis, met de landen in de zelfde volgorde als top
all_unis = []
for i in df18['location'].unique():
    koelheid = alles['countries'] == i
    uni = alles[koelheid]
    if i == 'United States':
        all_unis.append(3281)
    for j in uni['universities']:
        all_unis.append(j)


# definieer voor numpy
array_all_unis = np.asarray(all_unis)
array_top = np.asarray(top)

# bereken percentage en rond af op een heel getal
percentage_in_top = []
getal = np.divide(array_top, array_all_unis)
for i in getal*100:
    percentage_in_top.append(int(i))

# maak plotje
output_file('/home/judithcorsel/hoi/test/percountry.html')

xas=df18['location'].unique()
yas=percentage_in_top
print(xas)
print(yas)

p = figure(x_range=xas, title="landjes")
p.vbar(x=xas, top=percentage_in_top, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
