# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-9

favorite_places = {
    'keyante': {
        'first': 'my bed',
        'second': 'my car',
        'third': 'a soca concert',

    },
    'darrell': {
        'first': 'my computer desk',
        'second': 'the mall',
        'third': 'the movies',
    },
    'robert': {
        'first': 'the apple store',
        'second': 'the movies',
        'third': 'a football game',
    },

}

for name, favorites in favorite_places.items():
    print('My name is ' + name.title() + ' and my favorite places to be, in order are: \n'
          '\t' + favorites['first'].title() + '\n' +
          '\t' + favorites['second'].title() + '\n' +
          '\t' + favorites['third'].title() + '\n')
