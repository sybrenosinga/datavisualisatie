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


# mean teaching score of ALL universities
print('TEACHING SCORE ALL')
print(df11['scores_teaching'].mean())
print(df12['scores_teaching'].mean())
print(df13['scores_teaching'].mean())
print(df14['scores_teaching'].mean())
print(df15['scores_teaching'].mean())
print(df16['scores_teaching'].mean())
print(df17['scores_teaching'].mean())
print(df18['scores_teaching'].mean())
print()

# mean teaching score of FIRST 199 universities
print('TEACHING SCORE TOP 199')
print(df11['scores_teaching'][0:198].mean())
print(df12['scores_teaching'][0:198].mean())
print(df13['scores_teaching'][0:198].mean())
print(df14['scores_teaching'][0:198].mean())
print(df15['scores_teaching'][0:198].mean())
print(df16['scores_teaching'][0:198].mean())
print(df17['scores_teaching'][0:198].mean())
print(df18['scores_teaching'][0:198].mean())
print()

# percentage man door de jaren heen
print("PERCENTAGE MAN '16 '17 '18")

pcm16 = df16['percentage_male']
pcm16 = pcm16 / 100
nrs16 = df16['stats_number_students']
malestudents16 = pcm16*nrs16
meanmale16 = malestudents16.mean()
meanstud16 = df16['stats_number_students'].mean()
percoftotstudmalemean16 = meanmale16 / meanstud16 * 100
print(percoftotstudmalemean16)

pcm17 = df17['percentage_male']
pcm17 = pcm17 / 100
nrs17 = df17['stats_number_students']
malestudents17 = pcm17*nrs17
meanmale17 = malestudents17.mean()
meanstud17 = df17['stats_number_students'].mean()
percoftotstudmalemean17 = meanmale17 / meanstud17 * 100
print(percoftotstudmalemean17)

pcm18 = df18['percentage_male']
pcm18 = pcm18 / 100
nrs18 = df18['stats_number_students']
malestudents18 = pcm18*nrs18
meanmale18 = malestudents18.mean()
meanstud18 = df18['stats_number_students'].mean()
percoftotstudmalemean18 = meanmale18 / meanstud18 * 100
print(percoftotstudmalemean18)
