import psycopg2

class db_interactions:
    """ This class will be used to control the interactions between a PostgreSQL or not"""
    def __init__(self):
        self.db_content = []

    def query_version(self):
        """Base query to test initial connection"""
        self.cur.execte('SELECT version()')

    def print_db(self):
        """prints everythings that has been collected - as easy check"""
        for i in self.db_content:
            print(i)

#New structure for fetch, have 1 fetchas that does all the other fetch when other input given, if no input fetch all
    def get_fetchone(self):
        """collects 1 of the results of the query"""
        self.db_content = self.cur.fetchone()

    def get_fetchall(self):
        """collects all of the results of the query"""
        self.db_content = self.cur.fetchall()

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
