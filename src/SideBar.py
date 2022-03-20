# Sidebar components
title = html.H1(
    'BC Surgical Wait Time Dashboard',
    style = {'color': 'var(--bs-primary)'}
)

nav = dbc.Nav(
    children = [
         dbc.NavLink(
             'Summary',
             style = {'border-radius': '0.4rem 0 0 0.4rem'},
             href = '/summary_tab',
             active = 'exact'
         ),
        dbc.NavLink(
            'Waiting and Completed Cases by Procedure',
            style = {'border-radius': '0.4rem 0 0 0.4rem'},
            href = '/count_tab_proc',
            active = 'exact'
        ),
        dbc.NavLink(
            'Waiting and Completed Cases by Hospital',
            style = {'border-radius': '0.4rem 0 0 0.4rem'},
            href = '/count_tab_hosp',
            active = 'exact'
        ),
         dbc.NavLink(
            'Wait Times by Procedure',
            style = {'border-radius': '0.4rem 0 0 0.4rem'},
            href = '/times_tab_proc',
            active = 'exact'
        ),
        dbc.NavLink(
            'Wait Times, by Hospital',
            style = {'border-radius': '0.4rem 0 0 0.4rem'},
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
        # year_slider,
        # quarter_radio
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