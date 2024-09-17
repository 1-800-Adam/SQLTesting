"""
These scripts are for testing out SQL Functions in python: https://www.geeksforgeeks.org/sql-using-python/
"""
import sqlite3
import logging
import pandas as pd
import re

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
    try: 
        db_conn.close()
        logger.info("Closed connection to the database: {db_name}".format(db_name = str(db_conn))) # print statement will execute if there are no errors
    except sqlite3.ProgrammingError:
        logger.info("DB connection seems to already be closed")
    
def close():
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)
    logger.info('closed')

def dialogue(db_conn, close_conn=True):
    """
    Open a dialogue for continueous DB SQL Queries until recieves a QUIT symbol. Then Closes the conn

    Args:
        db_conn (???): connection to the database.
        close_conn (bool): flag for if the program should close the db connection
    """
    def manual_tokenize_sql(query):
        # Split by spaces and punctuation
        tokens = re.split(r'(\s+|,|;|\(|\))', query)
        tokens = [token.strip() for token in tokens if token.strip()]
        return tokens
    
    def reconstruct_statement(tokens):
        return ' '.join(tokens)


    logger.info("Started DB Dialogue. Type 'QUIT' to exit...")

    #userexit = False
    while True:
        userinput = input("User Query: ")
        if userinput == "QUIT":
            db_close(db_conn) if close_conn else None
            break
        else:
            sql_tokens = manual_tokenize_sql(userinput)
            logger.info("SQL TOKENS: " + str(sql_tokens))
            sql_statement = reconstruct_statement(sql_tokens)
            logger.info("SQL STATEMENT is: " + str(sql_statement))
            try:
                df = pd.read_sql_query(sql_statement, db_conn)
                print(df)
            except:
                continue

def main():
    my_db,my_cur = db_conn("fantasy.db")
    dialogue(my_db)
    db_close(my_db)

logger = logging_setup()
logger.info('___Program Started___')
main()
logger.info('___Program Finished___')

