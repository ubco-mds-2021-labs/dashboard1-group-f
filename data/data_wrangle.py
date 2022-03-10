import pandas as pd



df1 = pd.read_excel('./2009_2021-quarterly-surgical_wait_times.xlsx')
df2 = pd.read_excel('./2021_2022-quarterly-surgical_wait_times-q3-interim.xlsx')
df = df1.append(pd.DataFrame(data = df2), ignore_index=True)

# Cleaned column names
df.columns=[i.lower() for i in (df.columns.values.tolist())]
df = df.rename(columns={'fiscal_year': 'year', 
                        'hospital_name': 'hospital',
                       'procedure_group': 'procedure',
                       'completed_50th_percentile': 'wait_time_50', 
                       'completed_90th_percentile': 'wait_time_90'})
#convert <5 string to median value of 3
df = df.replace(['<5'],3)
# correct datatypes of columns, simplify fiscal year to year at start of first quarter
df.year = df.year.str.replace('(/).*', "", regex=True)
# drop rows with NA's
df = df.dropna()

# Save to CSV
df.to_csv('data.csv', index=False)