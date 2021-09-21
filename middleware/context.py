
import os

# This is a bad place for this import
import pymysql

def get_db_info():
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """
    db_host = os.environ.get("DBHOST", None)
    db_user = os.environ.get("DBUSER", None)
    db_password = os.environ.get("DBPASSWORD", None)

    #Debug info
    print("get_db_info()")
    print("db_host: ", db_host)
    print("db_user: ", db_user)
    print("db_password: ", db_password)

    if db_host is not None:
        db_info = {
            "host": db_host,
            "user": db_user,
            "password": db_password,
            "cursorclass": pymysql.cursors.DictCursor
        }
    else:
        db_info = {
            "host": "localhost",
            "user": "dbuser",
            "password": "dbuserdbuser",
            "cursorclass": pymysql.cursors.DictCursor
        }

    return db_info
