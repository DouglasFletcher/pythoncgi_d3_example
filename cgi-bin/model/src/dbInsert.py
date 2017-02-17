
# -*- coding: utf-8 -*-
from src.dbSchema import Base, ExchangeRates
import datetime
import Quandl


class DBInsert:

	def __init__(self, dbCreate, startDate):

		self.dbCreate = dbCreate
		self.startDate = startDate
		self.rawData = []

	def extractData(self):
		#------------------------------
		#-- extract rawdata from quandl
		#------------------------------

		print "extracting data from quandl ... \n"

		# get data
		dataGbpAud = Quandl.get("BOE/XUDLADS", trim_start=self.startDate)
		dataEurGbp = Quandl.get("BOE/XUDLSER", trim_start=self.startDate)

		print "preparing data ... \n"
		dataGbpAud.columns = ['gbpaud']
		dataGbpEur = 1 / dataEurGbp
		dataGbpEur.columns = ['gbpeur']
		dataExchange = dataGbpEur.merge(dataGbpAud
			, how='inner'
			, left_index=True
			, right_index=True
		)

		print "extracting rawdata ... \n"
		self.rawData = []
		# files with data
		for index, row in dataExchange.iterrows():
			rowval = ExchangeRates(period=index,gbpeur=row['gbpeur'],gbpaud=row['gbpaud'])
			self.rawData.append(rowval)

		print "rawdata extract complete. \n"

	def insertData(self):
		# get session
		sess = self.dbCreate.getSession()
		# commit changes
		try:
			print "\n inserting rawdata ...\n"
			sess.bulk_save_objects(self.rawData)
			sess.commit()
			print "\n committed " + str(len(self.rawData)) + " changes to rawdata. \n"
		except:
			sess.rollback()
			raise

