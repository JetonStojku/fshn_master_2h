# Import the necessary libraries
import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Enum, Date
from sqlalchemy.ext.declarative import declarative_base

# Create an engine to connect to the database
engine = create_engine('sqlite:///formula_one.db', echo=True)

# Create a base class for declarative models
Base = declarative_base()


class PilotTimeType(enum.Enum):
    fastest = 'fastest'
    lap = 'lap'


class Race(Base):
    __tablename__ = 'races'

    id = Column(String, primary_key=True)
    location = Column(String)


class Pilot(Base):
    __tablename__ = 'pilots'

    id = Column(String, primary_key=True)
    email = Column(String)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    company = Column(String)
    dob = Column(Date)
    about = Column(String)


class RacePilotResult(Base):
    __tablename__ = 'race_pilot_results'

    id = Column(Integer, primary_key=True)
    race_id = Column(String, ForeignKey('races.id'))
    pilot_id = Column(String, ForeignKey('pilots.id'))
    fastest_time = Column(Float)
    race_time = Column(Float)
    fastest_position = Column(Integer)
    race_position = Column(Integer)

    race_id = Column(String, ForeignKey('races.id'))
    pilot_id = Column(String, ForeignKey('pilots.id'))


class PilotTime(Base):
    __tablename__ = 'pilot_times'

    id = Column(String, primary_key=True)
    time = Column(Float)
    time_type = Column(Enum(PilotTimeType))
    race_pilot_result_id = Column(Integer, ForeignKey('race_pilot_results.id'))


# Create the table
Base.metadata.create_all(engine)
