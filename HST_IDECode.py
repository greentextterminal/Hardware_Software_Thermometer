import requests
from bs4 import BeautifulSoup
import time


def destroy():
    print('cleanup function call')


T = True
F = False

table = {'0': [F, F, F, F],
         '1': [F, F, F, T],
         '2': [F, F, T, F],
         '3': [F, F, T, T],
         '4': [F, T, F, F],
         '5': [F, T, F, T],
         '6': [F, T, T, F],
         '7': [F, T, T, T],
         '8': [T, F, F, F],
         '9': [T, F, F, T]
         }

# dictionary to hold cities for temp data parsing
weather_urls = {'Houston': 'https://weather.com/weather/today/l/Houston+TX?canonicalCityId'
                           '=e7763a6187b4cb5fd0f85ad30c23f37f320bfe7e910e6fdbe90b501f206d265c',
                'San Diego': 'https://weather.com/weather/today/l/San+Francisco+CA?canonical'
                             'CityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c',
                'New York': 'https://weather.com/weather/today/l/New+York+City+NY?canonicalCityId'
                            '=a701ee19c4ab71bbbe2f6ba2fe8c250913883e5ae9b8eee8b54f8efbdb3eec03'}

try:
    selection = weather_urls[input('Enter a city to view current temp: ')]

    while True:
        active_link = selection
        # pulls the info
        source = requests.get(active_link, 'lxml').text
        # make an object with parsed html data
        soup = BeautifulSoup(source, 'lxml')
        # have a general location of all div types
        general_html_location = soup.find('div')
        # find in general the temp
        temp_line = general_html_location.find(class_='CurrentConditions--tempValue--3a50n').text
        split_data = temp_line.split('°')
        temp = split_data[0]
        # print(time_line)
        string = temp
        print(string)
        container = []
        for val in string:
            for x in table:
                if val == x:
                    line = table[x]
                    container.append(line)


        def num1():
            print(container[0][0])
            print(container[0][1])
            print(container[0][2])
            print(container[0][3])


        def num2():
            print(container[1][0])
            print(container[1][1])
            print(container[1][2])
            print(container[1][3])

        num1()
        num2()
        time.sleep(10)

except:
    pass
finally:
    destroy()
