# Get Global Rates (SOFR, EURIBOR, SARON, SONIA) #

Pull the rate for different interest rate on the website "https://www.global-rates.com/en/".
This Python script generate the collect the data and load them in a table in a database.

### Description

* Version 2
* Documentation attached to the repository
![Global Rate](https://github.com/dnaval/globalrates/blob/main/GlobalRates.gif)

### Dependencies

* MYSQL  (DATABASE)
* Python (POGRAMMING LANGUAGE)
* Docker

### Executing program

* Update .env.example.local then rename to .env.local file. 
* Copy content of .env.local in GlobalRates_script/.env
* RUN docker-compose --env-file .env.local up --build

### Authors

Contributors names and contact info

Daniel Naval 
[@navald27](https://twitter.com/navald27)
# globalrates

