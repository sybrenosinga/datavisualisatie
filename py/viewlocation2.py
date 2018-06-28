import pandas as pd
import numpy as np

import itertools
import bokeh.palettes
from bokeh.plotting import figure
from bokeh.io import output_file, show, curdoc
from bokeh.models import DataRange1d
from bokeh.layouts import column, widgetbox, gridplot
from bokeh.models.widgets import MultiSelect, Paragraph
from bokeh.palettes import Spectral6
from bokeh.embed import components, server_document

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
global color_list
# multiselect different countries in 3 plots
color_list = bokeh.palettes.Category20[20]

def update(attrname, old, new):
    global color_list
    myString = ''
    for i in multi_select.value:

        country = df18['location'] == i
        rank = df18[country]['rank_order']
        studentstaff = df18[country]['stats_student_staff_ratio']
        size = df18[country]['stats_number_students']
        boiz = df18[country]['percentage_male']
        preinternational = df18[country]['stats_pc_intl_students']
        international = [i[:-1] for i in df18[country]['stats_pc_intl_students']]

        f.circle(x = rank,y = studentstaff, color = color_list[0],legend=[uni for uni in multi_select.value])
        h.circle(x = international, y = boiz,color = color_list[0],legend=[uni for uni in multi_select.value])
        g.circle(x= boiz,y=size, color = color_list[0],legend=[uni for uni in multi_select.value])
        color_list = color_list[1:]

    # next(color_list)

        # myString += '\n' + i
    # myText.text = myString

multi_locations = sorted(list(df18['location'].unique()),key=str.upper,reverse=True)
multi_select = MultiSelect(title="Country:", value=["0"], size=7,
                           options=multi_locations)
# myText = Paragraph(text='Initial Text', width=1200)
multi_select.on_change('value', update)
multi_select_widgetbox = widgetbox(multi_select)

# plot 1: rank vs student staff ratio
f = figure()
f.xaxis.axis_label="rank"
f.yaxis.axis_label="student staff ratio"
f.x_range=DataRange1d(start=0, end=1103)
f.y_range=DataRange1d(start=0, end=90)
f.legend.location = 'bottom_right'

# plot 3: percentage international vs percentage man (omdat size handig met t bolletje zelf kan)
h = figure()
h.xaxis.axis_label="percentage international"
h.yaxis.axis_label="percentage man"
h.x_range=DataRange1d(start=0, end=50)
h.y_range=DataRange1d(start=0, end=100)

# plot 2: size university vs percentage man
g = figure()
g.xaxis.axis_label="percentage man"
g.yaxis.axis_label="number of students"
g.x_range=DataRange1d(start=0, end=100)
g.y_range=DataRange1d(start=0, end=300000)

# gridplot alle 3 figuren en de widgetbox
f.plot_width, f.plot_height, h.plot_width, h.plot_height, g.plot_width, g.plot_height = 400,400,400,400,400,400
l=gridplot([[multi_select_widgetbox,None,None],[f,h,g]])
curdoc().add_root(l)

script = server_document("http://localhost:5006/location")
print(script)
