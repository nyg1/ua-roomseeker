# This project is licenced under the MIT licence.

# Imports.
import sqlite3, json
from sys import exit, argv
from os import listdir, path

# Data dir from web scraping.
DATA_DIR = '../web_scraping/data/'

# Database and sql files.
DATABASE = 'seeker.db'
SCHEMA = 'schema.sql'

# SQL query, with placeholders.
INSERT_QUERY = 'INSERT INTO rooms(building, num, day, time) VALUES (?, ?, ?, ?);'

# Debug output.
VERBOSE = False


def main():
    '''
    Main function, controls database initialization.
    '''

    # First initialize the database. We may exit the program here.
    init_res = create_db(('-f' in argv))

    if not init_res:
        exit(0)
    
    # Load in the room info from every data file.
    data = load_data()

    # Debug info.
    if VERBOSE:
        print('Populating database with json data.')
    
    # Establish a connection and populate the database.
    con = sqlite3.connect(DATABASE)

    con.cursor().executemany(INSERT_QUERY, data)
    
    # Close the connection.
    con.commit()
    con.close()

    # Debug info.
    if VERBOSE:
        print('Successfully populated database.')


def create_db(force_flag):
    '''
    Prompt the user to initialize the seeker database or not.
    Overwrites any existing one.

    Arguments:
        - force_flag (bool): Boolean for forcing init or not.
    
    Returns:
        - (bool): Boolean for was the database initalized or not.
    '''

    # Prompt the user to verify they want to initialize the database.
    if not force_flag:
        print('Are you sure you want to initialize the database? (y/n)')
        print('This will delete the current database, and can\'t be undone.')

        res = ''

        # Make sure the user input is correct.
        while res != 'y' and res != 'n':
            res = input()

            if res != 'y' and res != 'n':
                print('Invalid response, please answer y/n.')
        
        # Return if not.
        if res == 'n':
            return False

    # Connect to the sqlite3 database and initialize the schema.
    con = sqlite3.connect(DATABASE)

    # Debug info.
    if VERBOSE:
        print('Opened connection to the database.')
    
    with open(SCHEMA, 'r') as f:
        curs, buf = con.cursor(), ''

        for line in f:
            if len(line.strip()) > 0:
                buf += line.strip()
            
            if ';' in buf:
                curs.execute(buf)

                # Debug info.
                if VERBOSE:
                    print('Executing query:', buf)

                buf = ''
        
        con.commit()
    
    # Debug info.
    if VERBOSE:
        print('Closing connection to the database.')

    # Close the database connection and return.
    con.close()
    return True


def load_data():
    '''
    Load in the json data that was obtained from web scraping.
    Loads in data based on whatever is in DATA_DIR.

    Returns:
        - (list): List of all the data to populate the database with.
    '''

    # Initialize the list of data.
    data = []

    # Loop through every file in the data directory.
    for file in listdir(DATA_DIR):
        if not path.isfile(DATA_DIR + file):
            continue

        # Remove `.json` extention for building name.
        building = file[:-5]

        # Debug info.
        if VERBOSE:
            print('Reading from file:', file)

        # Read in all the file's data.
        with open(DATA_DIR + file, 'r') as f:
            json_data = json.load(f)

            for day in json_data:
                for room in json_data[day]:
                    for time in json_data[day][room]:
                        data.append((building, room, day, time))
    
    # Return the final data list.
    return data


# Entry point of the program.
if __name__ == '__main__':
    main()