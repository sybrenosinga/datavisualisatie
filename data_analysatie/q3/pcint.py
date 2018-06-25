import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.layouts import gridplot
from bokeh.models import DataRange1d

# compare percetage men over 3 years

# get tables of all years
df11 = pd.read_csv('../../Data_csv/data_2011.csv')
df12 = pd.read_csv('../../Data_csv/data_2012.csv')
df13 = pd.read_csv('../../Data_csv/data_2013.csv')
df14 = pd.read_csv('../../Data_csv/data_2014.csv')
df15 = pd.read_csv('../../Data_csv/data_2015.csv')
df16 = pd.read_csv('../../Data_csv/data_2016.csv')
df17 = pd.read_csv('../../Data_csv/data_2017.csv')
df18 = pd.read_csv('../../Data_csv/data_2018.csv')

# collect data
pcint16 = []
pcint17 = []
pcint18 = []

pre18 = df18['stats_pc_intl_students']
for entry in pre18:
    entry = int(entry[:-1])
    pcint18.append(int(entry))

pre17 = df17['stats_pc_intl_students']
for entry in pre17:
    if entry[:-1] != '':
        pcint17.append(int(entry[:-1]))
    else:
        pcint17.append(0)

pre16 = df16['stats_pc_intl_students']
for entry in pre16:
    entry = int(entry[:-1])
    pcint16.append(int(entry))

# put data in list
boxpcint = [pcint16, pcint17, pcint18]

# # Create a figure instance
# fig = plt.figure(1, figsize=(9, 6))
#
# # Create an axes instance
# ax = fig.add_subplot(111)
# ax.grid()
# # ax.set_ylim(None, 125)
#
# # Create the boxplot
# bp = ax.boxplot(boxpcint)

# # Save the figure
# fig.savefig('pcint1.png', bbox_inches='tight')


# histogram 2016
arr_hist16, edges16 = np.histogram(pcint16[:800],
                               bins = int(100/4),
                               range = [0, 100])

# Put the information in a dataframe
uni16 = pd.DataFrame({'arr_pcint': arr_hist16,
                       'left': edges16[:-1],
                       'right': edges16[1:]})

# Create the blank plot
p16 = figure(plot_height = 600, plot_width = 600,
           title = 'Histogram of percentage international students',
          x_axis_label = 'pcint',
           y_axis_label = 'Number of universities')

p16.y_range=DataRange1d(start=0, end=175)

# Add a quad glyph
p16.quad(bottom=0, top=uni16['arr_pcint'],
       left=uni16['left'], right=uni16['right'],
       fill_color='green', line_color='black')

# histogram 2017
arr_hist17, edges17 = np.histogram(pcint17[:800],
                               bins = int(100/4),
                               range = [0, 100])

# Put the information in a dataframe
uni17 = pd.DataFrame({'arr_pcint': arr_hist17,
                       'left': edges17[:-1],
                       'right': edges17[1:]})

# Create the blank plot
p17 = figure(plot_height = 600, plot_width = 600,
           title = 'Histogram of percentage international students',
          x_axis_label = 'pcint',
           y_axis_label = 'Number of universities')

p17.y_range=DataRange1d(start=0, end=175)

# Add a quad glyph
p17.quad(bottom=0, top=uni17['arr_pcint'],
       left=uni17['left'], right=uni17['right'],
       fill_color='green', line_color='black')

# histogram 2018
arr_hist18, edges18 = np.histogram(pcint18[:800],
                               bins = int(100/4),
                               range = [0, 100])

# Put the information in a dataframe
uni18 = pd.DataFrame({'arr_pcint': arr_hist18,
                       'left': edges18[:-1],
                       'right': edges18[1:]})

# Create the blank plot
p18 = figure(plot_height = 600, plot_width = 600,
           title = 'Histogram of percentage international students',
          x_axis_label = 'pcint',
           y_axis_label = 'Number of universities')

p18.y_range=DataRange1d(start=0, end=175)

# Add a quad glyph
p18.quad(bottom=0, top=uni18['arr_pcint'],
       left=uni18['left'], right=uni18['right'],
       fill_color='green', line_color='black')

# Show the plot
show(gridplot([p16, p17, p18], [None, None, None]))
