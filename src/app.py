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
root_dir = Path(__file__).parent.parent
data_file = root_dir.joinpath('data/processed/data.csv')
df = pd.read_csv(data_file)



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