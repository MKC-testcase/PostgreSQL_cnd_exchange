import unittest
import psycopg2

# you have to revise how to code this unittest (part of the program instead of part of the unittest)
class PostgreSQL_Test(unittest.TestCase):
    #task to do set up a setup and tear down so I won'd need to keep doing the open connection and close connection
    def test_connection(self):
        self.conn = psycopg2.connect(host = "localhost", database = "mdata",user = "postgres", password = "deus3stm4china")
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT version()')
        db_version = self.cur.fetchone()
        self.assertEqual(db_version, "('PostgreSQL 12.1, compiled by Visual C++ build 1914, 64-bit',)")
        self.conn.close()

    def test_database_id(self):
        self.conn = psycopg2.connect(host="localhost", database="mdata", user="postgres", password="deus3stm4china")
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT id FROM cnd_exchange_rate WHERE id = 3')
        id_check = self.cur.fetchone()
        self.assertEqual(id_check, "3")
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
