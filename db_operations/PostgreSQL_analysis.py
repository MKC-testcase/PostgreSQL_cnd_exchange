#!/usr/bin/env python3

import psycopg2

class db_interactions:
    """ This class will be used to control the interactions between a PostgreSQL or not"""
    def __init__(self):
        self.db_content = []
        try:
            self.conn = psycopg2.connect(host="localhost", database="mdata", user="postgres", password="deus3stm4china")
            self.cur = self.conn.cursor()
        except Exception as exc:
            print('Error: {} exception raised by connection request'.format(exc))
            raise

    def SQL_command_builder(self):
        """The purpose of this function is to offer to Create SQL command easily"""

    def execute_query(self, command):
        try:
            self.cur.execute(command)
        except ValueError:
            print("An incorrect SQL command was given Please Try Again")

    def query_version(self):
        """Base query to test initial connection"""
        self.cur.execute('SELECT version()')

    def print_db(self):
        """prints everythings that has been collected - as easy check"""
        for i in self.db_content:
            print(i)

#New structure for fetch, have 1 fetchas that does all the other fetch when other input given, if no input fetch all
    def get_fetch(self, *args, **kwargs):
        """implementation of variable fetches(one, many or all) """
        collect = kwargs.get('collect', None)
        try:
            if collect == None:
                self.db_content = self.cur.fetchall()
                return self.db_content
            elif collect != None:
                self.db_content = self.cur.fetchmany(collect)
                return self.db_content
        except ValueError:
            print("You have entered a non supported variable for this function. User a Number next time")

    def get_fetchone(self):
        """collects 1 of the results of the query"""
        self.db_content = self.cur.fetchone()
        return self.db_content

    def get_fetchall(self):
        """collects all of the results of the query"""
        self.db_content = self.cur.fetchall()
        return self.db_content

    def __enter__(self):
        """hopefully when this class is called it will automatically use this after the __init__"""
        try:
            self.conn = psycopg2.connect(host="localhost", database="mdata", user="postgres", password="deus3stm4china")
            self.cur = self.conn.cursor()
        except Exception as exc:
            print('Error: {} exception raised by connection request'.format(exc))
            raise

    def __exit__(self):
        """This function closes the database after object is used"""
        self.conn.close()

class db_analysis:
    def __init__(self):
        inter = db_interactions()

def main():
    test = db_interactions()

if __name__ == '__main__':
    main()