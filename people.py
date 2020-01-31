# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-7

Johnny = {
    'first': 'john',
    'last': 'doe',
    'age': '20',
    'location': 'new york city',
}

Bob = {
    'first': 'robert',
    'last': 'johnson',
    'age': '28',
    'location': 'san francisco',
}

Jenny = {
    'first': 'jennifer',
    'last': 'lopez',
    'age': '40',
    'location': 'miami',
}

people = [Johnny, Bob, Jenny]

for name in people:
    print('This is ' + name['first'].title() + ' ' + name['last'].title() +
          '. They moved to ' + name['location'].title() + ' when they were ' + name['age'] + ' years old.')
