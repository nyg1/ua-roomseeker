#!/bin/bash

# This project is licenced under the MIT licence.

# Starting point of the entire project.
# Run the server, start web scraping, etc.


# Global constants.
export FLASK_APP="app/server.py"
export FLASK_ENV="development"

# Comment this out for now.
# # Handle each sub command.
# case $1 in
#     server) flask run ;;
#     scrape) python3 web_scraping/scraping.py ;;
#     populate) echo "populate!" ;;
#     *) echo "Invalid command. Usage: ./seeker.sh [server|scrape|populate]"
# esac