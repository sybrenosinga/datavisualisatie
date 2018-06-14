import pandas
import math
from bokeh.plotting import figure
from bokeh.io import output_file, show, curdoc
from bokeh.layouts import widgetbox, row
from bokeh.models.widgets import MultiSelect, Button, TextInput, Slider
from bokeh.models import ColumnDataSource
import numpy as np


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
                                    df_2017[df_2017['nid'] == row['nid']]['rank_order'].iloc[0] if check_empty(row, df_2018) else math.nan]
                        for i, row in df_2011.iterrows()], columns=['name', 'location', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])

dfT = df.transpose()
# for i in range(len(dfT.columns.tolist())):
#     print(dfT[dfT.columns[i]])

# print(dfT[dfT.columns[157]][2:10])

# # Prepare some data
# y = dfT[dfT.columns[157]][2:10]
# x = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
#
#
# # Create a figure object
# f = figure(x_range=x, y_range=(500, 0), title='kaas')
#
# # Create line plot
# source = ColumnDataSource(data=dict(x=x, y=y))
#
# f.line('x', 'y', source=source)
#
#
# def something(attr, old, new):
#     f.title.text = text.value
#
# text = TextInput(title="title", value='my sine wave')
#
# button = Button(label="Foo", button_type="success")
#
# inputs = widgetbox(text, button)
#
# text.on_change('value', something)
#
# layout = row(inputs, f)
#
# show(layout)

# Set up data
N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(plot_height=400, plot_width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


# Set up widgets
text = TextInput(title="title", value='my sine wave')
offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0, step=0.1)
phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)


# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values
    a = amplitude.value
    b = offset.value
    w = phase.value
    k = freq.value

    # Generate the new curve
    x = np.linspace(0, 4*np.pi, N)
    y = a*np.sin(k*x + w) + b

    source.data = dict(x=x, y=y)

for w in [offset, amplitude, phase, freq]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = widgetbox(text, offset, amplitude, phase, freq)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"
