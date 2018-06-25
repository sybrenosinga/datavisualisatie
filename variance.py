import warnings
import pandas
import itertools
import bokeh.palettes
from bokeh.plotting import figure
from bokeh.io import show, curdoc
from bokeh.layouts import column, row, widgetbox
from bokeh.models.widgets import MultiSelect, TextInput, Dropdown
from bokeh.models import ColumnDataSource, CustomJS, HoverTool

warnings.simplefilter(action='ignore', category=FutureWarning)


def update_graphs(attr, old, new):
    dropdown.label = dropdown.value.replace('var_', '').replace('_', ' ')
    f1.x_range.factors = list(df_scores_var.groupby(['location']).mean().sort_values(dropdown.value, ascending=False).index.values)
    f.x_range.factors = list(df_scores_var.sort_values(dropdown.value, ascending=False)['name'])
    f2.x_range.factors = list(df_scores_var.nlargest(10, dropdown.value)['name'])
    f3.x_range.factors = list(df_scores_var.nsmallest(10, dropdown.value)['name'])
    f1.title.text = 'Variance {} per country from 2011 to 2018'.format(dropdown.value).replace('var_', '').replace('_', ' ')
    f.title.text = 'Variance {} from 2011 to 2018'.format(dropdown.value).replace('var_', '').replace('_', ' ')
    f2.title.text = 'Top 10 least stable universities ({})'.format(dropdown.value).replace('var_', '').replace('_', ' ')
    f3.title.text = 'Top 10 most stable universities ({})'.format(dropdown.value).replace('var_', '').replace('_', ' ')
    source.data=dict(x_f=df_scores_var.sort_values(dropdown.value, ascending=False)['name'].tolist(),
                     top_f=df_scores_var.sort_values(dropdown.value, ascending=False)[dropdown.value])
    source1.data=dict(x_f1=df_scores_var.groupby(['location']).mean().sort_values(dropdown.value, ascending=False).index.values,
                     top_f1=df_scores_var.groupby(['location']).mean().sort_values(dropdown.value, ascending=False)[dropdown.value])
    source2.data=dict(x_f2=df_scores_var.nlargest(10, dropdown.value)['name'].tolist(),
                     top_f2=df_scores_var.nlargest(10, dropdown.value)[dropdown.value])
    source3.data=dict(x_f3=df_scores_var.nsmallest(10, dropdown.value)['name'].tolist(),
                     top_f3=df_scores_var.nsmallest(10, dropdown.value)[dropdown.value])
    return




df_all = pandas.DataFrame.from_csv('./Data_csv/rank_order.csv')
dfT_all = df_all.transpose()
df_citations = pandas.DataFrame.from_csv('./Data_csv/citations_rank.csv')
dfT_citations = df_citations.transpose()
df_industry = pandas.DataFrame.from_csv('./Data_csv/industry_income_rank.csv')
dfT_industry = df_industry.transpose()
df_international = pandas.DataFrame.from_csv('./Data_csv/international_outlook_rank.csv')
dfT_international = df_international.transpose()
df_research = pandas.DataFrame.from_csv('./Data_csv/research_rank.csv')
dfT_research = df_research.transpose()
df_teaching = pandas.DataFrame.from_csv('./Data_csv/teaching_rank.csv')
dfT_teaching = df_teaching.transpose()

df_citations_scores = pandas.DataFrame.from_csv('./Data_csv/citations.csv')
dfT_citations_scores = df_citations_scores.transpose()
df_industry_scores = pandas.DataFrame.from_csv('./Data_csv/industry_income.csv')
dfT_industry_scores = df_industry_scores.transpose()
df_international_scores = pandas.DataFrame.from_csv('./Data_csv/international_outlook.csv')
dfT_international_scores = df_international_scores.transpose()
df_research_scores = pandas.DataFrame.from_csv('./Data_csv/research.csv')
dfT_research_scores = df_research_scores.transpose()
df_teaching_scores = pandas.DataFrame.from_csv('./Data_csv/teaching.csv')
dfT_teaching_scores = df_teaching_scores.transpose()

