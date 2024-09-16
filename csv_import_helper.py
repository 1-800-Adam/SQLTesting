import pandas as pd
import sqlite3

def create_from_CSV(folder="csv_import_helper", file_name=None, db_name=None, table_name="automation_data"):
# Replace 'your_file.csv' with the path to your CSV file
# folder = r"csv_import_helper"
# file_name = r"automation_data_by_state.csv"
# table_DB_name = "automation_data"
    if file_name is None:
        return
    file_path = folder + '\\' + file_name

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, encoding='latin1')

    # Print the first 5 rows of the DataFrame
    print(df.head())

    # Try reading the CSV file with a different encoding
    try:
        df = pd.read_csv(file_path, encoding='utf-8')  # Default encoding
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin1')  # Alternative encoding
        # You can also try 'cp1252' or other encodings if necessary

    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name + ".db")

    # Write the DataFrame to an SQLite table
    # Replace 'table_name' with the desired table name
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    #test
    my_cur = conn.cursor()
    test_query = "SELECT * FROM " + table_name + ";"
    my_cur.execute(test_query)

    i=0
    for row in my_cur.fetchall():
        i = i + 1 
        print(row)
        if i >= 20:
            break

    # Close the connection
    conn.close()

def add_table_to_db(folder="csv_import_helper", file_name=None, db_name="automation_data", new_table_name=None):
    if (file_name is None) or (new_table_name is None):
        return
    file_path = folder + '\\' + file_name

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, encoding='latin1')

    # Print the first 5 rows of the DataFrame
    print(df.head())

    # Try reading the CSV file with a different encoding
    try:
        df = pd.read_csv(file_path, encoding='utf-8')  # Default encoding
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin1')  # Alternative encoding
        # You can also try 'cp1252' or other encodings if necessary

    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name + ".db")

    # Write the DataFrame to an SQLite table
    # Replace 'table_name' with the desired table name
    df.to_sql(new_table_name, conn, if_exists='replace', index=False)

    #test
    my_cur = conn.cursor()
    test_query = "SELECT * FROM " + new_table_name + ";"
    my_cur.execute(test_query)

    i=0
    for row in my_cur.fetchall():
        i = i + 1 
        print(row)
        if i >= 20:
            break

    # Close the connection
    conn.close()

def main():
    create_from_CSV(folder="csv_import_helper", file_name="characters.csv", db_name="fantasy", table_name="characters")
    add_table_to_db(folder="csv_import_helper", file_name="inventory.csv", db_name="fantasy", new_table_name="inventory")
    add_table_to_db(folder="csv_import_helper", file_name="items.csv", db_name="fantasy", new_table_name="items")

main() 