'''Reads the data into a pandas dataframe.'''

'''
BUGS
1. Read trips file, not general zip
'''

import os
import shutil
import pandas as pd
import numpy as np
from subprocess import call

def ProntoData(file_name="open_data_year_one",
    url="https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
    ):
  # Returns a Pandas data frame
  parent_path = os.path.abspath("..")
  zip_file = "%s.zip" % file_name
  csv_file = "%s.csv" % file_name
  zip_abs_path = os.path.join(parent_path, "Data/%s" % zip_file)
  csv_abs_path = os.path.join(parent_path, "Data/%s" % csv_file)
  import pdb; pdb.set_trace()
  if not os.path.exists(zip_abs_path):
#    call(["curl", 
#        "-O", 
#        url
#        ])
    shutil.move(zip_file, zip_abs_path)
    call(["unzip", zip_abs_path])
  result = pd.read_csv(csv_abs_path,
      parse_dates=['starttime', 'stoptime'],
      infer_datetime_format=True)
  return result

result = ProntoData()

