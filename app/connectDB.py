import pyodbc

class ConnectDB:
    def db_connect(self):
        conn = pyodbc.connect(
                        "Driver=SQL Server;"
                        "Server=localhost;"
                        "Database=UserManagement;"
                        "uid=sa;"
                        "pwd=12345;"
                        "Trusted_Connection=yes;"
                    )
        return conn

    