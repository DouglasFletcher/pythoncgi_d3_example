
# create dbscheme
from sqlalchemy import create_engine
from src.dbSchema import Base
from sqlalchemy.orm import sessionmaker

class DBCreate:

	def __init__(self, username, password, server):
		self.username = username
		self.password = password
		self.server = server
		self.engine = None
		self.session = None

	def getEngine(self):
		return self.engine

	def getSession(self):
		return self.session

	def getServer(self):
		return self.server

	def engineCreate(self):
		print "\n creating db engine ... \n"
		self.engine = create_engine('mysql+mysqldb://'+str(self.username) \
		+":"+str(self.password)+"@"+str(self.server), echo=True)

	def dbRefresh(self):
		print "clearing all tables from db ... \n"
		Base.metadata.drop_all(self.engine, checkfirst=True)

	def schemaCreate(self):
		print "\n creating database schema ... \n"
		Base.metadata.create_all(self.engine)

	def sessionCreate(self):
		print "\n creating session object ... \n"
		Session = sessionmaker(bind=self.engine)
		self.session = Session()

