from dash import Dash, dcc, html
from pydoc import classname
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from pathlib import Path

import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd
import numpy as np
from app import region_df as region_df
## Plotting 
# Waiting and completed case count line plot
def line_plot_tc(all_by_autho):
    """
    Plot a line plot to show the count of the waiting and completed cases for a certain region by time.
    
    Parameters
    ----------
    autho : str
        The string of the region name.

    Returns
    -------
    html
        The returned plot which converted to html. 
        
    Examples
    --------
    >>> line_plot_tc(autho="Fraser")
    ttchart.interactive().to_html()
    """
    # all_by_autho = region_df(autho,alldata=True)
    data=all_by_autho.groupby(['Y_Q'])[["waiting","completed"]].sum().reset_index().melt('Y_Q')
    chart=alt.Chart(data).mark_line().encode(
        x=alt.X('Y_Q', title='Year & Quarter'),
        y=alt.Y('value',title='Number of Cases'),
        tooltip=['value'],
        color='variable'
    ).properties(
        title="Number of Waiting & Completed Cases by Time",
        width=920,
        height=280)
    tt=chart.mark_line(strokeWidth=30, opacity=0.01)
    ttchart=chart+tt
    return ttchart.interactive().to_html()

# Waiting and completed case count side by side bar plot by procedures
def plot_bar_sbs_procedure_tc(subdata):
    """
    Plot a two bar plots to show the count of the waiting and completed cases by procedures for a certain region in each year.
    One for the waiting cases, and the other is for the completed cases. 

    Parameters
    ----------
    autho : str
        The string of the region name.

    Returns
    -------
    html
        The returned bar plots that are converted to html. 
        
    Examples
    --------
    >>> plot_bar_sbs_procedure_tc(autho="Fraser")
    chart_sbs
    """
    # subdata=region_df(autho)
    top=subdata.groupby(["procedure"])[["waiting"]].sum().reset_index().sort_values(by=['waiting'], ascending=False).head(20)["procedure"].tolist()
    subdata_top=subdata[subdata["procedure"].isin(top)]
    chart1 = alt.Chart(subdata_top).mark_bar().encode(
            x=alt.X('sum(waiting):Q',title="Total Waiting Cases"),
            y=alt.Y("procedure", sort='-x', title = ""),
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
            y=alt.Y("procedure", sort='-x', title = ""),
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

# Waiting and completed case count side by side bar plot by hospital
def plot_bar_sbs_hospital_tc(subdata):
    """
    Plot a two bar plots to show the count of the waiting and completed cases by hospital for a certain region in each year.
    One for the waiting cases, and the other is for the completed cases. 

    Parameters
    ----------
    autho : str
        The string of the region name.

    Returns
    -------
    html
        The returned bar plots that are converted to html. 
        
    Examples
    --------
    >>> plot_bar_sbs_hospital_tc(autho="Fraser")
    chart_sbs
    """
    # subdata=region_df(autho)
    top=subdata.groupby(["hospital"])[["waiting"]].sum().reset_index().sort_values(by=['waiting'], ascending=False).head(20)["hospital"].tolist()
    subdata_top=subdata[subdata["hospital"].isin(top)]
    chart1 = alt.Chart(subdata_top).mark_bar().encode(
            x=alt.X('sum(waiting):Q',title="Total Waiting Cases"),
            y=alt.Y("hospital", sort='-x', title = ""),
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
            y=alt.Y("hospital", sort='-x', title = ""),
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


# CountTab-plot1: waiting & completed cases by time
tcp1=html.Iframe(
    id="tcp1",
    # srcDoc=line_plot_tc(),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# CountTab-plot2: waiting and completed cases by procedure
tcp2=html.Iframe(
    id="tcp2",
    # srcDoc=plot_bar_sbs_procedure_tc(autho="All"),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# CountTab-plot3: waiting and completed cases by hospital
tcp3=html.Iframe(
    id="tcp3",
    # srcDoc=plot_bar_sbs_hospital_tc(autho="All"),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# Waiting and completed case Layout Components
proc = [
    html.Div([
        html.H5('Research Question: During the first quarter of 2020, how many procedures were completed in the Interior Health Region?'),
        html.H6('Answer: 6474  Hint: Tooltip hover over blue line'),
        dbc.Row(dbc.Col(tcp1)),
        dbc.Row(dbc.Col(tcp2)),
            ]),
    ]

hosp = [
    html.Div([
        html.H5('Research Question: In Fraser Health Authority, which 3 hospitals consistantly complete the most number of surgeries?'),
        html.H6('Answer: Surrey Memorial, Burnaby, and Chilliwack General Hospitals'),
        dbc.Row(dbc.Col(tcp1)),
        dbc.Row(dbc.Col(tcp3)),
            ]),
    ]
