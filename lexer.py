from sys import *

def open_file(filename):
	data = open(filename, "r").readlines()
	return data

def check(data):
	for line in data:
		if "showbitch" in line:
			show(line)
		elif "ifbitch" in line:
			ifbitch(line)
		elif "elsebitch" in line:
			elsebitch(line)

def show(data): #The print parser. 
	_,data,space = data.split("\"")
	print data
	
def ifbitch(data): #Writing the if parser. 
	print "Got it."

def elsebitch(data): #Witing the else parser.
	print "Again Got it"

def run():
	data = open_file(argv[1])
	check(data)

run()