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
[link](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/dtc-de-project.png)

## OUTLINE OF PROPOSED DATA PIPELINE 

Given the requirements in the problem statement , broad solution envisaged is to use GCP tools to pull the data(both historical and daily data ) from API, put the data in a data lake , pull the data and transform using an internal GCP pipeline (Google Data Fusion ) and ingest into tables in Big Query . From the tables in BQ , we can load the data into Google Data Studio to create Dashboards . It is also proposed to run additional quries in BQ (scheduled queries) to create additional tables/views so that the data from these tables can be loaded to Google Data Studio for visualisations as required. To automate the loading of data into data lake , Google Cloud Scheduler can be used to trigger the cloud function . The link to Dashboard can be shared with Management in Health Department for their access. 

## PROJECT DATA PIPELINE DESIGN 

![alt text](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/dtc-de-project.png)

## DATA INGESTION 
The Data ingestion part of pipeline consists of scheduled pulling of COVID19 data from API (both historical and daily updates) at 1400 hours every day (daily data is expected to be updated every daya around noon EST). A storage bucket has been created in GCS . A Google Cloud Function and Google Cloud Schduler together will pull the data from API and put in GCS Bucket. A python script has been used in Google Cloud Function .  The historic and current data has also been merged to ingest a combined data (using the python script in GCF)into the bucket for further transformation and processing. The python script used in Cloud Function is https://github.com/HSubbu/dtc-de-project-mar22/blob/main/ingest_data.txt 

The detailed documentation for data ingestion part is given in this https://github.com/HSubbu/dtc-de-project-mar22/blob/main/data-ingestion.pdf

Creating GCS bucket video link https://loom.com/share/55355ddbd91b4cf980e8a9584117f03c 

Creating a service account https://www.loom.com/share/a832ec5c8e364261a569fcd2d99ffdf9

Create a cloud Function for data ingestion https://www.loom.com/share/9ff420fbb7d941fb81a58d7bce8eed57

Local testing of Cloud Function https://www.loom.com/share/e9b62bf6551d4147b89c36348c3808a5

Creata cloud scheduler https://www.loom.com/share/e06f13c657714eb588c7512790dd2652

## ETL PIPELINE 
The data in GCS bucket needs to be further loaded into DWH after minimum data transformation. GCP tool called DATA FUSION was adopted for the ETL process. The Data Fusion has UI which can pull the data from GCS and carry our basic transformation and load data as BQ table . In addition, these pipeline execution can be scheduled to run at specified intervals everyday. I am ingesting the data at 1400 hours everyday. Hence the pileine is scheduled to run at 1500 hours everyday. There are two data pipelines running simultaeneously , once for the current data and one for historic data. 

Detailed documentation of ETL pipeline is given ..

## DASHBOARD
The tables in BQ has been used as input data to GOOGLE DATA STUDIO to create Dashboards. The Dashboards presents two pages/tiles . One for current data and once giving historical perspective(since the time pandemic started) . The dashboards get updated when the tables get updated by the pipeline. 

The detailed documentation for the Dashboard creatiion is ..


## CONCLUSION

## AREAS FOR IMPROVEMENT

This project is academic in nature and is an attempt to put into practice learnings from DataTalksClub DE Zoomcamp. There is scope to improve the project to achieve improved performance . Following areas are identified as areas of improvement :

  (a) The cost optimatization of GCP platform with current dataflow plipeline ( I havent worked much towards cost optimization and identify areas for improvement)
  
  (b) Try out more transformation in ETL to achieve better data output 
  
  (c) Identify more metrics (critical ones ) for incorporation in dashboard
  
  (d) CI/CD pipeline of testing (I have manually tested the pipeline , automated testing is way to go !)

## REFERNCES

Using Cloud Function for Data Ingstionhttps://www.ternarydata.com/news/use-python-and-google-cloud-to-schedule-a-file-download-and-load-into-bigquery-3p3aw

Using Data Fusion for ETL. https://codelabs.developers.google.com/codelabs/batch-csv-cdf-bq#0

Using Data Fusion for ETL https://www.youtube.com/watch?v=1QhJDsYQTfM 

Using Data Fusion for ETL with Join Current data and historic data https://blog.pythian.com/join-group-by-and-aggregate-in-cloud-data-fusion/

Using Data Studio for visualisation https://codelabs.developers.google.com/codelabs/bigquery-data-studio#2

Building dashboards in Data Studio https://datadrivenlabs.io/blog/how-to-build-a-data-studio-dashboard/
