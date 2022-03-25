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

You are hired as consulatant Data Engineer by Florida Health Department. The Management of Health Department would like to monitor the status of COVID 19 across US states on a daily basis with special emphasis on state of Florida. There is a need to identify risk levels across the states on a daily basis in terms of critical metrics and visuals on a dashboard . The Data Engineer may prepare monitoring metrics from the information available in the data. The historic and daily data can be pulled from an API https://apidocs.covidactnow.org using an API key. For the sake of keeping the data pipeline simple only data related to US states have been considered for processing the pipeline. The Department of Health has a billed account in Google Cloud Platform(GCP) and solutions worked out could include either open source tools or GCP tools . The pipeline needs to be automated for daily updation of dashboard. 

## DATA DESCRIPTION

The data is to be pulled from an API of website https://apidocs.covidactnow.org using an API KEY. The details of dataset is available in following document
[link](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/dtc-de-project.png)

## OUTLINE OF PROPOSED DATA PIPELINE 

Given the requirements in the problem statement , broad solution envisaged is to use GCP tools to pull the data(both historical and daily data ) from API, put the data in a data lake , extract the data and transform using an internal GCP pipeline (Google Data Fusion) and ingest into tables in Big Query . From the tables in BQ , we can load the data into Google Data Studio to create Dashboards . To automate the loading of data into data lake , Google Cloud Scheduler can be used to trigger the cloud function which will contain a python script to ingest data from URL to GCS bucket (data lake). The python script will also merge current data and historic data to provide a second combined data . The current data will feed one tile of Dashboard and combined data will be input data for second tile. The link to the Dashboard can be shared with Management in Health Department for their access. 

## PROJECT DATA PIPELINE DESIGN 

![alt text](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/dtc-de-project.png)

## DATA INGESTION 
The Data ingestion part of pipeline consists of scheduled pulling of COVID19 data from the API (both historical and daily updates) at 1400 hours every day (daily data is expected to be updated every day around noon EST). A storage bucket has been created in GCS . A Google Cloud Function and Google Cloud Scheduler together will pull the data from API and put in GCS Bucket. A python script has been used in Google Cloud Function .  The historic and current data has also been merged to ingest a combined data (using the python script in GCF)into the bucket for further transformation and processing. The python script used in Cloud Function is https://github.com/HSubbu/dtc-de-project-mar22/blob/main/ingest_data.txt 

The detailed documentation for data ingestion part is given in this [link](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/data-ingestion.pdf)

Creating GCS bucket video link https://loom.com/share/55355ddbd91b4cf980e8a9584117f03c 

Creating a service account https://www.loom.com/share/a832ec5c8e364261a569fcd2d99ffdf9

Create a cloud Function for data ingestion https://www.loom.com/share/9ff420fbb7d941fb81a58d7bce8eed57

Local testing of Cloud Function https://www.loom.com/share/e9b62bf6551d4147b89c36348c3808a5

Creata cloud scheduler https://www.loom.com/share/e06f13c657714eb588c7512790dd2652

## ETL PIPELINE 
The data ingestion puts the data into GCS bucket everyday at 1400 hrs . The data in GCS bucket needs to be further loaded into DWH(our case Big Query) after some data transformation. GCP tool called DATA FUSION was adopted for the ETL process. The Data Fusion has UI which can pull the data from GCS and carry our basic transformation and load data as BQ table . The transformation consists of dropping some columns which has irrelavant data , parsing dat as datetime and filling na values. In addition, these pipeline execution can be scheduled to run at specified intervals everyday. I am ingesting the data at 1400 hours everyday. Hence the pileine is scheduled to run at 1500 hours everyday. There are two data pipelines running simultaeneously , once for the current data and one for combined data. The pipeline ingests two tables in BQ , current_data and combined_data . 

Detailed documentation of ETL pipeline is given [link](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/data_transformation_cloud_datafusion.pdf)

The ETL in Google Data Fusion is as shown [link[(https://github.com/HSubbu/dtc-de-project-mar22/blob/main/etl_data_fusion.png)

## DASHBOARD
The tables in BQ has been used as input data to GOOGLE DATA STUDIO to create Dashboards. The Dashboards presents two pages/tiles . One for current data and once giving historical perspective(since the time pandemic started) . The dashboards get updated when the tables get updated by the pipeline. 

The detailed documentation for the Dashboard creatiion is in [link]{https://github.com/HSubbu/dtc-de-project-mar22/blob/main/data_transformation_cloud_datafusion.pdf)

Dashboard tile one layout [link](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/dashboard_tile1.png)

Dashboard tile two layout [link](https://github.com/HSubbu/dtc-de-project-mar22/blob/main/dashboard_tile2.png)

## CONCLUSION

The Data Engineering project build a simple data pipeline which extracts COVID data from API and loads into a data lake. The data is further extracted for transformation and loaded into Data Ware House (DWH) , viz, Big Query. The tables in BQ is further processed to create a Dashboard using Google Data Studio. The entire pipeline functionng has been automated using scheduler tools in GCP and data is observeed to move seamlessly to update the Dashboard everyday. 

## AREAS FOR IMPROVEMENT

This project  is an attempt to put into practice, the learnings from DataTalksClub DE Zoomcamp. It is acknowledged that there is scope to improve the project to achieve improved performance . Following areas are identified as areas of improvement :

  (a) The cost optimatization of GCP platform with current dataflow plipeline 
  
  (b) Try out more transformation in ETL to achieve better/variety of data output 
  
  (c) Identify more metrics (critical ones ) for incorporation in dashboard
  
  (d) CI/CD pipeline of testing (I have manually tested the pipeline , automated testing is way to go !)
  
  (e) Improve the documentation to provide more formal structure.

## REFERENCES

Cloud Function for Data Ingstion [link](https://www.ternarydata.com/news/use-python-and-google-cloud-to-schedule-a-file-download-and-load-into-bigquery-3p3aw)

Data Fusion for ETL. [link](https://codelabs.developers.google.com/codelabs/batch-csv-cdf-bq#0)

Data Fusion for ETL [link](https://www.youtube.com/watch?v=1QhJDsYQTfM) 

Data Studio for visualisation [link](https://codelabs.developers.google.com/codelabs/bigquery-data-studio#2)

Building dashboards in Data Studio [link](https://datadrivenlabs.io/blog/how-to-build-a-data-studio-dashboard/)
