from enum import unique
from click import style
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from vega_datasets import data

import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd

# Import data
df = pd.read_excel('./data/2009_2021-quarterly-surgical_wait_times.xlsx')

# Declare dash app
app = Dash(
    __name__#,
    # external_stylesheets = [dbc.themes.MINTY]   # why doesn't this apply to non-html components?
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

region_select = html.Div([
    dcc.Checklist(
        options = [{'label': 'Select All', 'value': 1}],
        value = [],
        id = 'region-select-all'
    ),
    dcc.Dropdown(
        df.HEALTH_AUTHORITY.unique()[1:-1],
        df.HEALTH_AUTHORITY.unique()[1],
        multi = True,
        id = 'region-select'
    )
])

tabs = dcc.Tabs([
    dcc.Tab(
        children = tab1,
        label = 'Tab 1'
    ),
    dcc.Tab(
        children = tab2,
        label = 'Tab 2'
    )
])

# Layout
app.layout = dbc.Container([
    title,
    region_select,
    tabs
])

@app.callback(
    Output('region-select', 'value'),
    Input('region-select-all', 'value'),
    State('region-select', 'value'),
    State('region-select', 'options')
)
def select_all_regions(all, regions_selected, regions):
    if all:
        return [region for region in regions]
    else:
        return regions_selected

@app.callback(
    Output('region-select-all', 'value'),
    Input('region-select', 'value'),
    State('region-select', 'options')
)
def deselect_checkbox(regions_selected, regions):
    if regions_selected == regions:
        return [1]
    else:
        return []

if __name__ == '__main__':
    app.run_server(debug=True)