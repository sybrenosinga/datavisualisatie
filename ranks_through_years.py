'''

Run file with 'bokeh serve --show ranks_through_years.py'

'''

import pandas
import math
import itertools
import bokeh.palettes
from bokeh.plotting import figure
from bokeh.io import show, curdoc
from bokeh.layouts import column, widgetbox
from bokeh.models.widgets import MultiSelect, TextInput
from bokeh.models import ColumnDataSource, CustomJS


def check_empty(row, df1, df2=0):
    if not df2 == 0:
        if df1[df1['nid'] == row['nid']]['rank_order'].empty or df2[df2['nid'] == row['nid']]['rank_order'].empty:
            return False
    else:
        if df1[df1['nid'] == row['nid']]['rank_order'].empty:
            return False
    return True


df_2011 = pandas.read_csv('./Data_csv/data_2011.csv')
df_2012 = pandas.read_csv('./Data_csv/data_2012.csv')
df_2013 = pandas.read_csv('./Data_csv/data_2013.csv')
df_2014 = pandas.read_csv('./Data_csv/data_2014.csv')
df_2015 = pandas.read_csv('./Data_csv/data_2015.csv')
df_2016 = pandas.read_csv('./Data_csv/data_2016.csv')
df_2017 = pandas.read_csv('./Data_csv/data_2017.csv')
df_2018 = pandas.read_csv('./Data_csv/data_2018.csv')

df = pandas.DataFrame([[row['name'], row['location'], row['rank_order'] if check_empty(row, df_2011) else math.nan,
                                    df_2012[df_2012['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(row, df_2012) else math.nan,
                                    df_2013[df_2013['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(row, df_2013) else math.nan,
                                    df_2014[df_2014['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(row, df_2014) else math.nan,
                                    df_2015[df_2015['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(row, df_2015) else math.nan,
                                    df_2016[df_2016['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(row, df_2016) else math.nan,
                                    df_2017[df_2017['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(row, df_2017) else math.nan,
                                    df_2018[df_2018['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(row, df_2018) else math.nan]
                        for i, row in df_2011.iterrows()], columns=['name', 'location', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])

dfT = df.transpose()

# Prepare some data
y = [dfT[dfT.columns[165]][2:10]]
x = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
legend = ['University of Amsterdam']
color = [bokeh.palettes.Category20[20][0]]

# Create a figure object
f = figure(x_range=x, y_range=(500, 0), title='University ranking per year', x_axis_label='Year', y_axis_label='Rank')

# Create line plot
source = ColumnDataSource(data=dict(x=[x], y=y, legend=[legend], color=[color]))

lines = f.multi_line(xs='x', ys='y', legend='legend', color='color', source=source, line_width=5)


def something(attr, old, new):
    color_list = []
    for i in itertools.cycle(bokeh.palettes.Category20[20]):
        if len(color_list) == len(multi_select.value):
            break
        color_list += [i]
    source.data = dict(x=[x for _ in range(len(multi_select.value))],
                       y=[dfT[dfT.columns[df.index[df['name'] == uni][0]]][2:10] for uni in multi_select.value],
                       legend=[uni for uni in multi_select.value],
                       color=color_list)


ds = ColumnDataSource(data=dict(options=[dfT[dfT.columns[x]]['name'] for x in dfT[dfT.columns]]))

multi_select = MultiSelect(title="University: (hold ctrl to select multiple)", value=['0'],
                           options=ds.data['options'])

ti = TextInput(placeholder='Search University',
               callback=CustomJS(args=dict(ds=ds, s=multi_select),
                                 code="s.options = ds.data['options'].filter(i => i.toLowerCase().includes(cb_obj.value.toLowerCase()));"))

multi_select.on_change('value', something)

f.legend.location = 'bottom_right'

curdoc().add_root(column(f, widgetbox(multi_select, ti)))
curdoc().title = "test"

show(column(f, widgetbox(multi_select, ti)))

