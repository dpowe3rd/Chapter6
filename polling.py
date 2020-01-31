# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

print('\n')

new_poll = ['bob', 'john', 'jen', 'chris', 'sarah', 'natalie', 'ryan']

for poll in new_poll:
    if poll in favorite_languages:
        print(poll.title() + ', thank you for taking the poll.')
    else:
        print(poll.title() + ', please take the poll.')