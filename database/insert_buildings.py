# (c) Noah Gergel, Sichun Xu, Weilin Qiu, Nina Yang 2020

# Imports.
import json

f = open('files.txt', 'r')

while True:
	line = f.readline()

	if not line:
		break

	print('INSERT INTO buildings VALUES (%s);' % (line[:-6]))