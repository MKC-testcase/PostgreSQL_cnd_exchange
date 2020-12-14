"""
By: Marcus Chan
The purpose of this file is to act as a main function and to work with all python file in the package thus far
"""

from db_operations.PostgreSQL_analysis import db_interactions
from db_operations.PostgreSQL_insertion import db_insert
from db_operations.stock_reader import web_interaction
from time import sleep

column_names = ["previous_close", "open", "bin", "ask", "day_range", "52 Week Range", "volume", "avg_volume", " market_cap", "beta(5Y Monthly", "PE Ratio", "eps", "Earnings Data", "Foward Dividend & Yield", "Ex-Dividend Date", "1y Target Estimate"]
yf_reader = web_interaction()   #creates the object to interact with the functions in stock_reader
data_insert = db_insert()

#opens the csv file and sets it to web_interaction interal variable
yf_reader.csv_extract("D:\\Marcus\\Python\\Github_PG_cnd\\test_file.csv")

#this tests if the elements extracted are in the second row(TESTED)
for elem in yf_reader.csv_data:
    print(elem)
ticker_data = []

yf_reader.open_browser() #opens browser, yahoo finance

#loading the results from csv data into the rest of the web_interaction functions
for elem in yf_reader.csv_data:
    yf_reader.navigate_to_page(elem) #browser to indicate webpage
    sleep(4) #allows time for webpage to load
    yf_reader.extract_left() #gets the information from the leftside table
    yf_reader.extract_right() #gets information from the rightside table
    ticker_data.append(yf_reader.to_local()) #copies the information from internal variable to local list
    yf_reader.content_reset() #resets internal variable to empty list

#exits the browser to continue on the
yf_reader.exit_browser()#exits the browser

#how to proceed and insert the data into the database
for in_elem in ticker_data:
    data_insert.auto_insert("stock_data", column_names, in_elem)