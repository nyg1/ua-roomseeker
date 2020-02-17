#!/bin/bash

# This project is licenced under the MIT licence.

# Starting point of a lot of the functionality.
# Either start web scrapping, run the server, or populate the database.

# Usage: ./seeker.sh [server|scrape|populate]


# Global constants.
export FLASK_APP="app/server.py"
export FLASK_ENV="development"


# Handle each sub command.
case $1 in
    server) flask run ;;
    scrape) python3 web_scraping/scraping.py ;;
    populate) echo "populate!" ;;
    *) echo "Invalid command. Usage: ./seeker.sh [server|scrape|populate]"
esac
#flask run