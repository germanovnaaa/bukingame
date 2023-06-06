from .db_config import Config
import datetime
import random

def create_new_user(email: str, password: str) -> str:
    try:
        Config().mssql_connection.execute(f"""
        INSERT INTO [users] (email, password)
        VALUES ('{email}', '{password}')
        """)
        return 'success'
    except:
        return 'unsuccess'


def check_user(email: str, password: str) -> int:
    try:
        user = Config().mssql_connection.execute(f"""
        SELECT * from [users] WHERE
        email = '{email}' AND password = '{password}'
        """).fetchall()[0]
        if user:
            return 1
        else:
            return 0
    except:
        return 0


def get_user_data(email: str, password: str) -> tuple:
    try:
        id, email, password = Config().mssql_connection.execute(f"""
        SELECT * from [users] WHERE
        email = '{email}' AND password = '{password}'
        """).fetchall()[0]
        return id, email, password
    except:
        return ()


def get_userid_for_order(email: str) -> tuple:
    try:
        id = Config().mssql_connection.execute(f"""
        SELECT id from [users] WHERE
        email = '{email}'
        """).fetchall()[0]
        return id[0]
    except:
        return ()


def create_order(email: str, game_name: str, price: float) -> str:
    try:
        order_date = datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 7))
        user_id = get_userid_for_order(email)
        Config().mssql_connection.execute(f"""
        INSERT INTO [orders] (user_id, game_name, price, date)
        VALUES ({user_id}, '{game_name}', {price}, '{order_date}')
        """)
        return 'success'
    except:
        return 'unsuccess'


def get_user_orders(email: str) -> tuple:
    try:
        data = Config().mssql_connection.execute(f"""
        SELECT id, game_name, price, date from [orders] WHERE
        user_id = (SELECT id from users WHERE email = '{email}')
        """).fetchall()[:]
        return data
    except:
        return ()
