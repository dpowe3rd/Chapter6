# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-10

favorite_numbers = {
    'keyante': {
        'first': int('9'),
        'second': int('5'),
        'third': int('11'),

    },
    'darrell': {
        'first': int('13'),
        'second': int('69'),
        'third': int('21'),
    },
    'robert': {
        'first': int('10000'),
        'second': int('224'),
        'third': int('556'),
    },
    'riley': {
        'first': int('98'),
        'second': int('13'),
        'third': int('90'),
    },
    'huey': {
        'first': int('69'),
        'second': int('420'),
        'third': int('11'),
    },


}

for name, numbers in favorite_numbers.items():
    print('My name is ' + name.title() + ' and my numbers, not in order are: \n'
          '\t' + str(numbers['first']) + '\n' +
          '\t' + str(numbers['second']) + '\n' +
          '\t' + str(numbers['third']))
