import unittest
import psycopg2
from cnd_exchange_rate.db_operations.PostgreSQL_analysis import db_interactions



class PostgreSQL_Test(unittest.TestCase):

    def test_connection(self):
        """This test Initial connection to the database"""
        """This test to see if a connection can be made to the database"""
        self.conn = psycopg2.connect(host="localhost", database="mdata", user="postgres", password="deus3stm4china")
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT version()')
        id_check = self.cur.fetchone()
        self.assertEqual(id_check, ('PostgreSQL 12.1, compiled by Visual C++ build 1914, 64-bit',))
        self.conn.close()

    def test_class_interaction(self):
        """Tests the basic functions in the PostgreSQL_analysis.py"""
        self.new_class = db_interactions()
        self.new_class.query_version()
        db_version = self.new_class.get_fetchone()
        self.new_class.print_db()
        self.assertEqual(db_version,('PostgreSQL 12.1, compiled by Visual C++ build 1914, 64-bit',))

    def test_database_id(self):
        self.conn = psycopg2.connect(host="localhost", database="mdata", user="postgres", password="deus3stm4china")
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT id FROM cnd_exchange_rate WHERE id = 3')
        id_check = self.cur.fetchone()
        self.assertEqual(id_check, "3")
        self.conn.close()

    def test_connection(self):
        """
        self.new_class = db_interactions()
        self.cur.execute('SELECT version()')
        db_version = self.cur.fetchone()
        self.assertEqual(db_version, "('PostgreSQL 12.1, compiled by Visual C++ build 1914, 64-bit',)")
        self.conn.close()


        """

if __name__ == '__main__':
    unittest.main()
