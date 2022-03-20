from pydoc import classname
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from pathlib import Path

import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd
import numpy as np

import SideBar.py
import SummaryTab.py
import CountTab.py
import TimesTab.py

# Load data
# Data for first plot 
df_all = pd.read_csv('data/processed/all_data.csv')
fraser_all = pd.read_csv('data/processed/all_fraser.csv')
interior_all = pd.read_csv('data/processed/all_interior.csv')
northern_all = pd.read_csv('data/processed/all_northern.csv')
psha_all = pd.read_csv('data/processed/all_psha.csv')
vc_all = pd.read_csv('data/processed/all_vancouver_coastal.csv')
vi_all = pd.read_csv('data/processed/all_vancouver_island.csv')

# Data for plots by hospital and procedure
df_main = pd.read_csv('data/processed/main_data.csv')
fraser = pd.read_csv('data/processed/fraser.csv')
interior = pd.read_csv('data/processed/interior.csv')
northern = pd.read_csv('data/processed/northern.csv')
psha = pd.read_csv('data/processed/psha.csv')
vc = pd.read_csv('data/processed/vancouver_coastal.csv')
vi = pd.read_csv('data/processed/vancouver_island.csv')
# add the Y_Q column and fix the year problem
def add_Y_Q(df):
    df['Y_Q']= df['year'].astype('str').str[2:4].map(str) + '_' + df['quarter'].map(str)
    df['year']= df['year'].astype('str').str[0:4].map(str)
dflist=[df_all,fraser_all,interior_all,northern_all,psha_all,vc_all,vi_all,df_main,fraser,interior,northern,psha,vc,vi]
for item in dflist:
    add_Y_Q(item)
# dataframe selection function: 
def region_df(region="All",alldata=False):
    if alldata==True: #alldata: data for first plot
        if region=="All":
            return df_all
        elif region=="Fraser":
            return fraser_all
        elif region=="Interior":
            return interior_all
        elif region=="Northern":
            return northern_all
        elif region=="Provincial Health Services Authority":
            return psha_all
        elif region=="Vancouver Coastal":
            return vc_all
        elif region=="Vancouver Island":
            return vi_all
    elif alldata==False:
        if region=="All":
            return df_main
        elif region=="Fraser":
            return fraser
        elif region=="Interior":
            return interior
        elif region=="Northern":
            return northern
        elif region=="Provincial Health Services Authority":
            return psha
        elif region=="Vancouver Coastal":
            return vc
        elif region=="Vancouver Island":
            return vi
    else:
        return None

# Declare dash app
app = Dash(__name__, external_stylesheets = [dbc.themes.MINTY])
# app.config.suppress_callback_exceptions = True
server = app.server

# Configure Altair - uncomment to run locally, comment out for Heroku deployment
alt.renderers.enable('mimetype')
alt.data_transformers.enable('data_server')
alt.data_transformers.disable_max_rows()

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

## Callback functions
# Navigation
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/count_tab_proc':
        return CountTab.proc
    elif pathname == '/count_tab_hosp':
        return CountTab.hosp
    elif pathname == '/times_tab_proc':
        return TimesTab.proc
    elif pathname == '/times_tab_hosp':
        return TimesTab.hosp
    else:
        return SummaryTab.written
        

# Settings
@app.callback(
    Output('region-select', 'value'),
    Input('region-select-all', 'n_clicks'),
    State('region-select', 'options')
)
def select_all_regions(_, regions):
    return [region for region in regions]

# Tabs
@app.callback(
    Output('tcp1','srcDoc'),
    Input('region-select', 'value'))
def update_tcp1(autho):
    return CountTab.line_plot_tc(list(autho))
@app.callback(
    Output('ttp1','srcDoc'),
    Input('region-select', 'value'))
def update_ttp1(autho):
    return TimesTab.line_plot_tt(list(autho))
@app.callback(
    Output('tcp2','srcDoc'),
    Input('region-select', 'value'))
def update_tcp2(autho):
    return CountTab.plot_bar_sbs_procedure_tc(list(autho))
@app.callback(
    Output('ttp2','srcDoc'),
    Input('region-select', 'value'))
def update_ttp2(autho):
    return TimesTab.plot_bar_sbs_procedure_tt(list(autho))
@app.callback(
    Output('tcp3','srcDoc'),
    Input('region-select', 'value'))
def update_tcp3(autho):
    return CountTab.plot_bar_sbs_hospital_tc(list(autho))
@app.callback(
    Output('ttp3','srcDoc'),
    Input('region-select', 'value'))
def update_ttp3(autho):
    return TimesTab.plot_bar_sbs_hospital_tt(list(autho))

# @app.callback(
#     Output('year-slider', 'children'),
#     Input('year-slider', 'value'))
# def update_output(input_value):
#     return 'Year(s) selected{}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)