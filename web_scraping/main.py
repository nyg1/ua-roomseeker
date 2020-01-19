# (c) Noah Gergel, Sichun Xu, Weilin Qiu, Nina Yang 2020

# Imports.
import util, scraping


def main():
	'''
	Main function, guides execution of the web scraping.
	'''

	# First, initialize regex.
	course_regex, class_regex = util.init_regex()
	
	# Get raw data first, then parse it.
	raw_courses = scraping.scrape_courses()
	courses = util.parse_courses(course_regex, raw_courses)

	print(util.parse_class(class_regex, scraping.scrape_class('MATH', 100)))


# Entry point for the program.
if __name__ == "__main__":
	main()