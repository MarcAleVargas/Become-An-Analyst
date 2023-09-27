import cx_Oracle #Download this libary - "pip install cx_Oracle" on your terminal
import pyodbc #Download this libary - "pip install pyodbc" on your terminal

"""
using this code you will be able to connect to different database
once is connected you need to read you SQL and put together the connection like: pd.read_sql(sql_statement,connection)
"""

class database():
    def __init__(self, user, password, server, database):
        #Before to run this make sure you have the access and drivers to connect to the database
        #// database Credentials
        self.database_user = user
        self.database_password = password
        self.database_server = server
        self.database = database
    
    def connection(self):
        try:
            if self.database == 'oracle_(Name)':
                self.connection = cx_Oracle.connect(self.database_user,
                                    self.database_password,
                                    self.database_server)
                self.cursor = self.connection.cursor()

            elif self.database == 'odbc_(Name)':
                    self.connection = pyodbc.connect(
                        f"""DSN={self.self.database_server};
                        UID={self.self.database_user};
                        PWD={self.database_password}"""
                        )
                    self.cursor = self.connection.cursor()
            print("Connection Successfully")
            return(self.connection)
        except:
            print("Connection Lost")
    

#database().connection()

"""
You can set up your credentials in the enviroment so you won't be rewriting everything your credentials and separete each database with a different class in order to pass the right credentials.
"""