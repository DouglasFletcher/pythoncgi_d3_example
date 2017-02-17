#!/usr/bin/python

print "Content-Type: text/html\n\n".encode('utf-8')

# get connection
import sys
import MySQLdb
import json
import collections
import cgi

# define function
def PrintFields(database, table1):
	# get post data
	data = cgi.FieldStorage()
	# connection params
	host="79.170.44.86"
	user="cl40-exchanger"
	password = "exchanger"
	# connection obj
	conn = MySQLdb.Connection(db=database, host=host, user=user, passwd=password)
	cursor = conn.cursor()

	# select statement
	sql = """SELECT * FROM %s """ % (table1)

	# get data
	cursor.execute(sql)
	fields= cursor.fetchall()

	# data to json
	objList = []
	for field in fields:

		d = collections.OrderedDict()
		d['period'] = str(field[0])

		# get exchange rate based on user input
		if data['result'].value == "1":
			d['values'] = field[1]
		elif data['result'].value == "2":
			d['values'] = field[2]
		else:
			print "error recieving user input"
			break

		# collect data
		objList.append(d)

	# rounding
	json.encoder.FLOAT_REPR = lambda f: ("%.2f" % f)

	print json.dumps(objList)

	# close connection
	cursor.close()
	conn.close()

# params
database="cl40-exchanger"
table1 ="ExchangeRates"

# execute
PrintFields(database, table1)
