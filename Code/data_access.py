'''
   Provides access to the Pronto Data files, downloading the
   data if it is not present.

BUGS/FEATURES
1. Test getTripData
2. Deal with unzip file exists
'''

import settings
import utils
import os
import shutil
import pandas as pd
import numpy as np
from subprocess import call


def getDataFile(
    url="https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
    ):
  # Acquires the data from the URL
  zip_file = os.path.split(url)[-1]
  stack_dir = utils.StackDir()
  stack_dir.push(settings.DATA_DIR)
  if not os.path.exists(zip_file):
    call(["curl", 
        "-O", 
        url
        ])
    call(["unzip", zip_file])
  stack_dir.pop()
  return

def deleteDataFiles(file_list = settings.PRONTO_FILES):
  # Deletes files from the data directory
  stack_dir = utils.StackDir()
  stack_dir.push(settings.DATA_DIR)
  for item in file_list:
    os.remove(item)
  stack_dir.pop()

def getTripsData():
  # Returns a pandas dataframe with the trip data
  getDataFile()
  abs_path = os.path.join(settings.PARENT_PATH, "Data/%s" % 
      settings.TRIP_FILE)
  result = pd.read_csv(abs_path,
      parse_dates=['starttime', 'stoptime'],
      infer_datetime_format=True)
  ind = pd.DatetimeIndex(result.starttime)
  result['date'] = ind.date.astype('datetime64')
  result['hour'] = ind.hour
  return result
