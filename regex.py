import re, io

def init_regex():
	'''
	Initialize regex objects to parse HTML pages.
	The first object is for parsing course listings, and the second is for
	parsing a course page.

	Returns:
		tuple - A tuple of the two objects.
	'''

	# Initialize regex objects.
	course_expr = re.compile(r'[A-Z]+\s*[A-Z]*\s*[A-Z]*\s[1-9]{3,}')
	#class_expr = re.compile(r'[A-Z]+\s*[A-Z]*\s*[A-Z]*\s[1-9]{3,}')

	# Return tuple of each case.
	# return (course_expr, class_expr)
	return course_expr

def parse_course_list(expr, file_name):
	'''
	Given regex object and file, open and parse the HTML to get a course list.

	Arguments:
		- expr (regex): Regex object.
		- file_name (string): The file name.  
	
	Returns:
		- (list): A list of the course names, where each is a tuple of the
				  subject and course number.
	'''

	# Verify data types.
	if not str(expr) == 're.compile(r\'[A-Z]+\\s*[A-Z]*\\s*[A-Z]*\\s[1-9]{3,}\')':

	# Initialize final course list.
	courses = []

	# Read through the file, collecting the courses.
	with io.open(file_name, 'r', 1) as fin:
		while True:
			line = fin.readline()

			if not line:
				break

			# Break up the courses into subject and number, then add to list.
			for c in expr.findall(line):
				sep = c.rfind(' ')
				subject, num = c[:sep], c[sep + 1:]

				courses.append((subject, num))

	# Return course list.
	return courses

print(parse_course_list(init_regex(), 'html_file'))



