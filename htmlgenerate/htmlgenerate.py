# coding=utf-8
# Mars Simulation Project
# Script for making the HTML5 user guide files for resources and processes
# replaces the previous java-based internal code
# htmlgenerate.py
# @version 3.08 2015-08-14
# @author Lars Næsbye Christensen
#
# Usage : 'python htmlgenerate.py [xmldir] [htmldir]' 
# must match the current '-help' functionality currently in the Java code

from xml.dom.minidom import Document

import sys

# TODO: 
# we should check for empty args
# Parse the XML nodes properly
# include the existing CSS
xmldir = sys.argv[1]; # path to XML source file 

# Open our sample file
f = open('resources.xml')
g = open('resources.html','w')

lines = f.readlines() # read the lines

docheader ="<!DOCTYPE html>\n<html>\n<head>\n<title>Generic Title</title>\n</head>\n<!-- generated by htmlgenerate.py -->\n<meta charset=utf-8 /><body>\n"
docfooter ="</body>\n</html>\n"

for line in lines:
	if line == "\n":
		print "Skipped empty line..."  # ignore empty lines
	else:
		print line
f.close()
g.write(docheader)
g.write(docfooter)
g.close()
