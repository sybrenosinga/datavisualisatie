from bs4 import BeautifulSoup
import pandas as pd
# total amount of universities per country dataframe

# open html file
soup = BeautifulSoup(open('./totalunis.html'), 'html.parser')

# find all countries
countries = [country.get_text() for country in soup.findAll('strong')]
countries = countries[10:]

# find corresponding univerity numbers
unis = [uni.get_text() for uni in soup.findAll('td')[7::8]]

# put in table
tudf = pd.DataFrame()
tudf['countries'] = countries
tudf = tudf.assign(universities = unis)

# make it US instead of USA
tudf.set_value(0, 'countries', 'United States')
tudf.set_value(31, 'countries', 'Czech Republic')
tudf.set_value(35, 'countries', 'Russian Federation')
tudf.set_value(59, 'countries', 'Northern Cyprus')

# return csv
tudf.to_csv('./Data_csv/all_universities.csv')

# N.B. hij slaat het eerste land niet op
