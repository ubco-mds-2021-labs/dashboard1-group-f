from dash import Dash, dcc, html
#from pydoc import classname
#from dash.dependencies import Input, Output, State
#from pathlib import Path

import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd
import numpy as np

# Wait times line plot
def line_plot_tt(df):
    #autho = autho[0]
    all_by_autho = df
    data=all_by_autho.groupby(['Y_Q'])[["wait_time_50","wait_time_90"]].mean().reset_index().melt('Y_Q')
    chart=alt.Chart(data).mark_line().encode(
        x=alt.X('Y_Q', title='Year & Quarter'),
        y=alt.Y('value',title='Wait Time (weeks'),
        tooltip=['value'],
        color='variable'
    ).properties(
        title="50th and 90th Percentile Waiting Times",
        width=920,
        height=280)
    return chart.interactive().to_html()


# Wait times side by side bar plot for procedures
def plot_bar_sbs_procedure_tt(df):
    #autho = autho[0]
    subdata = df
    top=subdata.groupby(["procedure"])[["wait_time_50"]].mean().reset_index().sort_values(by=['wait_time_50'], ascending=False).head(20)["procedure"].tolist()
    subdata_top=subdata[subdata["procedure"].isin(top)]
    chart1 = alt.Chart(subdata_top).mark_tick().encode(
            x=alt.X('mean(wait_time_50):Q',title="Wait Time (weeks)"),
            y=alt.Y("procedure", sort='-x',title="Procedure"),
            color=alt.Color('year')
        ).properties(
            title="Waiting Times for 50 percent of Cases by Procedure",
            width=200,
            height=300
        ).interactive()
    top2=subdata.groupby(["procedure"])[["wait_time_90"]].mean().reset_index().sort_values(by=['wait_time_90'], ascending=False).head(20)["procedure"].tolist()
    subdata_top2=subdata[subdata["procedure"].isin(top2)]
    chart2 = alt.Chart(subdata_top2).mark_tick().encode(
            x=alt.X('mean(wait_time_90):Q',title="Wait Time (weeks)"),
            y=alt.Y("procedure", sort='-x',title="Procedure"),
            color=alt.Color('year')
        ).properties(
            title="Waiting Times for 90 percent of Cases by Procedure",
            width=200,
            height=300
        ).interactive()
    chart_sbs=alt.hconcat(chart1,chart2).configure_axis(
        labelFontSize=10,
        titleFontSize=10
    ).to_html()
    return chart_sbs

# Wait times side by side bar plot for hospital
def plot_bar_sbs_hospital_tt(df):
    #autho = autho[0]
    subdata = df
    top=subdata.groupby(["hospital"])[["wait_time_50"]].mean().reset_index().sort_values(by='hospital').head(20)["hospital"].tolist()
    subdata_top=subdata[subdata["hospital"].isin(top)]
    chart1 = alt.Chart(subdata_top).mark_tick().encode(
            x=alt.X('mean(wait_time_50):Q',title="Wait Time (weeks)"),
            y=alt.Y("hospital", sort='-x',title="Hospital"),
            color=alt.Color('year')
        ).properties(
            title="Waiting Times for 50 percent of Cases by Hospitals",
            width=200,
            height=300
        ).interactive()
    top2=subdata.groupby(["hospital"])[["wait_time_90"]].mean().reset_index().sort_values(by='hospital').head(20)["hospital"].tolist()
    subdata_top2=subdata[subdata["hospital"].isin(top2)]
    chart2 = alt.Chart(subdata_top2).mark_tick().encode(
            x=alt.X('mean(wait_time_90):Q',title="Wait Time (weeks)"),
            y=alt.Y("hospital", sort='-x',title="Hospital"),
            color=alt.Color('year')
        ).properties(
            title="Waiting Times for 90 percent of Cases by Hospitals",
            width=200,
            height=300
        ).interactive()
    chart_sbs=alt.hconcat(chart1,chart2).configure_axis(
        labelFontSize=10,
        titleFontSize=10
    ).to_html()
    return chart_sbs

# TimesTab-plot1: wait times (50th and 90th percentile) by time
ttp1=html.Iframe(
    id="ttp1",
    srcDoc=None,
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# TimesTab-plot2: wait times (50th and 90th percentile) by procedure
ttp2=html.Iframe(
    id="ttp2",
    srcDoc=None,
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# TimesTab-plot3: wait times (50th and 90th percentile) by hospital
ttp3=html.Iframe(
    id="ttp3",
    srcDoc=None,
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# Wait Times Layout Components
proc = [
    html.Div([
        dbc.Row([
            dbc.Col(ttp1, width=13)]),
            dbc.Row(dbc.Col(ttp2)),
            ]),
]

hosp = [
    html.Div([
        dbc.Row([
            dbc.Col(ttp1, width=13)]),
            dbc.Row(dbc.Col(ttp3)),
            ]),
]
