# (c) Noah Gergel, Sichun Xu, Weilin Qiu, Nina Yang 2020

# Imports.
from requests import get

# Global constants.
COURSE_URL = 'https://calendar.ualberta.ca/content.php?catoid=29&catoid=29&navoid=7430&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={}#acalog_template_course_filter'
CLASS_URL = 'https://catalogue.ualberta.ca/Course/Details?subjectCode={}&catalog={}'
NUM_PAGES = 3 # Hard coded number of pages.

# Debug flag.
VERBOSE = False


def scrape_courses():
    '''
    Parses full course listing and generates list of every course offered at
    the U of A, Including some misc garbage. Returns the raw course list.

    Returns:
        - (list): Raw data of course listings.
    '''

    # Initialize data list and parser.
    data = []

    # Loop through every page of courses.
    for i in range(1, NUM_PAGES + 1):
        # Get formatted URL.
        url = COURSE_URL.format(i)

        # Scrape HTML data and append to data.
        html = get(url).text
        data.append(html)

        # Debug info.
        if VERBOSE:
            print('Successfully scrapped course page #%d' % i)

    # Return the scrapped data.
    return data


def scrape_class(subject, num):
    '''
    Parses class page and return all the occupied times.

    Arguments:
        - subject (string): The course subject.
        - num (string): Course number, as a string.

    Returns:
        - (string): Raw data of a class page.
    '''

    # Get formatted URL and scrape HTML data.
    url = CLASS_URL.format(subject, num)
    html = get(url).text

    # Debug info.
    if VERBOSE:
        print('Successfully scrapped class page for %s %d' % (subject, num))

    # Return the scrapped data.
    return html