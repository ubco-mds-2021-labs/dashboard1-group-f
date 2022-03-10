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
# df = df1.append(pd.DataFrame(data = df2), ignore_index=True)
# # Cleaned column names
# df.columns=[i.lower() for i in (df.columns.values.tolist())]
# df = df.rename(columns={'fiscal_year': 'year', 
#                         'hospital_name': 'hospital',
#                        'procedure_group': 'procedure',
#                        'completed_50th_percentile': 'wait_time_50', 
#                        'completed_90th_percentile': 'wait_time_90'})
# #convert <5 string to median value of 3
# df = df.replace(['<5'],3)
# # correct datatypes of columns, simplify fiscal year to year at start of first quarter
# df.year = df.year.str.replace('(/).*', "", regex=True)
# # drop rows with NA's
# df = df.dropna()

df = pd.read_csv('./data/data.csv')
#create counts dataset
count = df.drop(["wait_time_50","wait_time_90"], axis=1,inplace=False).dropna()
#data subsetting
main = df[(df['procedure']!='All Procedures') & (df['hospital']!='All Facilities') & (df['health_authority']!='All Health Authorities')]
count  = count[(count['procedure']!='All Procedures') & (count['hospital']!='All Facilities') & (count['health_authority']!='All Health Authorities')]
alldata = df[(df['procedure']=='All Procedures') & (df['hospital']=='All Facilities') & (df['health_authority']=='All Health Authorities')]
# Create year_quarter column
df['Y_Q'] = df['year'].astype('str').str[-2:].map(str) + '_' + df['quarter'].map(str)

# Declare dash app
app = Dash(__name__, external_stylesheets = [dbc.themes.MINTY])
app.config.suppress_callback_exceptions = True
server = app.server

# # Configure Altair
# alt.renderers.enable('mimetype')
# alt.data_transformers.enable('data_server')

# ## Plotting 
# # Tab 1 line plot
# def line_plot_t1(autho=["Fraser"]):
#     all_by_autho = df[(df['procedure']=='All Procedures') & (df['hospital']=='All Facilities') & (df.health_authority.isin(autho))]
#     data=all_by_autho.groupby(['Y_Q'])[["waiting","completed"]].sum().reset_index().melt('Y_Q')
#     chart=alt.Chart(data).mark_line().encode(
#         x=alt.X('Y_Q', title='Year & Quarter'),
#         y=alt.Y('value',title='Number of Cases'),
#         color='variable'
#     ).properties(
#         title="Number of Waiting & Completed Cases by Time",
#         width=920,
#         height=280)
#     return chart.interactive().to_html()

# # Tab 2 line plot
# def line_plot_t2(autho=["Fraser"]):
#     all_by_autho = df[(df['procedure']=='All Procedures') & (df['hospital']=='All Facilities') & (df.health_authority.isin(autho))]
#     data=all_by_autho.groupby(['Y_Q'])[["wait_time_50","wait_time_90"]].mean().reset_index().melt('Y_Q')
#     chart=alt.Chart(data).mark_line().encode(
#         x=alt.X('Y_Q', title='Year & Quarter'),
#         y=alt.Y('value',title='Wait Time (weeks'),
#         color='variable'
#     ).properties(
#         title="50th and 90th Percentile Waiting Times",
#         width=920,
#         height=280)
#     return chart.interactive().to_html()


# # Tab 1 side by side bar plot for procedures
# def plot_bar_sbs_procedure_t1(autho=["Fraser"]):
#     subdata=count[count.health_authority.isin(autho)]
#     top=subdata.groupby(["procedure"])[["waiting"]].sum().reset_index().sort_values(by=['waiting'], ascending=False).head(20)["procedure"].tolist()
#     subdata_top=subdata[subdata["procedure"].isin(top)]
#     chart1 = alt.Chart(subdata_top).mark_bar().encode(
#             x=alt.X('sum(waiting):Q',title="Total Waiting Cases"),
#             y=alt.Y("procedure", sort='-x',title="Procedure"),
#             color=alt.Color('year')
#         ).properties(
#             title="Number of Waiting Cases for Different Procedure Groups",
#             width=200,
#             height=300
#         ).interactive()
#     top2=subdata.groupby(["procedure"])[["completed"]].sum().reset_index().sort_values(by=['completed'], ascending=False).head(20)["procedure"].tolist()
#     subdata_top2=subdata[subdata["procedure"].isin(top2)]
#     chart2 = alt.Chart(subdata_top2).mark_bar().encode(
#             x=alt.X('sum(completed):Q',title="Total Completed Cases"),
#             y=alt.Y("procedure", sort='-x',title="Procedure"),
#             color=alt.Color('year')
#         ).properties(
#             title="Number of Completed Cases for Different Procedure Groups",
#             width=200,
#             height=300
#         ).interactive()
#     chart_sbs=alt.hconcat(chart1,chart2).configure_axis(
#         labelFontSize=10,
#         titleFontSize=10
#     ).to_html()
#     return chart_sbs

