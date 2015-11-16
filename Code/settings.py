''' Parameters used in analysis. '''

import os


PRONTO_FILES = ["2015_station_data.csv", "2015_status_data.csv",
                "2015_trip_data.csv", "2015_weather_data.csv",
                "README.txt", "open_data_year_one.zip"]
PARENT_PATH = os.path.abspath("..")
CODE_DIR = os.path.join(PARENT_PATH, "Code")
DATA_DIR = os.path.join(PARENT_PATH, "Data")
TRIP_FILE = "2015_trip_data.csv"
