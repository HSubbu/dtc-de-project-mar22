# dtc-de-project-mar22
Data Engineering project for Data Engineering Zoom Camp by Data Talks Club

## PROJECT FRAMEWORK BY DATATALKSCLUB
Build a dashboard with two tiles.

For that, you will need:

Select a dataset that 
* Create a pipeline for processing this dataset and putting it to a datalake
* Create a pipeline for moving the data from the lake to a data warehouse
* Transform the data in the data warehouse: prepare it for the dashboard
* Create a dashboard

## PROBLEM DESCRIPTION

You are hired as consulatant Data Engineer by Florida Health Department. The Management of Health Department would like to monitor the status of COVID 19 across US states on a daily basis . There is a need to identify risk levels across the states on a daily basis in terms of critical metrics and visuals on a dashboard . The Data Engineer may prepare monitoring metrics from the information available in the data. The historic and daily data can be pulled from an API https://apidocs.covidactnow.org using an API key. For the sake of keeping the data pipeline simple only data related to US states have been considered for processing the pipeline. The Department of Health has a billed account in Google Cloud Platform(GCP) and solutions worked out could include open source tools or GCP tools . The pipeline needs to be automated for daily updation of dashboard. 

## DATA DESCRIPTION

The data is to be pulled from an API of website https://apidocs.covidactnow.org using an API KEY. The details of dataset is available in following document
[a link]()

## PROJECT DATA PIPELINE DESIGN 

![alt text](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/dtc-de-project.png)
