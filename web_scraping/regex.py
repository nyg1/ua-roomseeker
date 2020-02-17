# This project is licenced under the MIT licence.

# Imports.
import re, io


# Regex for courses and classes.
COURSE_EXPR = r'[A-Z]+\s*[A-Z]*\s*[A-Z]*\s[1-9]{3,}'
CLASS_EXPR = r'([MTWRF]+\s([0-9]{2}:){2}[0-9]{2}\s-\s([0-9]{2}:){2}[0-9]{2}\s\([A-Z]+\s*[A-Z]*[\s0-9]+\))'


def init_regex():
	'''
	Initialize regex objects to parse HTML pages.
	The first object is for parsing course listings, and the second is for
	parsing a course page.

	Returns:
		- (tuple): A tuple of the two objects.
	'''

	# Initialize regex objects.
	course_reg, class_reg = re.compile(COURSE_EXPR), re.compile(CLASS_EXPR)

	# Return tuple of each case.
	return (course_reg, class_reg)


def parse_courses(expr, raw_data):
	'''
	Given regex object and file, open and parse the HTML to get a course list.

	Arguments:
		- expr (regex): Regex object.
		- raw_data (list): The raw data for course listings.  
	
	Returns:
		- (list): A list of the course names, where each is a tuple of the
				  subject and course number.
	'''

	# Verify data types.
	if str(type(expr)) != '<class \'_sre.SRE_Pattern\'>' \
	   or str(type(raw_data)) != '<class \'list\'>':
		raise TypeError

	# Initialize final course list.
	courses = []

	# Read through the raw_data, collecting the courses.
	for line in raw_data:
		# Loop through every match, and parse the string.
		for val in expr.findall(line):
			sep = val.rfind(' ')
			subject, num = val[:sep], val[sep + 1:]

			courses.append((subject, num))

	# Return course list.
	return courses


def parse_class(expr, raw_data):
	'''
	Given regex object and file, open and parse HTML to get a class' times.
	Then return the times it is available.

	Arguments:
		- expr (regex): Regex object.
		- raw_data (string): The raw data to process.  
	
	Returns:
		- (list): A list of dictionaries of the appropriate information.
	'''

	# Verify data types.
	if str(type(expr)) != '<class \'_sre.SRE_Pattern\'>' \
	   or str(type(raw_data)) != '<class \'str\'>':
		raise TypeError

	# Initialize final list of entries.
	times = []

	# Parse the class and add them to the list.
	for line in expr.findall(raw_data):
		val = line[0]

		# Seperate time and building information.
		time, building = val.split('(')
		building = building[:-1].split()
		room, building = '-'.join(building[1:]), building[0]

		# Split up time data.
		days, start, _, end = time.split()

		# Add each time segment to the list.
		for i in days:
			for j in get_time(start, end):
				time_seg = { "building" : building, "day": i,
							 "room": room, "time": j }
				times.append(time_seg)

	# Return course list.
	return times


def get_time(start, end):
	'''
	Given a start and end time, returns all 30 min time segments between them.

	Arguments:
		- start (string): Start time, in the format hh:mm:ss.
		- end (string): End time, in the format hh:mm:ss.

	Returns:
		- (list): List of time values, in minutes since the start of the day.
	'''

	# Convert time to integers.
	start_vals = list(map(int, start.split(':')))
	end_vals = list(map(int, end.split(':')))

	# Get time in minutes, ignore seconds.
	start_time = 60 * start_vals[0] + start_vals[1]
	end_time = 60 * end_vals[0] + end_vals[1]

	# Return list of time segments.
	return [i for i in range(start_time, end_time, 30)]




