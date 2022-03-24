from dash import dcc, html

# Summary page markdown content

markdown_text_1 = '''
During these pandemic years, when medical resources are stretched beyond their capacity, supporting medical system decision makers as they look to improve system efficiencies and secure financial and non-monetary resources is more important than ever.
'''
markdown_text_2 = '''
<- The sidebar contains a **_ dropdown menu_** to select a specific health authority.  The default is set to "all" Health Authorities.

<- **_Four tabs_** are also available to allow exploration of the waiting and completed case *counts* and the surgical wait *times* (in weeks), by *hospital* and by *procedure*.

'''
markdown_text_3 = '''

#### Data Information
Data is sourced from: [British Columbia Open Data Catalogue](https://catalogue.data.gov.bc.ca/dataset/bc-surgical-wait-times/resource/f294562c-a6fd-4d7f-8f99-c51c91891c67)
Data is collated and published every health authority fiscal quarter.

#### Surgical Efficiency (Waiting vs Completed Cases)
Improving surgical efficiency and maximizing surgical completion counts has been at the forefront of healthcare discourse in BC for over a decade.[[12],](https://www.doctorsofbc.ca/sites/default/files/enhancingsurgicalcare_web.pdf)[[13]](https://bcpsqc.ca/improve-care/surgery/)  Surgical case completions has been used as a blunt metric for surgical efficiencies. [[14]](https://www.researchgate.net/publication/347888026_Operating_Room_Efficiency_measurement_made_simple_by_a_single_metric) A thourough understanding of the current numbers of waiting and completed cases is an essential starting point for any systems based decisions.  This dashboard was developed to assist in this regard.

#### Surgical Wait Times
It is well documented that surgical delays are associated with negative medical outcomes. [[1],](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4582239/)[[2],](https://journals.lww.com/spinejournal/Abstract/2019/04010/Immediate_Versus_Delayed_Surgical_Treatment_of.6.aspx)[[3]](https://www.cmaj.ca/content/182/15/1609.short) In an effort to minimize these effects, surgical wait time benchmarks have been established and are monitored across the province of BC for several surgical procedures.[[4],](https://www2.gov.bc.ca/gov/content/health/accessing-health-care/surgical-wait-times/understanding-wait-times/wait-time-targets)[[5],](https://www.cihi.ca/en/wait-time-metadata)[[6]](https://www.waittimealliance.ca/benchmarks/) The dataset accessed for this report was purpose built to facilitate evaluation of surgical demand by monitoring wait lists and wait times.

#### Impact of Covid-19
The Covid-19 Pandemic has been found to have had a profound impact on the health care system.[[7],](https://www.cihi.ca/en/covid-19-resources/impact-of-covid-19-on-canadas-health-care-systems/the-big-picture)[[8],](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0253875)[[9]](https://academic.oup.com/intqhc/article/33/1/mzaa158/6018446?login=true)  Public Health measures in BC have been implemented to maintain healthcare operations with a continued focus on surgical throughtput. Despite these efforts, surgical delays and cancellations have occurred across the province periodically since early 2020. [[10]](https://bc.ctvnews.ca/staffing-crisis-forces-reduced-hours-at-b-c-hospitals-cancelled-surgeries-1.5746178), [[11]](https://www2.gov.bc.ca/assets/gov/health/conducting-health-research/surgical-renewal-plan.pdf) Understanding the degree of these delays is important for administrators and all British Columbians.

'''
## Summary page layout
intro = (
    html.H1(
        children ='Welcome!', 
        style={'textAlign': 'center', 'color': 'var(--bs-primary)'}
        ),
    html.Div([
        dcc.Markdown(
            children=markdown_text_1,
            style={'color': 'black'}
            )
    ]),
    html.H1(
        children ='Important Features', 
        style={'textAlign': 'center', 'color': 'var(--bs-primary)'}
        ),
    html.Div([
        dcc.Markdown(
            children=markdown_text_2,
            style={'color': 'black'}
            )
    ]),
    html.H1(
        children ='Background Information', 
        style={'textAlign': 'center', 'color': 'var(--bs-primary)'}
        ),
            html.Div([
        dcc.Markdown(
            children=markdown_text_3,
            style={'color': 'black'}
            )
            ])
)
# html.DIV(
#     children='',
#     style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }
# )


# written <- div(
#     h1(
# 	'Welcome',
# 	style = list(
#         'color' = 'var(--bs-primary)',
#         'textAlign' = 'center'
#         )
#         )
# ),
#      h3(
#          'Surgical systems are a fundamental part of an effective health care system.'
#          ),
#      h4(
#          'Data related to surgical system functioning is collected, synthesized and published in the BC Data Catalogue and displayed here by total values across time and by hospital and procedure from 2009 to the most recent fiscal quarter.  There are two main types of information contained within two tabs.'
#          ),
#      h4(
#          'Data for the counts of waiting and completed surgical cases is presented in the first tab to the left.  This data represents the counts of the number of patients waiting for surgery and the counts of the number of surgeries completed within each fiscal quarter. This tab is important for understanding the demands and productivity of the surgical system'
#          ),
#      h4(
#          'Data for the average wait times for completed surgical cases is presented in the second tab to the left.  This data represent the time, in weeks, patients had to wait before their surgery was completed.  For all the surgeries completed within each quarter, the time 50% of patients had to wait is represented by the 50th percentile data and the number of weeks 90% of patients had to wait is represented by the 90th percentile data.  This tab is important for understanding how long patients have to wait before they can get surgery.'
#          ),
#      h4(
#          'Individual health authoritise can be selected from the dropdown menu.'
#      )

# )