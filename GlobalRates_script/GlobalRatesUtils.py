import requests
import re
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

# Load variables from .env file
load_dotenv()

def db_conn():
    # Define your database credentials
    username = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST")  # or your database server's IP
    port = os.getenv("MYSQL_PORT")  # Default MySQL port
    database = os.getenv("MYSQL_DATABASE")

    # Create the connection string
    connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

    # Create an engine
    engine = create_engine(connection_string)

    return engine

def get_rate_value(year, url, cap_txt, engine, rate_type):
    # Get data from site
    try:
        # Clean HTml string
        CLEANR = re.compile('<.*?>') 

        # Make a request to the website
        url = url+'/'+ year +'/'
        response = requests.get(url)

        # Use Beautiful Soup to parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <caption> tags and their text
        captions = soup.findAll('caption')

        # Extract and print the text of each <caption> tag
        for caption in captions:
            if caption.get_text(strip=True) == cap_txt:
                #print(caption.get_text(strip=True))
                # Find the parent <table> tag of the <caption> tag
                table_tag = caption.find_parent('table')
                if table_tag:
                    tbody = table_tag.find('tbody')
                    print(caption.get_text(strip=True))
                else:
                    print("Parent table not found")
            else:
                print("Caption tag not found")

        for row in tbody.findAll("tr"):
            cells = row.findAll("td")
            nav = []
            for cell in cells:
                cleantext =  re.sub('▲', '', re.sub(CLEANR, '', str(cell))).translate({ord('%'): None})
                nav.append(cleantext)

            if(len(nav)!=0):
                # SELECT and INSERT Example
                with engine.connect() as connection:
                    # Fetch existing rows
                    select_query = text("SELECT COUNT(*) FROM grates WHERE `rate`=:value0 AND `month` = :value1 AND `year`= :value2")
                    result = connection.execute(select_query, {"value0":""+rate_type+"", "value1": ""+str(nav[0]).strip()+"", "value2": ""+year+""})
                    
                    # Fetch the result
                    count = result.scalar()
                    if(count==0):
                        # Insert a new row
                        insert_query = text("INSERT INTO `grates`( `rate`, `month`, `first`, `last`, `high`, `low`, `average`, `year`) VALUES (:value1, :value2, :value3, :value4, :value5, :value6, :value7, :value8)")
                        connection.execute(insert_query, {"value1": ""+rate_type+"", "value2": ""+str(nav[0]).strip()+"", "value3": ""+str(nav[1]).strip()+"", "value4": ""+str(nav[2]).strip()+"", "value5": ""+str(nav[3]).strip()+"", "value6": ""+str(nav[4]).strip()+"", "value7": ""+str(nav[5]).strip()+"", "value8": ""+year+""})
                        connection.commit()
        print(rate_type+" rates upload in table")
    except Exception as e:
        print(f"An error occurred: {e}")
