#!/usr/bin/env python3
# #By Marcus Chan
#Last Updated 2020-08-20
#Required Libraries: psycopg2, PostgreSQL_analysis.py
#Purpose:To create a conviennient wrapper for psycopg2 and create a few other functions to interact with inserting things
#       from the database

import psycopg2
from db_operations.PostgreSQL_analysis import db_interactions

class db_insert:
    """This class is used for helping with inserting data into the database"""
    def insert_help(self):
        """Creates guide to help the user see and interact with directing insertions into the database"""
