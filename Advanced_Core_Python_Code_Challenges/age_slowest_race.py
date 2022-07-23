# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

import re
from datetime import datetime

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    race_time = re.findall(r'\d{2}:\d{2}', line)
    match = re.findall(r'\d{2} \w{3} \d{4}', line)
    race_date = datetime.strptime(match[0], r'%d %b %Y')
    birth_date = datetime.strptime(match[1], r'%d %b %Y')
    age = race_date - birth_date
    return (age, race_time)
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    events = []
    for line in races.splitlines():
        if "Jennifer Rhines" in line:
            events.append(get_event_time(line))
    event = max(events, key=lambda x: x[1])
    age_days = event[0].days
    y, d = divmod(age_days, 365.25)
    age = f'{str(int(y))}y{str(int(d))}d'
    return age, event[1][0]


if __name__ == "__main__":
    age, time = get_age_slowest_times()
    print(age, time)
