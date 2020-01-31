# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-3 & 6-4

glossary = {
    'variable': 'a reserved memory location to store values.',
    'string': 'a sequence of characters.',
    'method': 'a function that “belongs to” an object.',
    'list': ' a data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
    'dictionary': 'an unordered collection of data values, used to store data values like a map, which unlike other.' 
    'Types that hold only single value as an element, Dictionary holds key:value pair.',
}

for words, meanings in glossary.items():
    print('A ' + words + ' in python is ' + meanings + '\n')
