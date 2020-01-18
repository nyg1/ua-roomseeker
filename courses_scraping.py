import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

for n in range(1, 74):
    course_url = "https://calendar.ualberta.ca/content.php?catoid=29&catoid=29&navoid=7430&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={}#acalog_template_course_filter".format(n)

    uClient = uReq(course_url)

    course_html = uClient.read()
    uClient.close()

    course_parser = soup(course_html, "html.parser")
    uClient.close()

    print(course_parser)
