# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-5

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yellow': 'china',
}

for river, location in rivers.items():
    print('The ' + river.title() + ' river, runs through ' + location.title() + '.')

print('\n')
for river in rivers.keys():
    print(river.title())

print('\n')
for location in rivers.values():
    print(location.title())
