# This project is licenced under the MIT licence.

# Imports.
from sqlite3 import connect


# Database and sql.
DATABASE = 'api/seeker.db'
USER_QUERY = 'SELECT building, num, time FROM rooms WHERE building = ? \
              AND day = ? AND time >= ? AND time <= ? ORDER BY num ASC;'

# Debug output.
VERBOSE = False


def query(building, day, time):
    '''
    Query the database for room information. Then format and return the data.

    Arguments:
        - building (string): Building to query.
        - day (string): Day to query.
        - time (int): Start time in minutes since the beginning of the day.

    Returns:
        - (list): List containing the query results.
    '''

    # First, query the database for the unformatted data.
    con = connect(DATABASE)
    curs = con.cursor()
    
    curs.execute(USER_QUERY, (building, day, time, min(time + 240, 1200)))
    res = curs.fetchall()

    con.close()

    # If res is empty, return an empty list.
    # TODO: Handle return properly and send codes.
    if not res:
        return []

    # Initialize formatted room list.
    # Build formatted data values based on room numbers and time.
    rooms, cur_building, cur_room = [], res[0][0], res[0][1]
    time_s, time_e = res[0][2], res[0][2]

    # Add terminating data to res list.
    # This allows us to catch the last room number cleanly.
    res.append((None, None, None))

    for i in res:
        if i[1] == cur_room and i[2] == time_e + 30:
            time_e += 30
        elif i[1] == cur_room:
            continue
        else:
            rooms.append({
                'building': cur_building,
                'room': cur_room,
                'time': format_time(time_s) + ' - ' + format_time(time_e + 20)
            })
            cur_building, cur_room = i[0], i[1]
            time_s = time_e = i[2]

            # Debug info.
            if VERBOSE:
                print('Formatted room data:', rooms[-1])

    # Return the formatted room data.
    return sorted(rooms, key=lambda x: x['time'][:2].replace(':', '').zfill(2))


def format_time(time):
    '''
    Formats time from minutes since start of day to 12 hour format.

    Arguments:
        - time (int): Time in minutes since start of day.
    
    Returns:
        - (string): Formatted time value.
    '''

    # Get hours and minutes.
    hours, minutes = time // 60, time % 60

    # Get meridiem and shift hours.
    meridiem = ('AM' if hours < 12 else 'PM')
    hours = (hours % 12 if hours % 12 != 0 else 12)

    # Return format as XX:XX AM / PM.
    return str(hours) + ':' + str(minutes).zfill(2) + ' ' + meridiem