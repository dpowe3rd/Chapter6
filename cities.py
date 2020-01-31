# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 6-11

cities = {
    'tokyo': {
        'country': 'japan',
        'population': '13,900,000',
        'fact': 'The cherry blossom is the national symbol of Japan. In April, the trees flower for two weeks, this'
                ' period is known as Hanami.',
    },
    'sydney': {
        'country': 'australia',
        'population': '5,100,000',
        'fact': 'It was in the Guinness Book of Records for producing the longest line of pizzas at 221 metres in the '
                'Italian quarter of Leichardt.',
    },
    'paris': {
        'country': 'france',
        'population': '2,141,000',
        'fact': 'The Paris Metro system doesn\'t announce their steps like most major cities. So don’t fall asleep on '
                'your commute – who knows where you could wake up!',
    }
}

for city, city_info in cities.items():
    print('\nThe city of ' + city.title() + ', is a wonderful city located in ' + city_info['country'].title() + '.\n'
          + 'Approximately, ' + city_info['population'] + ' people live in ' + city.title() + ' today! ' +
          'Here\'s a fun fact about ' + city.title() + ':\n'
          '\t' + city_info['fact'])
