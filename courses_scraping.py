import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

course_url = "https://calendar.ualberta.ca/content.php?catoid=29&navoid=7430"

uClient = uReq(course_url)

course_html = uClient.read()
uClient.close()

course_parser = soup(course_html, "html.parser")
uClient.close()

print("course_parser")
