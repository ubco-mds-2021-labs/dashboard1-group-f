from pydoc import classname
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd
import numpy as np

# Data cleaning and data wrangling
# Load data
# df1 = pd.read_excel('./data/2009_2021-quarterly-surgical_wait_times.xlsx')
# df2 = pd.read_excel('./data/2021_2022-quarterly-surgical_wait_times-q3-interim.xlsx')
df1 = pd.read_csv('./data/2009_2021-quarterly-surgical_wait_times.csv')
df2 = pd.read_csv('./data/2021_2022-quarterly-surgical_wait_times-q3-interim.csv')
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
# Create year_quarter column
df['Y_Q'] = df['year'].str[-2:].map(str) + '_' + df['quarter'].map(str)

# Declare dash app
app = Dash(__name__, external_stylesheets = [dbc.themes.MINTY])
app.config.suppress_callback_exceptions = True
app = app.server

# Sidebar components
title = html.H1(
    'BC Surgical Wait Time Dashboard',
    style = {'color': 'var(--bs-primary)'}
)

nav = dbc.Nav(
    children = [
        dbc.NavLink(
            'Waiting and Completed Cases - Tab 1',
            style = {'border-radius': '0.4rem 0 0 0.4rem'},
            href = '/tab1',
            active = 'exact'
        ),
        dbc.NavLink(
            'Wait Times, 50th and 90th Percentile - Tab 2',
            style = {'border-radius': '0.4rem 0 0 0.4rem'},
            href = '/tab2',
            active = 'exact'
        )
    ],
    pills = True,
    vertical = True
)

region_select = dbc.InputGroup(
    children = [
        dbc.Label('Health Region'),
        dcc.Dropdown(
            options = df.health_authority.unique()[1:],
            multi = True,
            style = {
                'border-radius': '0.4rem 0.4rem 0 0',
                'width': '100%'
            },
            className = 'dash-bootstrap',
            id = 'region-select'
        ),
        dbc.Button(
            'Select all regions',
            id = 'region-select-all',
            style = {
                'margin': 0,
                'border': 0,
                'border-radius': '0 0 0.4rem 0.4rem',
                'width': '100%'
            },
            n_clicks = 0,
            color = 'primary'
        )
    ],
    style = {'padding-right': '1rem'}
)

year_slider = html.Div(
    children = [
        dbc.Label('Year Range'),
        dcc.RangeSlider(
            2009, 
            2022, 
            1,
            value = [2020, 2021],
            marks = None,
            allowCross=False,
            tooltip = {'placement': 'bottom', 'always_visible': True},
            id='year-slider'
        )
    ],
    style = {'margin-top': '1rem'}
)

quarter_radio = html.Div(
    children = [
        dbc.Label('Quarter'),
        dbc.RadioItems(
            options = [
                {'label': q, 'value': q}
                for q in ['Q1', 'Q2', 'Q3', 'Q4', 'All']
            ],
            value = 'All',
            inline = True,
            id = 'quarter'
        )
    ],
    style = {'margin-top': '1rem'}
)

sidebar = html.Div(
    children = [
        title,
        html.Hr(style = {'color': 'var(--bs-primary)'}),
        nav,
        html.Hr(style = {'color': 'var(--bs-primary)'}),
        region_select,
        year_slider,
        quarter_radio
    ],
    style = {
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'width': '25rem',
        'height': '100%',
        'padding': '2rem 0 2rem 1rem'
    },
    className = 'bg-light'
)

# Layout
app.layout = dbc.Container(
    children = [
        dcc.Location(id = 'url'),
        sidebar,
        html.Div(
            id = 'page-content',
            style = {
                'margin-left': '25rem',
                'padding': '2rem 1rem'
            }
        )
    ],
    fluid = True
)


if __name__ == '__main__':
    app.run_server(debug=True)