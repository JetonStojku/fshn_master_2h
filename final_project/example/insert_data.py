import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_schema import Race, Pilot, RacePilotResult, PilotTime
from final_project.example.utils import *

# Load data from JSON file
with open('formula_one.json', 'r') as f:
    data = json.load(f)

# Create SQLAlchemy engine
engine = create_engine('sqlite:///formula_one.db')

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into database
race_i = 0
pilot_time_i = 0
for race_data in data:
    race = Race(id=race_data['id'], location=race_data['location'])
    session.add(race)
    session.flush()
    pilot_converted_data = convert_to_pilots_list_with_fastest_times_race_time(race_data['pilots'])
    fastest_times_pilot_position = convert_to_dictionary_pilot_fastest_times_position(pilot_converted_data)
    race_times_pilot_position = convert_to_dictionary_pilot_race_time_position(pilot_converted_data)
    for j, pilot_data in enumerate(race_data['pilots']):
        pilot = Pilot(**convert_to_pilots_data(pilot_data))
        session.add(pilot)
        session.flush()

        race_i += 1
        race_pilot_result = RacePilotResult(id=race_i, race_id=race.id, pilot_id=pilot.id)
        session.add(race_pilot_result)

        fastest_times = []
        race_times = []
        for time_data in pilot_data['fastest_time']:
            pilot_time_i += 1
            pilot_time = PilotTime(id=pilot_time_i, time=time_data, time_type='fastest',
                                   race_pilot_result_id=race_pilot_result.id)
            session.add(pilot_time)
            session.flush()

        for time_data in pilot_data['laps_time']:
            pilot_time_i += 1
            pilot_time = PilotTime(id=pilot_time_i, time=time_data, time_type='lap',
                                   race_pilot_result_id=race_pilot_result.id)
            session.add(pilot_time)
            session.flush()

        race_pilot_result.fastest_time = min(pilot_data['fastest_time'])
        race_pilot_result.race_time = sum(pilot_data['laps_time'])
        race_pilot_result.fastest_position = fastest_times_pilot_position[pilot.id]
        race_pilot_result.race_position = race_times_pilot_position[pilot.id]

# Commit the transaction to save the data
session.commit()

# Close session
session.close()
