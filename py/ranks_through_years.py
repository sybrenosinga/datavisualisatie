'''

Run file with 'bokeh serve --show ranks_through_years.py'

'''

import pandas
import itertools
import bokeh.palettes
from bokeh.plotting import figure
from bokeh.io import show, curdoc
from bokeh.layouts import column, row, widgetbox
from bokeh.models.widgets import MultiSelect, TextInput
from bokeh.models import ColumnDataSource, CustomJS, HoverTool

def update_source(attr, old, new):
    color_list = []
    for i in itertools.cycle(bokeh.palettes.Category20[20]):
        if len(color_list) == len(multi_select.value):
            break
        color_list += [i]
    source.data = dict(x=[x for _ in range(len(multi_select.value))],
                       y_all=[dfT_all[dfT_all.columns[df_all.index[df_all['name'] == uni][0]]][2:10] for uni in multi_select.value],
                       y_citations=[dfT_citations[dfT_citations.columns[df_citations.index[df_citations['name'] == uni][0]]][2:10] for uni in multi_select.value],
                       y_industry=[dfT_industry[dfT_industry.columns[df_industry.index[df_industry['name'] == uni][0]]][2:10] for uni in multi_select.value],
                       y_international=[dfT_international[dfT_international.columns[df_international.index[df_international['name'] == uni][0]]][2:10] for uni in multi_select.value],
                       y_research=[dfT_research[dfT_research.columns[df_research.index[df_research['name'] == uni][0]]][2:10] for uni in multi_select.value],
                       y_teaching=[dfT_teaching[dfT_teaching.columns[df_teaching.index[df_teaching['name'] == uni][0]]][2:10] for uni in multi_select.value],
                       legend=[uni for uni in multi_select.value],
                       color=color_list,
                       location=[df_all[df_all['name'] == uni]['location'] for uni in multi_select.value])

# Open data and create dataframes + transposes
df_all = pandas.DataFrame.from_csv('../Data_csv/rank_order.csv')
dfT_all = df_all.transpose()
df_citations = pandas.DataFrame.from_csv('../Data_csv/citations_rank.csv')
dfT_citations = df_citations.transpose()
df_industry = pandas.DataFrame.from_csv('../Data_csv/industry_income_rank.csv')
dfT_industry = df_industry.transpose()
df_international = pandas.DataFrame.from_csv('../Data_csv/international_outlook_rank.csv')
dfT_international = df_international.transpose()
df_research = pandas.DataFrame.from_csv('../Data_csv/research_rank.csv')
dfT_research = df_research.transpose()
df_teaching = pandas.DataFrame.from_csv('../Data_csv/teaching_rank.csv')
dfT_teaching = df_teaching.transpose()

# Prepare some data
y_all = [dfT_all[dfT_all.columns[165]][2:10]]
y_citations = [dfT_citations[dfT_citations.columns[165]][2:10]]
y_industry = [dfT_industry[dfT_industry.columns[165]][2:10]]
y_international = [dfT_international[dfT_international.columns[165]][2:10]]
y_research = [dfT_research[dfT_research.columns[165]][2:10]]
y_teaching = [dfT_teaching[dfT_teaching.columns[165]][2:10]]
x = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
legend = ['University of Amsterdam']
color = [bokeh.palettes.Category20[20][0]]
location = ['Netherlands']

# Create a figure object
f_all = figure(x_range=x, y_range=(500, 0), title='University ranking per year', x_axis_label='Year', y_axis_label='Rank')
f_citations = figure(x_range=x, y_range=(500, 0), title='University citations ranking per year', x_axis_label='Year', y_axis_label='Rank')
f_industry = figure(x_range=x, y_range=(500, 0), title='University industry income ranking per year', x_axis_label='Year', y_axis_label='Rank')
f_international = figure(x_range=x, y_range=(500, 0), title='University international outlook per year', x_axis_label='Year', y_axis_label='Rank')
f_research = figure(x_range=x, y_range=(500, 0), title='University research ranking per year', x_axis_label='Year', y_axis_label='Rank')
f_teaching = figure(x_range=x, y_range=(500, 0), title='University teaching ranking per year', x_axis_label='Year', y_axis_label='Rank')


# Create line plot
source = ColumnDataSource(data=dict(x=[x], y_all=y_all, y_citations=y_citations, y_industry=y_industry, y_international=y_international, y_research=y_research, y_teaching=y_teaching, legend=[legend], color=[color], location=[location]))

f_all.multi_line(xs='x', ys='y_all', color='color', source=source, line_width=5)
f_citations.multi_line(xs='x', ys='y_citations', color='color', source=source, line_width=5)
f_industry.multi_line(xs='x', ys='y_industry', color='color', source=source, line_width=5)
f_international.multi_line(xs='x', ys='y_international', color='color', source=source, line_width=5)
f_research.multi_line(xs='x', ys='y_research', color='color', source=source, line_width=5)
f_teaching.multi_line(xs='x', ys='y_teaching', color='color', source=source, line_width=5)

ds = ColumnDataSource(data=dict(options=[dfT_all[dfT_all.columns[x]]['name'] for x in dfT_all[dfT_all.columns]]))

multi_select = MultiSelect(title="University: (hold ctrl to select multiple)", value=['0'],
                           options=ds.data['options'], size=10)

ti = TextInput(placeholder='Search University',
               callback=CustomJS(args=dict(ds=ds, s=multi_select),
                                 code="s.options = ds.data['options'].filter(i => i.toLowerCase().includes(cb_obj.value.toLowerCase()));"))

f_all.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[('name', '@legend'), ('location', '@location')]))
f_citations.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[('name', '@legend'), ('location', '@location')]))
f_industry.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[('name', '@legend'), ('location', '@location')]))
f_international.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[('name', '@legend'), ('location', '@location')]))
f_research.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[('name', '@legend'), ('location', '@location')]))
f_teaching.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[('name', '@legend'), ('location', '@location')]))


multi_select.on_change('value', update_source)

f_all.legend.location = 'bottom_right'

f_citations.plot_height = 300
f_citations.plot_width = 300
f_industry.plot_height = 300
f_industry.plot_width = 300
f_international.plot_height = 300
f_international.plot_width = 300
f_research.plot_height = 300
f_research.plot_width = 300
f_teaching.plot_height = 300
f_teaching.plot_width = 300

curdoc().add_root(column(row(column(ti, multi_select), f_all), row(f_citations, f_industry, f_international, f_teaching), f_research))
curdoc().title = "University rankings through years"

show(column(row(column(ti, multi_select), f_all), row(f_citations, f_industry, f_international, f_teaching, f_research), f_research))
