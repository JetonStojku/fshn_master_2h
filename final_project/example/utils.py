# Add needed functions to use in the insert_data.py
from datetime import datetime


def sort_pilots_by_fastest_time(pilots):
    return sorted(pilots, key=lambda pilot: pilot['fastest_time'])


def convert_to_dictionary_pilot_fastest_times_position(pilots):
    return {pilot['pilot_id']: i + 1 for i, pilot in enumerate(sort_pilots_by_fastest_time(pilots))}


def sort_pilots_by_race_time(pilots):
    return sorted(pilots, key=lambda pilot: pilot['race_time'])


def convert_to_dictionary_pilot_race_time_position(pilots):
    return {pilot['pilot_id']: i + 1 for i, pilot in enumerate(sort_pilots_by_race_time(pilots))}


def convert_to_pilots_list_with_fastest_times_race_time(pilots):
    return [{'pilot_id': pilot_data['id'], 'fastest_time': min(pilot_data['fastest_time']),
             'race_time': sum(pilot_data['laps_time'])} for pilot_data in pilots]


def convert_to_pilots_data(data):
    return {
        'id': data['id'],
        'email': data['email'],
        'username': data['username'],
        'first_name': data['profile']['name'].split()[0],
        'last_name': data['profile']['name'].split()[1],
        'company': data['profile']['company'],
        'dob': datetime.strptime(data['profile']['dob'], '%Y-%m-%d'),
        'about': data['profile']['about']
    }
