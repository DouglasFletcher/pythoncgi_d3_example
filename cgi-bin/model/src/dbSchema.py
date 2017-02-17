

# dependencies
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

# base class
Base = declarative_base()

# expenditure table
class ExchangeRates(Base):

	__tablename__ = 'ExchangeRates'

	period = Column(Date, nullable=False, primary_key=True)
	gbpeur = Column(Float, nullable=False)
	gbpaud = Column(Float, nullable=False)

	def __str__(self):
		return "<ExchangeRates(period='%s', gbpeur='%s', gbpaud='%s')>" \
			%( self.period, self.gbp, self.gbpaud)
