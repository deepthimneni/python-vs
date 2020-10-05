from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Integer, String, Column

class PythonFunction(object):
    """description of class"""
    engine = None

    def __init__(self):
        self.engine = create_engine("mysql://root:Deepu805!@localhost/college",echo = True)
        #written staticconfig file 

        meta = MetaData()

        students = Table(
           'students', meta, 
           Column('id', Integer, primary_key = True), 
           Column('firstname', String(256)), 
           Column('lastname', String(256)),
        )
        meta.create_all(self.engine)        

    def execute_query(self,query):
        with self.engine.connect() as connection:
            return connection.execute(query)


    def create_students(self,firstname,lastname):
        query = "INSERT INTO students (firstname,lastname) values ('{firstname}','{lastname}')".format(firstname=firstname,lastname=lastname)
        self.execute_query(query)
        print("created student")

    def get_students(self):
        query = "SELECT * FROM students"
        result = self.execute_query(query)
        for row in result:
            print(row)
