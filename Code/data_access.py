'''
   Provides access to the Pronto Data files, downloading the
   data if it is not present.

BUGS/FEATURES
1. Tests
2. Separate access to different data files
3. Deal with unzip file exists
'''

import os
import shutil
import pandas as pd
import numpy as np
from subprocess import call

def prontoData(file_name="open_data_year_one",
    url="https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
    ):
  # Makes sure that the data are downloaded into Data/
  # Changes to the data directory
  parent_path = os.path.abspath("..")
  data_dir = os.path.join(parent_path, "Data")
  os.chdir(data_dir)
  zip_file = "%s.zip" % file_name
  if not os.path.exists(zip_file):
    os.chdir
    call(["curl", 
        "-O", 
        url
        ])
    import pdb; pdb.set_trace()
    call(["unzip", zip_file])
  return

def tripData():
  # Returns a pandas dataframe with the trip data
  prontoData()
  TRIP_FILE = "2015_trip_data.csv"
  abs_path = os.path.join(parent_path, "Data/%s" % TRIP_FILE)
  result = pd.read_csv(abs_path,
      parse_dates=['starttime', 'stoptime'],
      infer_datetime_format=True)
