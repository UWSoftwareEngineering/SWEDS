#!/bin/bash
# Download the data file and uncompress it.
# Assumes running from the Code directory
cd ../Data
curl "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
unzip "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