# # Tab 2 side by side bar plot for procedures
# def plot_bar_sbs_procedure_t2(autho=["Fraser"]):
#     subdata=main[main.health_authority.isin(autho)]
#     top=subdata.groupby(["procedure"])[["wait_time_50"]].mean().reset_index().sort_values(by=['wait_time_50'], ascending=False).head(20)["procedure"].tolist()
#     subdata_top=subdata[subdata["procedure"].isin(top)]
#     chart1 = alt.Chart(subdata_top).mark_tick().encode(
#             x=alt.X('mean(wait_time_50):Q',title="Wait Time (weeks)"),
#             y=alt.Y("procedure", sort='-x',title="Procedure"),
#             color=alt.Color('year')
#         ).properties(
#             title="Waiting Times for 50 percent of Cases by Procedure",
#             width=200,
#             height=300
#         ).interactive()
#     top2=subdata.groupby(["procedure"])[["wait_time_90"]].mean().reset_index().sort_values(by=['wait_time_90'], ascending=False).head(20)["procedure"].tolist()
#     subdata_top2=subdata[subdata["procedure"].isin(top2)]
#     chart2 = alt.Chart(subdata_top2).mark_tick().encode(
#             x=alt.X('mean(wait_time_90):Q',title="Wait Time (weeks)"),
#             y=alt.Y("procedure", sort='-x',title="Procedure"),
#             color=alt.Color('year')
#         ).properties(
#             title="Waiting Times for 90 percent of Cases by Procedure",
#             width=200,
#             height=300
#         ).interactive()
#     chart_sbs=alt.hconcat(chart1,chart2).configure_axis(
#         labelFontSize=10,
#         titleFontSize=10
#     ).to_html()
#     return chart_sbs

# # Tab 1 side by side bar plot for hospital
# def plot_bar_sbs_hospital_t1(autho=["Fraser"]):
#     subdata=count[count.health_authority.isin(autho)]
#     top=subdata.groupby(["hospital"])[["waiting"]].sum().reset_index().sort_values(by=['waiting'], ascending=False).head(20)["hospital"].tolist()
#     subdata_top=subdata[subdata["hospital"].isin(top)]
#     chart1 = alt.Chart(subdata_top).mark_bar().encode(
#             x=alt.X('sum(waiting):Q',title="Total Waiting Cases"),
#             y=alt.Y("hospital", sort='-x',title="Hospital"),
#             color=alt.Color('year')
#         ).properties(
#             title="Number of Waiting Cases for Different Hospitals",
#             width=200,
#             height=300
#         ).interactive()
#     top2=subdata.groupby(["hospital"])[["completed"]].sum().reset_index().sort_values(by=['completed'], ascending=False).head(20)["hospital"].tolist()
#     subdata_top2=subdata[subdata["hospital"].isin(top2)]
#     chart2 = alt.Chart(subdata_top2).mark_bar().encode(
#             x=alt.X('sum(completed):Q',title="Total Completed Cases"),
#             y=alt.Y("hospital", sort='-x',title="Hospital"),
#             color=alt.Color('year')
#         ).properties(
#             title="Number of Completed Cases for Different Hospitals",
#             width=200,
#             height=300
#         ).interactive()
#     chart_sbs=alt.hconcat(chart1,chart2).configure_axis(
#         labelFontSize=10,
#         titleFontSize=10
#     ).to_html()
#     return chart_sbs

# # Tab 2 side by side bar plot for hospital
# def plot_bar_sbs_hospital_t2(autho=["Fraser"]):
#     subdata=main[main.health_authority.isin(autho)]
#     top=subdata.groupby(["hospital"])[["wait_time_90"]].mean().reset_index().sort_values(by='hospital').head(20)["hospital"].tolist()
#     subdata_top=subdata[subdata["hospital"].isin(top)]
#     chart1 = alt.Chart(subdata_top).mark_tick().encode(
#             x=alt.X('mean(wait_time_50):Q',title="Wait Time (weeks)"),
#             y=alt.Y("hospital", sort='-x',title="Hospital"),
#             color=alt.Color('year')
#         ).properties(
#             title="Waiting Times for 50 percent of Cases by Hospitals",
#             width=200,
#             height=300
#         ).interactive()
#     top2=subdata.groupby(["hospital"])[["wait_time_90"]].mean().reset_index().sort_values(by='hospital').head(20)["hospital"].tolist()
#     subdata_top2=subdata[subdata["hospital"].isin(top2)]
#     chart2 = alt.Chart(subdata_top2).mark_tick().encode(
#             x=alt.X('mean(wait_time_90):Q',title="Wait Time (weeks)"),
#             y=alt.Y("hospital", sort='-x',title="Hospital"),
#             color=alt.Color('year')
#         ).properties(
#             title="Waiting Times for 90 percent of Cases by Hospitals",
#             width=200,
#             height=300
#         ).interactive()
#     chart_sbs=alt.hconcat(chart1,chart2).configure_axis(
#         labelFontSize=10,
#         titleFontSize=10
#     ).to_html()
#     return chart_sbs

