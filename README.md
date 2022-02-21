# {Surgical System Visualization Application} (Group F)

**Problem this dashboard hopes to solve**: Through interactive graphical and numeric visualizations, the proposed application will be designed to:  
1) Assess historical and current surgical resource/demand relationships in an effort to proactively secure future health care personal, infrastructure and funding.
2) Support development of the Fraser Health 2022/23 Surgical Funding Proposal for the upcoming BC Ministry of Health Resource Allocation Meeting. 
3) Review the impact of Covid-19 on surgical demand and throughput.   
4) Identify surgical procedures that are exceeding surgical wait-time benchmarks.

## Team Members

- Anqi Li: I like to try new things and want to do something creative :)
- Andrew Nguyen: I am not soft tomatoes!
- Person 3: one sentence about you!
- Person 4: one sentence about you!

## Describe your topic/interest in about 150-200 words

#### Surgical Wait Times
It is well documented that surgical delays are associated with negative medical outcomes. [[1],](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4582239/)[[2],](https://journals.lww.com/spinejournal/Abstract/2019/04010/Immediate_Versus_Delayed_Surgical_Treatment_of.6.aspx)[[3]](https://www.cmaj.ca/content/182/15/1609.short) In an effort to minimize these effects, surgical wait time benchmarks have been established and are monitored across the province of BC for several surgical procedures.[[4],](https://www2.gov.bc.ca/gov/content/health/accessing-health-care/surgical-wait-times/understanding-wait-times/wait-time-targets)[[5],](https://www.cihi.ca/en/wait-time-metadata)[[6]](https://www.waittimealliance.ca/benchmarks/) The dataset accessed for this report was purpose built to facilitate evaluation of surgical demand through wait list and wait time and surgical efficiencies through completed case metrics. 

#### Impact of Covid-19
The Covid-19 Pandemic has been found to have had a profound impact on the health care system.[[7],](https://www.cihi.ca/en/covid-19-resources/impact-of-covid-19-on-canadas-health-care-systems/the-big-picture)[[8],](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0253875)[[9]](https://academic.oup.com/intqhc/article/33/1/mzaa158/6018446?login=true)  Public Health measures in BC have been implemented to maintain healthcare operations with a specific focus on maintaining surgical throughput.  

#### Surgical Efficiency
Improving surgical efficiency and maximizing surgical completion counts has been at the forefront of healthcare discourse in BC for over a decade.[[10],](https://www.doctorsofbc.ca/sites/default/files/enhancingsurgicalcare_web.pdf)[[11]](https://bcpsqc.ca/improve-care/surgery/)  Surgical case completions can be used as a blunt metric for surgical efficiencies.[[12]]need to find references for this...

## About this Dashboard

The app uses six radio buttons to delivery corresponding information for the six health authorities. We designed four tabs to arrange the display of our data and variables. The first tab provides the summarized information to the user, which contains two cards showing the total number of cases and total cases completed, and also the proportion of completed cases by time, from which healthcare administrators can see the change and see if their actions at certain point in time has caused an impact on surgical demand. The second tab shows information about waiting cases, including number of waiting cases by time and by different hospitals and surgical groups to show the distribution of surgical demand. The third tab shows information about completed cases, including number of waiting cases by time and by different hospitals and surgical groups to show and their ability to handle the surgical demands. The fourth tab shows information about waiting time, including average waiting time and waiting time by procedures, which can provide an insight to the healthcare administrators about the procedures that require attention and need more human, infrastructure and financial resources. 

![Tab 1](sketch/Tab1.JPG)
<p align="center">Tab1</p>

![Tab 2](sketch/Tab2.JPG)
<p align="center">Tab2</p>

![Tab 3](sketch/Tab3.JPG)
<p align="center">Tab3</p>

![Tab 4](sketch/Tab4.JPG)
<p align="center">Tab4</p>

## Describe your dataset in about 150-200 words

The proposed application will visualize British Columbia surgical related data contained within the historic 2009 to 2021 and the current 2021/22 BC Surgical Wait Time databases. Data points are collected for all surgical procedures performed in all hospital facilities across the province.  Hospitals are additionally grouped by their respective Health Authorities.  Both datasets contain the number of patients waiting for surgery (waiting), number of completed surgical procedures (completed) and the 50th and 90th percentile surgical wait times in weeks (completed_50th_percentile and completed_90th_percentile, respectively). The data is for elective surgical procedures for patients of all ages and includes scheduled inpatient and day surgery cases. This data does not include unscheduled surgical cases. The data points are aggregated on a quarterly basis. Additional the datasets contain summation data for all procedures, all hospitals and all health authorities. Using this data the proposed app will also visualize new variables for predicted future wait list and surgical completion counts as well as anticipated wait-times (projected_wait_list, projected_completed, projected_wait_time).  Please refer to the accompanying [EDA.ipynb file](link edited EDA) for a more in depth exploration and analysis of the datasets.

## Acknowledgements and references 

