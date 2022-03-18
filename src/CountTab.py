## Plotting 
# Waiting and completed case count line plot
def line_plot_tc(autho=):
    #all_by_autho = df[(df['procedure']=='All Procedures') & (df['hospital']=='All Facilities') & (df.health_authority.isin(autho))]
    #all_by_autho = just call correct df that is loaded on app.py 
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


# Waiting and completed case count side by side bar plot by procedures
def plot_bar_sbs_procedure_tc(autho=["Fraser"]):
    #not calling count but specific csv based on autho
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

# Waiting and completed case count side by side bar plot by hospital
def plot_bar_sbs_hospital_tc(autho=["Fraser"]):
    #not calling count but specific csv based on autho
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


# CountTab-plot1: waiting & completed cases by time
tcp1=html.Iframe(
    id="tcp1",
    srcDoc=line_plot_tc(),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# CountTab-plot2: waiting and completed cases by procedure
tcp2=html.Iframe(
    id="tcp2",
    srcDoc=plot_bar_sbs_procedure_tc(autho=["Fraser"]),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# CountTab-plot3: waiting and completed cases by hospital
tcp3=html.Iframe(
    id="tcp3",
    srcDoc=plot_bar_sbs_hospital_t1(autho=["Fraser"]),
    style={'border-width': '0', 'width': '100%', 'height': '400px'}
)

# Waiting and completed case Layout Components
proc = [
    html.Div([
        dbc.Row(dbc.Col(tcp1)),
        dbc.Row(dbc.Col(tcp2)),
            ]),
    ]

hosp = [
    html.Div([
        dbc.Row(dbc.Col(tcp1)),
        dbc.Row(dbc.Col(tcp3)),
            ]),
    ]