# # Tab1-plot1: waiting & completed cases by time
# t1p1=html.Iframe(
#     id="t1p1",
#     srcDoc=line_plot_t1(),
#     style={'border-width': '0', 'width': '100%', 'height': '400px'}
# )

# # Tab2-plot1: wait times (50th and 90th percentile) by time
# t2p1=html.Iframe(
#     id="t2p1",
#     srcDoc=line_plot_t2(),
#     style={'border-width': '0', 'width': '100%', 'height': '400px'}
# )

# # Tab1-plot2: waiting and completed cases by procedure
# t1p2=html.Iframe(
#     id="t1p2",
#     srcDoc=plot_bar_sbs_procedure_t1(autho=["Fraser"]),
#     style={'border-width': '0', 'width': '100%', 'height': '400px'}
# )

# # Tab2-plot2: wait times (50th and 90th percentile) by procedure
# t2p2=html.Iframe(
#     id="t2p2",
#     srcDoc=plot_bar_sbs_procedure_t2(autho=["Fraser"]),
#     style={'border-width': '0', 'width': '100%', 'height': '400px'}
# )

# # Tab1-plot3: waiting and completed cases by hospital
# t1p3=html.Iframe(
#     id="t1p3",
#     srcDoc=plot_bar_sbs_hospital_t1(autho=["Fraser"]),
#     style={'border-width': '0', 'width': '100%', 'height': '400px'}
# )

# # Tab2-plot3: wait times (50th and 90th percentile) by hospital
# t2p3=html.Iframe(
#     id="t2p3",
#     srcDoc=plot_bar_sbs_hospital_t2(autho=["Fraser"]),
#     style={'border-width': '0', 'width': '100%', 'height': '400px'}

# )

# # Tab 1 Layout Components
# tab1 = [
#     html.Div([
#         dbc.Row(dbc.Col(t1p1)),
#         dbc.Row(dbc.Col(t1p2)),
#         dbc.Row(dbc.Col(t1p3)),
#             ]),
#     ]

# # Tab 2 Layout Components
# tab2 = [
#     html.Div([
#         dbc.Row([
#             dbc.Col(t2p1, width=13)]),
#         dbc.Row(dbc.Col(t2p2)),
#         dbc.Row(dbc.Col(t2p3)),
#             ]),
# ]

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

## Callback functions
# Navigation
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    # if pathname == '/tab1':
    #     # return tab1
    #     return html.H1('Tab1')
    # elif pathname == '/tab2':
    #     # return tab2
    #     return html.H1('Tab2')
    # else:
    #     return html.H1('Welcome')
    return html.H1(pathname)

# Settings
@app.callback(
    Output('region-select', 'value'),
    Input('region-select-all', 'n_clicks'),
    State('region-select', 'options')
)
def select_all_regions(_, regions):
    return [region for region in regions]

# # Tabs
# @app.callback(
#     Output('t1p1','srcDoc'),
#     Input('region-select', 'value'))
# def update_t1p1(autho):
#     return line_plot_t1(list(autho))
# @app.callback(
#     Output('t2p1','srcDoc'),
#     Input('region-select', 'value'))
# def update_t2p1(autho):
#     return line_plot_t2(list(autho))
# @app.callback(
#     Output('t1p2','srcDoc'),
#     Input('region-select', 'value'))
# def update_t1p2(autho):
#     return plot_bar_sbs_procedure_t1(list(autho))
# @app.callback(
#     Output('t2p2','srcDoc'),
#     Input('region-select', 'value'))
# def update_t2p2(autho):
#     return plot_bar_sbs_procedure_t2(list(autho))
# @app.callback(
#     Output('t1p3','srcDoc'),
#     Input('region-select', 'value'))
# def update_t1p3(autho):
#     return plot_bar_sbs_hospital_t1(list(autho))
# @app.callback(
#     Output('t2p3','srcDoc'),
#     Input('region-select', 'value'))
# def update_t2p3(autho):
#     return plot_bar_sbs_hospital_t2(list(autho))

# # @app.callback(
# #     Output('year-slider', 'children'),
# #     Input('year-slider', 'value'))
# # def update_output(input_value):
# #     return 'Year(s) selected{}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)