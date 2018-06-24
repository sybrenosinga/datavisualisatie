import pandas
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

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

print(df_ranks_var.groupby(['location']).mean().sort_values('var_overall'))
