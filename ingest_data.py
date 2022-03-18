import pandas as pd
import datetime
from google.cloud import storage
import os

def export_data(request):
  API_KEY = os.environ.get('API_KEY')
  HIST_URL = 'https://api.covidactnow.org/v2/states.timeseries.csv?apiKey='+API_KEY
  CURRENT_URL = 'https://api.covidactnow.org/v2/states.csv?apiKey='+API_KEY
  df_hist = pd.read_csv(HIST_URL)
  df_current = pd.read_csv(CURRENT_URL)
  csv_str_hist = df_hist.to_csv()
  csv_str_current = df_current.to_csv()

  # Then, upload it to cloud storage
  def upload_blob(bucket_name, data, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(data, content_type='text/csv')
  
  upload_blob('de-project-data', csv_str_hist, 'hist-data-' + str(datetime.date.today()) + '.csv')
  upload_blob('de-project-data', csv_str_current, 'current-data-' + str(datetime.date.today()) + '.csv')

  return 'Job Completed'

