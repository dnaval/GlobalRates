import os
from dotenv import load_dotenv
from GlobalRatesUtils import db_conn, get_rate_value

# Get DB Engine
engine = db_conn()

# Get year value
year = os.getenv("year")

# Get and load Euribor rate value
url = os.getenv("euribor_url")
get_rate_value(year, url, 'Euribor 1 week in '+year, engine, 'euribor')

# Get and load Saron rate value
url = os.getenv("saron_url")
get_rate_value(year, url, 'SARON in '+year+' - per month', engine, 'saron')

# Get and load Sofr rate value
url = os.getenv("sofr_url")
get_rate_value(year, url, 'SOFR in '+year+' - per month', engine, 'sofr')

# Get and load Sonia rate value
url = os.getenv("sonia_url")
get_rate_value(year, url, 'SONIA in '+year+' - per month', engine, 'sonia')
