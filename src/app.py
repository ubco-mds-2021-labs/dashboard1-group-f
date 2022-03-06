from enum import unique
from click import style
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from vega_datasets import data

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
# Create Year_quarter column
df['Y_Q'] = df['year'].str[-2:].map(str) + '_' + df['quarter'].map(str)

# Declare dash app
app = Dash(
    __name__,
    external_stylesheets = [dbc.themes.MINTY]   # why doesn't this apply to non-html components?
)
alt.renderers.enable('mimetype')
alt.data_transformers.enable('data_server')

## Plotting (side by side bar plot for procedures)
def plot_bar_sbs_procedure(autho=["Fraser"]):
    subdata=count[count.health_authority.isin(autho)]
    top=subdata.groupby(["procedure"])[["waiting"]].sum().reset_index().sort_values(by=['waiting'], ascending=False).head(20)["procedure"].tolist()
    subdata_top=subdata[subdata["procedure"].isin(top)]
    chart1 = alt.Chart(subdata_top).mark_bar().encode(
            x=alt.X('sum(waiting):Q',title="Total Waiting Cases"),
            y=alt.Y("procedure", sort='-x',title="Procedure"),
            color=alt.Color('year')
        ).properties(
            title="Number of Waiting Cases for Different Procedure Groups",
            width=200,
            height=300
        ).interactive()
    top2=subdata.groupby(["procedure"])[["completed"]].sum().reset_index().sort_values(by=['completed'], ascending=False).head(20)["procedure"].tolist()
    subdata_top2=subdata[subdata["procedure"].isin(top2)]
    chart2 = alt.Chart(subdata_top2).mark_bar().encode(
            x=alt.X('sum(completed):Q',title="Total Completed Cases"),
            y=alt.Y("procedure", sort='-x',title="Procedure"),
            color=alt.Color('year')
        ).properties(
            title="Number of Completed Cases for Different Procedure Groups",
            width=200,
            height=300
        ).interactive()
    chart_sbs=alt.hconcat(chart1,chart2).configure_axis(
        labelFontSize=10,
        titleFontSize=10
    ).to_html()
    return chart_sbs

def plot_bar_sbs_hospital(autho=["Fraser"]):
    subdata=count[count.health_authority.isin(autho)]
    top=subdata.groupby(["hospital"])[["waiting"]].sum().reset_index().sort_values(by=['waiting'], ascending=False).head(20)["hospital"].tolist()
    subdata_top=subdata[subdata["hospital"].isin(top)]
    chart1 = alt.Chart(subdata_top).mark_bar().encode(
            x=alt.X('sum(waiting):Q',title="Total Waiting Cases"),
            y=alt.Y("hospital", sort='-x',title="Hospital"),
            color=alt.Color('year')
        ).properties(
            title="Number of Waiting Cases for Different Hospitals",
            width=200,
            height=300
        ).interactive()
    top2=subdata.groupby(["hospital"])[["completed"]].sum().reset_index().sort_values(by=['completed'], ascending=False).head(20)["hospital"].tolist()
    subdata_top2=subdata[subdata["hospital"].isin(top2)]
    chart2 = alt.Chart(subdata_top2).mark_bar().encode(
            x=alt.X('sum(completed):Q',title="Total Completed Cases"),
            y=alt.Y("hospital", sort='-x',title="Hospital"),
            color=alt.Color('year')
        ).properties(
            title="Number of Completed Cases for Different Hospitals",
            width=200,
            height=300
        ).interactive()
    chart_sbs=alt.hconcat(chart1,chart2).configure_axis(
        labelFontSize=10,
        titleFontSize=10
    ).to_html()
    return chart_sbs

## Plotting (line plot)
def line_plot(autho=["Fraser"]):
    all_by_autho = df[(df['procedure']=='All Procedures') & (df['hospital']=='All Facilities') & (df.health_authority.isin(autho))]
    data=all_by_autho.groupby(['Y_Q'])[["waiting","completed"]].sum().reset_index().melt('Y_Q')
    chart=alt.Chart(data).mark_line().encode(
        x=alt.X('Y_Q', title='Year & Quarter'),
        y=alt.Y('value',title='Number of Cases'),
        color='variable'
    ).properties(
        title="Number of Waiting & Completed Cases by Time",
        width=920,
        height=280)
    return chart.interactive().to_html()

## Tab1-plot1: waiting cases by procedure
t1p1=html.Iframe(
    id="t1p1",
    srcDoc=plot_bar_sbs_procedure(autho=["Fraser"]),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

t1p2=html.Iframe(
    id="t1p2",
    srcDoc=plot_bar_sbs_hospital(autho=["Fraser"]),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

## Tab1-plot5: waiting & completed cases by time
t1p5=html.Iframe(
    id="t1p5",
    srcDoc=line_plot(),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# Tab 1 Layout Components
tab1 = [
    html.Div([
        dbc.Row(dbc.Col(t1p5)),
        dbc.Row(dbc.Col(t1p1)),
        dbc.Row(dbc.Col(t1p2)),
            ]),
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
        df.health_authority.unique()[1:-1],
        df.health_authority.unique()[1],
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

## Callback functions
@app.callback(
    Output('t1p1','srcDoc'),
    Input('region-select', 'value'))
def update_t1p1(autho):
    return plot_bar_sbs_procedure(list(autho))
@app.callback(
    Output('t1p2','srcDoc'),
    Input('region-select', 'value'))
def update_t1p2(autho):
    return plot_bar_sbs_hospital(list(autho))
@app.callback(
    Output('t1p5','srcDoc'),
    Input('region-select', 'value'))
def update_t1p5(autho):
    return line_plot(list(autho))
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8050, debug=True)