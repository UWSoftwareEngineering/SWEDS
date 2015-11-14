'''Reads the data into a pandas dataframe.'''

/*
BUGS
1. file ends up in Code, not Data
2. Setting paths in ipython
*/

import os
import pandas as pd
import numpy as np
from subprocess import call

def ProntoData(data_set="open_data_year_one.zip",
    url="https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
    ):
  # Returns a Pandas data frame
  parent_path = os.path.abspath("..")
  abs_path = os.path.join(parent_path, "Data/%s" % data_set)
  import pdb; pdb.set_trace()
  if not os.path.exists(abs_path):
    call(["curl", 
        "-O", 
        url
        ])
    call(["unzip", abs_path])
  result = pd.read_csv(abs_path,
      parse_dates=['starttime', 'stoptime'],
      infer_datetime_format=True)
  return result

result = ProntoData()

