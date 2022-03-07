from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd
import numpy as np

# Data cleaning and data wrangling
# Load data
df1 = pd.read_excel('./data/2009_2021-quarterly-surgical_wait_times.xlsx')
df2 = pd.read_excel('./data/2021_2022-quarterly-surgical_wait_times-q3-interim.xlsx')
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
#create counts dataset
count = df.drop(["wait_time_50","wait_time_90"], axis=1,inplace=False).dropna()
#data subsetting
main = df[(df['procedure']!='All Procedures') & (df['hospital']!='All Facilities') & (df['health_authority']!='All Health Authorities')]
count  = count[(count['procedure']!='All Procedures') & (count['hospital']!='All Facilities') & (count['health_authority']!='All Health Authorities')]
alldata = df[(df['procedure']=='All Procedures') & (df['hospital']=='All Facilities') & (df['health_authority']=='All Health Authorities')]
# Declare dash app
app = Dash(
    __name__,
    external_stylesheets = [dbc.themes.MINTY]
)

# Tab 1 Layout Components
tab1 = [
    html.P('You selected tab 1!')
]

# Tab 2 Layout Components
tab2 = [
    html.P('You selected tab 2!')
]

# Main Layout components
title = html.H1('BC Surgical Wait Time Dashboard')

region_select = dbc.InputGroup([
    dcc.Dropdown(
        options = df.health_authority.unique()[1:],
        multi = True,
        style = {
            'border-radius': '0.4rem 0 0 0.4rem',
            'width': '55rem'
        },
        className = 'dash-bootstrap',
        id = 'region-select'
    ),
    dbc.Button(
        'Select all regions',
        id = 'region-select-all',
        style = {'border': '0'},
        n_clicks = 0,
        color = 'primary'
    )
])

tabs = dbc.Tabs([
    dbc.Tab(
        children = tab1,
        label = 'Tab 1'
    ),
    dbc.Tab(
        children = tab2,
        label = 'Tab 2'
    )
])

# Layout
app.layout = dbc.Container([
    title,
    region_select,
    tabs
], fluid = True)

@app.callback(
    Output('region-select', 'value'),
    Input('region-select-all', 'n_clicks'),
    State('region-select', 'options')
)
def select_all_regions(_, regions):
    return [region for region in regions]

if __name__ == '__main__':
    app.run_server(debug=True)