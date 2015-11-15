'''
   Provides access to the Pronto Data files, downloading the
   data if it is not present.

BUGS/FEATURES
1. Test getTripData
2. Deal with unzip file exists
'''

import os
import shutil
import pandas as pd
import numpy as np
from subprocess import call

PRONTO_FILES = ["2015_station_data.csv", "2015_status_data.csv",
                "2015_trip_data.csv", "2015_weather_data.csv",
                "README.txt", "open_data_year_one.zip"]
PARENT_PATH = os.path.abspath("..")
DATA_DIR = os.path.join(PARENT_PATH, "Data")

class StackDir(object):

  '''This class provides a stack to easily navigate directories.'''

  def __init__(self):
    self.stack = []

  def push(self, new_directory):
    # Move to the new directory, remembering the current directory
    # Input: new_directory - new directory
    self.stack.insert(0, os.getcwd())
    os.chdir(new_directory)

  def pop(self):
    # Move to the previous directory
    new_directory = self.stack.pop()
    os.chdir(new_directory)


def getProntoFiles(file_name="open_data_year_one",
    url="https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
    ):
  # Makes sure that the data are downloaded into Data/
  stack_dir = StackDir()
  stack_dir.push(DATA_DIR)
  zip_file = "%s.zip" % file_name
  if not os.path.exists(zip_file):
    call(["curl", 
        "-O", 
        url
        ])
    call(["unzip", zip_file])
  stack_dir.pop()
  return

def deleteDataFiles(file_list = PRONTO_FILES):
  # Deletes files from the data directory
  stack_dir = StackDir()
  stack_dir.push(DATA_DIR)
  for item in file_list:
    os.remove(item)
  stack_dir.pop()

def getTripData():
  # Returns a pandas dataframe with the trip data
  getProntoFiles()
  TRIP_FILE = "2015_trip_data.csv"
  abs_path = os.path.join(PARENT_PATH, "Data/%s" % TRIP_FILE)
  result = pd.read_csv(abs_path,
      parse_dates=['starttime', 'stoptime'],
      infer_datetime_format=True)
