#!/usr/bin/python

from os import remove, listdir
from os.path import isdir
from re import match

current = ['.']
next = []

while len(current) != 0:
	for c in current:
		for o in listdir(c):
			if match(r'.*\.pyc$', o):
				remove(c + '/' +  o)
			elif match(r'^\._.*', o):
				remove(c + '/' +  o)
			elif isdir(c + '/' +  o):
				next.append(c + '/' +  o)
	current = next
	next = []
