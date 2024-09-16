"""
These scripts are for testing out SQL Functions in python: https://www.geeksforgeeks.org/sql-using-python/
"""
import sqlite3
import logging

def logging_setup():
    my_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='myapp.log', filemode='w', level=logging.DEBUG, format=my_format)
    s_logger = logging.getLogger(__name__) #establishes a logger obj
    s_logger.setLevel(logging.DEBUG)  # Set the logging level
    console_handler = logging.StreamHandler()
    # Define the log message format
    formatter = logging.Formatter(my_format)
    console_handler.setFormatter(formatter)
    s_logger.addHandler(console_handler)
    return s_logger

def db_conn(db_name):
    # connecting to the database
    db_conn = sqlite3.connect(db_name)
    # cursor
    my_cursor = db_conn.cursor()
    logger.info("Connected to the database: {} @ {}".format(db_name, str(db_conn))) # print statement will execute if there are no errors
    #logger.info("Closed connection to the database: {db_name}".format(db_name = str(db_conn))) # print statement will execute if there are no errors
    return db_conn,my_cursor

def db_close(db_conn):
    # close the connection
    db_conn.close()
    logger.info("Closed connection to the database: {db_name}".format(db_name = str(db_conn))) # print statement will execute if there are no errors
    pass

def close():
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)
    logger.info('closed')

def main():
    #my_db,my_cur = db_conn("Test.db") #connects to db
    my_db,my_cur = db_conn("test.db")

    ### Testing Sandbox ###
    sql_query = "SELECT * FROM automation_data_by_state.csv"
    my_cur.execute(sql_query)
    print(my_cur.fetchall)





    ### Testing Sandbox ###
    db_close(my_db)

logger = logging_setup()
logger.info('___Program Started___')
main()
logger.info('___Program Finished___')

