from collections import namedtuple

with open('olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.read()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals = [] #Complete this - medals is a list of medal namedtuples

def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    medals = [medal._make(line.split(";")) for line in olympics.splitlines()]
    meds = medals
    for key, val in kwargs.items():
        meds = [x for x in meds if getattr(x, key) == val]
    return meds

if __name__ == "__main__":
    print(len(get_medals(Edition='1984')))
    """ [medal(City='Los Angeles', Edition='1984', Sport='Athletics', Discipline='Athletics', Athlete='LEWIS, Carl', NOC='USA', Gender='Men', Event='100m', Event_gender='M', Medal='Gold'),
              medal(City='Seoul', Edition='1988', Sport='Athletics', Discipline='Athletics', Athlete='LEWIS, Carl', NOC='USA', Gender='Men', Event='100m', Event_gender='M', Medal='Gold')]"""
