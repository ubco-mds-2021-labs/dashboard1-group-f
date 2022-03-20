from dash import html, dcc

import dash_bootstrap_components as dbc

title = html.H1(
    'BC Surgical Wait Times',
    style = {
        'color': 'var(--bs-primary)',
        'padding-left': '1rem'
    }
)

nav = dbc.Nav(
    children = [
         dbc.NavLink(
             'Summary',
             style = {'border-radius': '0 0.4rem 0.4rem 0'},
             href = '/summary_tab',
             active = 'exact'
         ),
        dbc.NavLink(
            'Waiting and Completed Cases by Procedure',
            style = {'border-radius': '0 0.4rem 0.4rem 0'},
            href = '/count_tab_proc',
            active = 'exact'
        ),
        dbc.NavLink(
            'Waiting and Completed Cases by Hospital',
            style = {'border-radius': '0 0.4rem 0.4rem 0'},
            href = '/count_tab_hosp',
            active = 'exact'
        ),
         dbc.NavLink(
            'Wait Times by Procedure',
            style = {'border-radius': '0 0.4rem 0.4rem 0'},
            href = '/times_tab_proc',
            active = 'exact'
        ),
        dbc.NavLink(
            'Wait Times by Hospital',
            style = {'border-radius': '0 0.4rem 0.4rem 0'},
            href = '/times_tab_hosp',
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
            options = None,
            style = {'width': '100%'},
            className = 'dash-bootstrap',
            id = 'region-select'
        )
    ],
    style = {'padding-left': '1rem'}
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
        # year_slider,
        # quarter_radio
    ],
    style = {
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'width': '23rem',
        'height': '100%',
        'padding': '2rem 1rem 2rem 0'
    },
    className = 'bg-light'
)