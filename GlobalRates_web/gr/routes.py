from flask import Flask
from flask import render_template
from sqlalchemy import text
from gr import app, db

# ********* SQL - GET DATA *********
def get_rates_data(rate_type):
    # Example raw SQL query
    query = text("SELECT * FROM grates WHERE `rate`=:value ORDER BY `year`, STR_TO_DATE(CONCAT('0001 ', `month`, ' 01'), '%Y %M %d')")

    # Execute the query using the connection
    rates = db.session.execute(query, {"value": rate_type}).fetchall()
    
    db.session.close()
    return rates


# ********* HOME PAGE *********
# DASHBOARD
@app.route("/")
def home_view():
    euribor_data = get_rates_data('euribor')
    saron_data = get_rates_data('saron')
    sofr_data = get_rates_data('sofr')
    sonia_data = get_rates_data('sonia')
    return render_template('dashboard.html', year='2024', euribor=euribor_data, saron=saron_data, sofr=sofr_data, sonia=sonia_data)