df_scores_var = pandas.concat([df_all['name'], df_all['location'], df_citations_scores.var(axis=1), df_industry_scores.var(axis=1), df_international_scores.var(axis=1), df_research_scores.var(axis=1), df_teaching_scores.var(axis=1)], axis=1)
df_scores_var.columns = ['name', 'location', 'var_citations', 'var_industry_income', 'var_international_outlook', 'var_research', 'var_teaching']


df_ranks_var = pandas.concat([df_all['name'], df_all['location'], df_all.var(axis=1), df_citations.var(axis=1), df_industry.var(axis=1), df_international.var(axis=1), df_research.var(axis=1), df_teaching.var(axis=1)], axis=1)
df_ranks_var.columns = ['name', 'location', 'var_overall', 'var_citations', 'var_industry_income', 'var_international_outlook', 'var_research', 'var_teaching']


category = 'var_citations'
source = ColumnDataSource(data=dict(x_f=df_scores_var.sort_values('var_citations', ascending=False)['name'].tolist(),
                                    top_f=df_scores_var.sort_values('var_citations', ascending=False)['var_citations']))
source1 = ColumnDataSource(data=dict(x_f1= df_scores_var.groupby(['location']).mean().sort_values('var_citations', ascending=False).index.values,
                                    top_f1=df_scores_var.groupby(['location']).mean().sort_values('var_citations', ascending=False)['var_citations']))
source2 = ColumnDataSource(data=dict(x_f2=df_scores_var.nlargest(10, 'var_citations')['name'].tolist(),
                                    top_f2=df_scores_var.nlargest(10, 'var_citations')['var_citations']))
source3 = ColumnDataSource(data=dict(x_f3=df_scores_var.nsmallest(10, 'var_citations')['name'].tolist(),
                                    top_f3=df_scores_var.nsmallest(10, 'var_citations')['var_citations']))

f = figure(x_range=df_scores_var.sort_values('var_citations', ascending=False)['name'].tolist(), title='Variance citations from 2011 t0 2018', y_axis_label='variance')
f.vbar(x='x_f', top='top_f', source=source, bottom=0, width=0.5, fill_color="#b3de69")
f.xaxis.major_label_orientation = 1
f.plot_width = 1750

f1 = figure(x_range=df_scores_var.groupby(['location']).mean().sort_values('var_citations', ascending=False).index.values, title='Variance citations per country from 2011 to 2018', y_axis_label='variance')
f1.vbar(x='x_f1', top='top_f1', source=source1, bottom=0, width=0.5, fill_color="#b3de69")
f1.xaxis.major_label_orientation = 1

f2 = figure(x_range=df_scores_var.nlargest(10, 'var_citations')['name'].tolist(), title='Top 10 least stable universities (citations)', y_axis_label='variance')
f2.vbar(x='x_f2', top='top_f2', source=source2, bottom=0, width=0.5, fill_color="#b3de69")
f2.xaxis.major_label_orientation = 1

f3 = figure(x_range=df_scores_var.nsmallest(10, 'var_citations')['name'].tolist(), title='Top 10 most stable universities (citations)', y_axis_label='variance')
f3.vbar(x='x_f3', top='top_f3', source=source3, bottom=0, width=0.5, fill_color="#b3de69")
f3.xaxis.major_label_orientation = 1

dropdown = Dropdown(label="Category", button_type="warning", menu=[('citations', 'var_citations'), ('industry income', 'var_industry_income'), ('international outlook', 'var_international_outlook'), ('research', 'var_research'), ('teaching', 'var_teaching')])

dropdown.on_change('value', update_graphs)


curdoc().add_root(column(f, row(f1, f2, f3, dropdown)))
curdoc().title = "Variance scores Universities"


show(column(f, row(f1, f2, f3, dropdown)))