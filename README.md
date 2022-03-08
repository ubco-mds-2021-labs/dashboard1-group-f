# Surgical System Visualization Application (Group F)

***Support British Columbia's surgical system and make it better for everyone through data visualization.***

* Deloyed badge with link 

## Welcome to our project!

Warmest welcome! :tada::tada::tada: Accueil chaleureux! :tada::tada::tada:

Thanks for visiting the Surgical System Visualization Application app project repository.

This document (README.md) is designed to give you overall information about the project. Please click to one of the sections below to jump to the content you want or simply scroll down to find out more. :blush:

## Table of contents
* [What is Surgical System Visualization Application? (And why Surgical System Visualization Application?)](#what-is-surgical-system-visualization-application-and-why)
* [Who are we?](#who-are-we)
* [About this Dashboard](#about-this-dashboard)
* [Describe the dataset](#describe-the-dataset)
* [Interested to contribute to our project?](#are-you-a-developer-and-interested-to-contribute-to-our-project)
* [Contact us](#contact-us)
* [Acknowledgements and references](#acknowledgements-and-references)

## What is Surgical System Visualization Application and why?

Recognizing the importance of surgical wait times to everyone, especially those with underlying medical conditions, even a day earlier can save a life. Moreover, during these pandemic years, when medical resources are stretched beyond their capacity, the earlier the surgeries that those with serious life-threatening conditions are scheduled, the more lives we can save in our community. Following are the problems we are facing and the solutions our project proposes:

### The problem

#### Surgical Wait Times
It is well documented that surgical delays are associated with negative medical outcomes. [[1],](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4582239/)[[2],](https://journals.lww.com/spinejournal/Abstract/2019/04010/Immediate_Versus_Delayed_Surgical_Treatment_of.6.aspx)[[3]](https://www.cmaj.ca/content/182/15/1609.short) In an effort to minimize these effects, surgical wait time benchmarks have been established and are monitored across the province of BC for several surgical procedures.[[4],](https://www2.gov.bc.ca/gov/content/health/accessing-health-care/surgical-wait-times/understanding-wait-times/wait-time-targets)[[5],](https://www.cihi.ca/en/wait-time-metadata)[[6]](https://www.waittimealliance.ca/benchmarks/) The dataset accessed for this report was purpose built to facilitate evaluation of surgical demand by monitoring wait lists and wait times and surgical efficiencies by tracking completed surgical cases.

#### Impact of Covid-19
The Covid-19 Pandemic has been found to have had a profound impact on the health care system.[[7],](https://www.cihi.ca/en/covid-19-resources/impact-of-covid-19-on-canadas-health-care-systems/the-big-picture)[[8],](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0253875)[[9]](https://academic.oup.com/intqhc/article/33/1/mzaa158/6018446?login=true)  Public Health measures in BC have been implemented to maintain healthcare operations with a continued focus on surgical throughtput. Despite these efforts, surgical delays and cancellations have occurred across the province periodically since early 2020. [[10]](https://bc.ctvnews.ca/staffing-crisis-forces-reduced-hours-at-b-c-hospitals-cancelled-surgeries-1.5746178), [[11]](https://www2.gov.bc.ca/assets/gov/health/conducting-health-research/surgical-renewal-plan.pdf) 

#### Surgical Efficiency
Improving surgical efficiency and maximizing surgical completion counts has been at the forefront of healthcare discourse in BC for over a decade.[[12],](https://www.doctorsofbc.ca/sites/default/files/enhancingsurgicalcare_web.pdf)[[13]](https://bcpsqc.ca/improve-care/surgery/)  Surgical case completions has been used as a blunt metric for surgical efficiencies. [[14]](https://www.researchgate.net/publication/347888026_Operating_Room_Efficiency_measurement_made_simple_by_a_single_metric)

### The solution

**Problem this dashboard hopes to solve**: Through interactive graphical and numeric visualizations, the proposed application will be designed to:  
1) Assess historical and current surgical resource/demand relationships in an effort to proactively secure future health care personal, infrastructure and funding.
2) Support development of the Fraser Health 2022/23 Surgical Funding Proposal for the upcoming BC Ministry of Health Resource Allocation Meeting. 
3) Review the impact of Covid-19 on surgical demand and throughput.   
4) Identify surgical procedures within the Fraser Health Authority that are exceeding surgical wait-time benchmarks.

## Who are we?

We are a group of 4 students - [Anqi Li](https://github.com/anqiubc), [Andrew Nguyen](https://github.com/AndrewNg1891), [Kevin Rardford](https://github.com/kradford7) and [Monica Penner](https://github.com/Energix11) - in the Master of Data Science program at [UBC Okanagan](https://ok.ubc.ca/), class of 2021-2022, working on this project as a milestone for one of our courses.

### Team Members

- Anqi Li: I like to try new things and want to do something creative :)
- Andrew Nguyen: I never give up.
- Monica Penner: My current-self despises working out but I still exercise because I know my future-self will be grateful.
- Kevin Radford: I'm a good problem solver.

## About this Dashboard

The app uses six radio buttons to delivery corresponding information for the six health authorities. We designed two tabs to display of our data and variables. The first tab provides summarized information, which contains two cards showing the total number of waiting and completed cases, and also the proportion of completed cases by time. This tab would help healthcare administrators visualize changes and see if their actions at certain point is associated with changes in surgical demand. The second tab shows information about waiting cases, including number of waiting cases by time, by different hospitals and by surgical groups.
| | |
|:-------------------------:|:------------------------:|
![Tab 1](docs/sketch/Tab1.JPG) | ![Tab 2](docs/sketch/Tab2.JPG)
![Tab 3](docs/sketch/Tab3.JPG) | ![Tab 3](docs/sketch/Tab4.JPG)

## Describe the dataset

The proposed application will visualize British Columbia surgical related data contained within the historic 2009 to 2021 and the current 2021/22 BC Surgical Wait Time databases. Data points are collected for all surgical procedures performed in all hospital facilities across the province.  Hospitals are additionally grouped by their respective Health Authorities.  Both datasets contain the number of patients waiting for surgery (waiting), number of completed surgical procedures (completed) and the 50th and 90th percentile surgical wait times in weeks (completed_50th_percentile and completed_90th_percentile, respectively). The data is for elective surgical procedures for patients of all ages and includes scheduled inpatient and day surgery cases. This data does not include unscheduled surgical cases. The data points are aggregated on a quarterly basis. Additionally the datasets contain summation data for all procedures, all hospitals and all health authorities. Using this data, the proposed app will also visualize new variables for predicted future wait list and surgical completion counts as well as anticipated wait-times (projected_wait_list, projected_completed, projected_wait_time).  Please refer to the accompanying [EDA.ipynb](https://github.com/ubco-mds-2021-labs/dashboard1-group-f/blob/main/EDA.ipynb) for a more in depth exploration and analysis of the datasets.

## Are you a developer and interested to contribute to our project?

Our primary goal is to support BC surgical system and while the app is aimed at BC administrators. Recognizing that for the community, your contributions to us are very important. If you would like to contribute to this project and make it better, your help is extremely welcome. By supporting the professional development of any and all of our contributors, we're thrilled to patch another hole in the leaky pipeline. This is a fantastic chance for you if you want to learn to code, collaborate with others, gain experience writing grant applications, or apply your abilities to the digital arena. If you think you can help in any part of this project please feel free to send us a pull request. **How to make a clean pull request** please refer to the steps below.

Please keep in mind that maintaining a good and supportive environment for everyone who wishes to join is also important to us. When you join us, we expect you to adhere to our [code of conduct](CODE_OF_CONDUCT.md).

### How to make a clean pull request

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `develop` if it exists, else from `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `develop` branch if there is one, else go for `master`!
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete your extra branch(es).

### Installation instruction

Package dependencies can be installed using pip or conda. Make sure you have pip or conda using this [Instruction Guidlines](https://ubc-mds.github.io/resources_pages/installation_instructions/). In order to install this dashboard app and run in your local computer, please follow these steps:


1.Open a terminal in your local computer, navigate to a location you desired using `cd path` and clone our project from this Github repository using command:


    git clone https://github.com/ubco-mds-2021-labs/dashboard1-group-f.git


2.In the terminal, navigate to the project directory using `cd path` and run the following command, please note if there is any package dependency missing please install using `pip install package_name`:


    pip app.py
    
    
3.Copy the link from the terminal `localhost` and enter to your web browser to view the dash app.


## Contact us

We'd love to hear from you if you have a problem or a suggestion for improvement; just [open an issue](../../issues) on this github repository and we'll take care of it straight away.

## We are very thankful for any of your contributions to this project!

## Acknowledgements and references 

