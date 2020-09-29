"""
By: Marcus Chan
The purpose of this file is to act as a main function and to work with all python file in the package thus far
"""

from db_operations.PostgreSQL_analysis import db_interactions
from db_operations.PostgreSQL_insertion import db_insert
from db_operations.stock_reader import web_interaction

yf_reader = web_interaction()
yf_reader.csv_extract("D:\\Marcus\\Python\\Github_PG_cnd\\test_file.csv")



