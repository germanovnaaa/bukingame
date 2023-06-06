from sqlalchemy import create_engine

"""
All database configs could be placed here
"""

class Config:

    def __init__(self):
        """
                DATABASE: PUT YOUR MSSQLSERVER'S DATABASE_NAME
                SERVER: PUT YOUR MSSQLSERVER'S SERVER_NAME
                USER: PUT YOUR MSSQLSERVER'S USERNAME
                PASSWORD: PUT YOUR MSSQLSERVER'S PASSWORD
                :return: admin's config + connection string for database mssql server 2012
                """
        # config settings
        HOST_NAME = 'mssql'
        USER = 'db_admin'
        PASSWORD = '2002'
        DRIVER = 'ODBC Driver 17 for SQL Server'
        DATABASE = 'users'
        SERVER = 'APACHE'
        connection_URL = f"{HOST_NAME}://{USER}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}"
        self.mssql_engine = create_engine(connection_URL)
        self.mssql_connection = self.mssql_engine.connect()
