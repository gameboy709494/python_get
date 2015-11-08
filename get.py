#!/usr/bin/env python2

import urllib2

from bs4 import BeautifulSoup

from HTMLParser import HTMLParser


request = urllib2.Request("http://www.ishadowsocks.com")
file = urllib2.urlopen(request)
content = file.read()

#print content


soup = BeautifulSoup(content)

sections = soup.find_all("section")

print sections


last_a_tag = soup.find("section", id="free")
print last_a_tag

#class SSServer:
#	def __init__(self, address, port, password):
#		self.address = address
#		self.port = port
#		self.password = password
#	def __init__(self):
#		self.address = "null"
#		self.port = 0
#		self.password = "null"
#
#
#class MyHTMLParser(HTMLParser):
#	def handle_starttag(self, tag, attrs):
#		if tag == 'section':
#			for name,value in attrs:
#				if name == 'id' and value == "free":
#					#The tag contain what i want.
#					print "hello!!"
#
#
#

#result_list = [] 
#my = MyHTMLParser()
#my.feed(content)
