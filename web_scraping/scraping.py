# This project is licenced under the MIT licence.

# Imports.
from json import dumps
import util, regex
from copy import deepcopy
from time import sleep


# Place to store the final JSON data.
DATA_DIR = '../data/'

# Debug flag.
VERBOSE = True


def main():
	'''
	Main function, guides execution of the web scraping.
	'''

	# First, initialize regex.
	course_regex, class_regex = util.init_regex()
	
	# Get raw data first, then parse it.
	raw_courses = scraping.scrape_courses()
	courses = util.parse_courses(course_regex, raw_courses)

	# Initialize master dictionary.
	all_data = {}

	# Scrape each course page and construct each building JSON.
	for c in courses:
		raw_class = scraping.scrape_class(c[0], c[1])
		new_times = util.parse_class(class_regex, raw_class)

		# Loop through each new time and add it to master dictionary.
		for j in new_times:
			add_time(all_data, j)

		# Debug info.
		if VERBOSE:
			print('Scrapped the course:', c[0], c[1])

		# To not time out. :)
		sleep(0.06)

	all_data = invert_times(all_data)

	# Write the building data to each JSON file.
	for building in all_data:
		write_building(building, all_data[building])


def add_time(data, entry):
	'''
	Add a time entry to the master data dictionary.

	Arguments:
		- data (dict): Master dictionary of all the data.
		- entry (dict): Specific time entry to add.
	'''

	# For brevity, shorten variable names.
	building, day, room, time = entry['building'], entry['day'], entry['room'], entry['time']

	# Add a building if its not in the master dictionary.
	if building not in data:
		data[building] = { 'M' : {}, 'T' : {}, 'W' : {},
									'R' : {}, 'F' : {}}

	# Add a room if its not in the master dictionary.
	if room not in data[building][day]:
		for d in data[building]:
			data[building][d][room] = []

	# Add the specific time interval and make sure its sorted.
	if time not in data[building][day][room]:
		data[building][day][room].append(time)
		data[building][day][room].sort()


def invert_times(data):
	'''
	Inverts the time for the master dictionary to get all times that are available.

	Arguments:
		- data (dict): Master dictionary of all the data.

	Returns:
		- (dict): Inverted version of the data.
	'''

	# First get a deepcopy of the data, to remove references.
	inverted = deepcopy(data)

	# Loop through each room and invert the times.
	for building in data:
		for day in data[building]:
			for room in data[building][day]:
				inverted[building][day][room] = []

				# Go from 7:00 to 20:00.
				for time in range(420, 1200, 30):
					if time not in data[building][day][room]:
						inverted[building][day][room].append(time)

	return inverted


def write_building(name, data):
	'''
	Write a given building and its data to a JSON file.

	Arguments:
		- name (dict): Building name.
		- data (dict): Building data.
	'''

	# Convert data to JSON format.
	json_data = dumps(data, indent=4)

	# Open the file and write the data.
	with open(DATA_DIR + name + '.json', 'w') as fout:
		for line in json_data:
			fout.write(line)


# Entry point for the program.
if __name__ == "__main__":
	main()