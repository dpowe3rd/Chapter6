# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-8

penny = {
    'name': 'penny',
    'animal': 'rabbit',
    'owner': 'robert',
}

butters = {
    'name': 'butters',
    'animal': 'cat',
    'owner': 'keyante',
}

henny = {
    'name': 'henny',
    'animal': 'cat',
    'owner': 'darrell',
}

frank = {
    'name': 'frank',
    'animal': 'cat',
    'owner': 'darrell',
}

tiny = {
    'name': 'tiny',
    'animal': 'turtle',
    'owner': 'sophia',
}

pets = [penny, butters, henny, frank, tiny]

for pet in pets:
    print(pet['owner'].title() + ' owns a pet ' + pet['animal'] +
          ' named, ' + pet['name'].title() + '!')
