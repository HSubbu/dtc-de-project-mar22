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
[link](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/data-description.pdf)

## OUTLINE OF PROPOSED DATA PIPELINE 

Given the requirements in the problem statement , broad solution envisaged is to use GCP tools to pull the data(both historical and daily data ) from API, put the data in a data lake , pull the data and transform using an internal GCP pipeline (Google Data Fusion ) and ingest into tables in Big Query . From the tables in BQ , we can load the data into Google Data Studio to create Dashboards . It is also proposed to run additional quries in BQ (scheduled queries) to create additional tables/views so that the data from these tables can be loaded to Google Data Studio for visualisations as required. To automate the loading of data into data lake , Google Cloud Scheduler can be used to trigger the cloud function . The link to Dashboard can be shared with Management in Health Department for their access. 

## PROJECT DATA PIPELINE DESIGN 

![alt text](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/dtc-de-project.png)

## DATA INGESTION 
The Data ingestion part of pipeline consists of scheduled pulling of data from API (both historical and daily updates) at 1600 hours every day (daily data is expected to be updated every daya around noon EST). A storage bucket has been created in GCS . A Google Cloud Function and Google Cloud Schduler together will pull the data from API and put in GCS Bucket. 

The detailed documentation for data ingestion part is given in this
