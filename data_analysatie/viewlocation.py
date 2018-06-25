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
from bokeh.models.widgets import MultiSelect, TextInput
from bokeh.models import ColumnDataSource, CustomJS, HoverTool

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

# multiselect different countries in 3 plots
def update(attrname, old, new):
    myString = ''
    color_list = []

    for i in itertools.cycle(bokeh.palettes.Category20[20]):

        if len(color_list) == len(multi_select.value):
            break
        color_list += [i]

        source.data = dict(
            location=[df18[df18['location'] == uni]for uni in multi_select.value],
            xf=[df18[uni]['rank_order'] for uni in multi_select.value],
            yf=[df18[uni]['stats_student_staff_ratio'] for uni in multi_select.value],
            # xh=[df18[uni]['stats_pc_intl_students'][:-1] for uni in multi_select.value],
            # yh=[df18[uni]['percentage_male'] for uni in multi_select.value],
            xg=[df18[uni]['percentage_male'] for uni in multi_select.value],
            yg=[df18[uni]['stats_number_students'] for uni in multi_select.value],
            legend=[uni for uni in multi_select.value],
            color_list=[color * 1103 for color in color_list],
        )

# print(df18[df18['location'] == 'Uganda'])

        # myString += '\n' + i
    # myText.text = myString

legend = ['University of Amsterdam']
color_list = [bokeh.palettes.Category20[20][0]]

source = ColumnDataSource(data=dict(
            location=df18['location'],
            xf=df18['rank_order'],
            yf=df18['stats_student_staff_ratio'],
            # xh=df18['stats_pc_intl_students'][:-1],
            # yh=df18['percentage_male'],
            xg=df18['percentage_male'],
            yg=df18['stats_number_students'],
        ))
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

# # plot 3: percentage international vs percentage man (omdat size handig met t bolletje zelf kan)
# h = figure()
# h.xaxis.axis_label="percentage international"
# h.yaxis.axis_label="percentage man"
# h.x_range=DataRange1d(start=0, end=50)
# h.y_range=DataRange1d(start=0, end=100)

# plot 2: size university vs percentage man
g = figure()
g.xaxis.axis_label="percentage man"
g.yaxis.axis_label="number of students"
g.x_range=DataRange1d(start=0, end=100)
g.y_range=DataRange1d(start=0, end=300000)

f.circle(x = 'xf',y = 'yf', color = 'color_list',legend='legend',source=source)
# h.circle(x = 'xh', y = 'yh',color = 'color_list',legend='legend',source=source)
g.circle(x= 'xg', y='yg', color = 'color_list',legend='legend',source=source)

# gridplot alle 3 figuren en de widgetbox
l=gridplot([[multi_select_widgetbox,None,None],[f,None,g]])
curdoc().add_root(l)
