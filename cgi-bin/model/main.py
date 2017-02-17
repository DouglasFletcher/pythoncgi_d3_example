

import Quandl
import datetime
from src.dbCreate import DBCreate
from src.dbInsert import DBInsert

if __name__ == "__main__":

	# trim start date: yyyy-mm-dd
	startDate = "2000-01-01"

	# create sql connection instance
	dbCreate = DBCreate(username='cl40-exchanger', password='exchanger'
	, server='79.170.44.86:3306/cl40-exchanger')
	# create engine
	dbCreate.engineCreate()
	# refresh metadata
	dbCreate.dbRefresh()
	# create schema object
	dbCreate.schemaCreate()
	# create session access
	dbCreate.sessionCreate()
	# tables create object
	dbInsert = DBInsert(dbCreate=dbCreate, startDate=startDate)
	# extract rawdata to db mapper
	dbInsert.extractData()
	# add data to database
	dbInsert.insertData()
