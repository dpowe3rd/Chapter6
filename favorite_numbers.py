# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-2

favorite_numbers = {
    'Darrell': '13',
    'Keyante': '5',
    'Bob': '12',
    'Jade': '11',
    'Johnny': '18',
    'Carl': '70',
}

for name, num in favorite_numbers.items():
    print(name + '\'s favorite number is ' + num + '.')
