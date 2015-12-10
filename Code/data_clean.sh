#!/bin/bash
# Remove the pronto data files
# Assumes running from the Code directory
cd ../Data
rm -f open_data_year_one.zip
for f in *.csv
do
  rm -f $f
done
rm -f README.txt