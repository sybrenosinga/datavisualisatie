#
#   Scrape ranking data from website
#   replace missing values by mean
#
#   ! Outdated !
#


from bs4 import BeautifulSoup
import pandas as pd

# open html file and read with beautifulsoup
soup = BeautifulSoup(open('./ranking_table', 'rb'), 'html.parser')

# Put scraped data into data frame
df = pd.DataFrame([[A.get_text(), B.get_text(), C.get_text(), D.get_text(), E.get_text(), F.get_text()] for A, B, C, D, E, F in soup.findAll('tr')[1:]], columns=['Rank', 'Name', 'FTE Students', 'Students per Staff', 'International Students (%)', 'Female:Male Ratio'])

# Replace missing values by mean
for colname in df.columns.tolist():
    if colname == 'FTE Students':
        df[colname] = df[colname].apply(lambda val: val.replace(',', ''))
        mean_series = df[df[colname] != 'n/a'][colname].apply(int)
        mean = int(mean_series.mean())
        # print(mean)
        df[colname] = df[colname].apply(lambda val: val if val != 'n/a' else mean)
    if colname == 'International Students (%)':
        df[colname] = df[colname].apply(lambda val: val.replace('%', ''))
        mean_series = df[df[colname] != 'n/a'][colname].apply(int)
        mean = int(mean_series.mean())
        # print(mean)
        df[colname] = df[colname].apply(lambda val: '{}%'.format(val) if val != 'n/a' else '{}%'.format(mean))
    if colname == 'Female:Male Ratio':
        mean_series = df[df[colname] != 'n/a'][colname]
        mean_f = int(mean_series.apply(lambda val: int(val[:2])).mean())
        mean_m = int(mean_series.apply(lambda val: int(val[5:])).mean())
        # print(mean_m)
        # print(mean_f)
        df[colname] = df[colname].apply(lambda val: val if val != 'n/a' else '{} : {}'.format(mean_f, mean_m))
    if colname == 'Students per Staff':
        mean_series = df[colname].where(lambda val: val != 'n/a')
        df[colname] = df[colname].apply(lambda val: float(val))
        mean = df[colname].mean()
        # print(mean)
        df[colname] = df[colname].apply(lambda val: val if val != 'n/a' else mean)

print(df)

# Check if columns have missing data
for colname in df.columns.tolist():
    print('contains n/a: {}'.format(df[colname].apply(lambda val: str(val)).str.contains('n/a').any()))