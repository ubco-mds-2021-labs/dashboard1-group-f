## MoKeAn^2 Data Consultancy

#### Title: Surgical System Visualization App
#### Application Completion Date: March 23, 2022
#### Data Sources: [BC Surgical Wait Times -2009_2021 Quarterly Surgical Wait Times & 2021_2022 Quarterly Surgical Wait Times]("https://catalogue.data.gov.bc.ca/dataset/bc-surgical-wait-times/resource/f294562c-a6fd-4d7f-8f99-c51c91891c67") 
#### Requestor: Lee Charbonder, Lead- Surgical Services Fraser Health Authority (newly appointed, prior Lead Emergency Services Virginia Medical services, Seattle USA))
#### Application Purpose: 
Through interactive graphical and numeric visualizations, the proposed application will be designed to:  
1) Assess historical and current surgical resource/demand relationships in an effort to proactively secure future health care personal, infrastructure and funding.
2) Support development of the Fraser Health 2022/23 Surgical Funding Proposal for the upcoming BC Ministry of Health Resource Allocation Meeting. 
3) Review the impact of Covid-19 on surgical demand and throughput.   
4) Identify surgical procedures that are exceeding surgical wait-time benchmarks.
(We pick only two or three of these, although I think we can build a dashboard to answer all these and even many more)

### *Background Information*
#### Surgical Wait Times
It is well documented that surgical delays are associated with negative medical outcomes. [1]("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4582239/") [2]("https://journals.lww.com/spinejournal/Abstract/2019/04010/Immediate_Versus_Delayed_Surgical_Treatment_of.6.aspx") [3]("https://www.cmaj.ca/content/182/15/1609.short") In an effort to minimize these effects, surgical wait time benchmarks have been established and are monitored across the province of BC for several surgical procedures. [4]("https://www2.gov.bc.ca/gov/content/health/accessing-health-care/surgical-wait-times/understanding-wait-times/wait-time-targets") [5]("https://www.cihi.ca/en/wait-time-metadata") [5]("https://www.waittimealliance.ca/benchmarks/") The dataset accessed for this report was purpose built to facilitate evaluation of surgical demand through wait list and wait time and surgical efficiencies through completed case metrics. 

#### Impact of Covid-19
The Covid-19 Pandemic has been found to have had a profound impact on the health care system. [6]("https://www.cihi.ca/en/covid-19-resources/impact-of-covid-19-on-canadas-health-care-systems/the-big-picture") [7]("https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0253875") [8]("https://academic.oup.com/intqhc/article/33/1/mzaa158/6018446?login=true")  Public Health measures in BC have been implemented to maintain healthcare operations with a specific focus on maintaining surgical throughput.  

#### Surgical Efficiency
Improving surgical efficiency and maximizing surgical completion counts has been at the forefront of healthcare discourse in BC for over a decade. [9](""https://www.doctorsofbc.ca/sites/default/files/enhancingsurgicalcare_web.pdf) 
[10]("https://bcpsqc.ca/improve-care/surgery/").  Surgical case completions can be used as a blunt metric for surgical efficiencies. [11]need to find references for this...

### *Data Source*
The proposed application will visualize British Columbia surgical related data contained within the historic 2009 to 2021 and the current 2021/22 BC Surgical Wait Time databases. Data points are collected for all surgical procedures performed in all hospital facilities across the province.  Hospitals are additionally grouped by their respective Health Authorities.  Both datasets contain the number of patients waiting for surgery (waiting), number of completed surgical procedures (completed) and the 50th and 90th percentile surgical wait times in weeks (completed_50th_percentile and completed_90th_percentile, respectively)The data is for elective surgical procedures for patients of all ages and includes scheduled inpatient and day surgery cases. This data does not include unscheduled surgical cases. The data points are aggregated on a quarterly basis. Additional the datasets contain summation data for all procedures, all hospitals and all health authorities. Using this data the proposed app will also visualize new variables for predicted future wait list and surgical completion counts as well as anticipated wait-times (projected_wait_list, projected_completed, projected_wait_time).  Please refer to the accompanying [EDA.ipynb file](link edited EDA) for a more in depth exploration and analysis of the datasets.

### *Application Purpose and Usage*
The proposed app will feature an interactive graphical user interface to assist the Fraser Health Surgical Lead and other health care administrators as they [navigate] the surgical data in an effort to [identify] and [interpret] surgical trends, to efficiently [communicate] regional demands and requirements to upstream government and healthcare decision makers and to appropriately [plan] and [administer] surgical system resources. The apps ability to visualize data from the provincial down to the individual hospital levels will assist healthcare decision makers to [understand] the data directly related to their portfolios in relation to the entire surgical system.  


### Application Features
The app uses six tabs to delivery corresponding information for the six health authorities. Each tab page consists of three sections. The first section provides the summarized information contained in two cards showing the total number of cases and total cases completed. The second section displays critical variables by time in the form of two plots. Healthcare administrators can see the change in proportion of completed cases and average wait time by time to see if their actions at certain point in time have impacted the surgical process. The third section visualizes surgical demand for each health authority and hospital.  These sunburst plots and their associated range slider portray the hospital and authorities ability to handle surgical demands over time. TIn combination these pages will provide healthcare administrators insights about outlier hospitals and surgical procedures that may require additional human, infrastructure and financial resources.


### Application Mock-Up

INSERT Anqi's sketch here.