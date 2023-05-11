import RPi.GPIO as GPIO
from bs4 import BeautifulSoup
import time
import requests

# If you wish to exit the program use Ctrl + C (this is a keyboard interrupt) 

# pins being used on the RPi 
# PINS 7, 11, 13, 15
# PINS 31, 33, 35, 37

# function to clean up pin channels after definition 
def destroy():
    print("Destroy called, cleaning pin channels...")
    GPIO.cleanup()
    print("Succesful pin clean")

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

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
        # find in general the tem
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
            GPIO.output(7, container[0][0])
            GPIO.output(11, container[0][1])
            GPIO.output(13, container[0][2])
            GPIO.output(15, container[0][3])

        def num2():
            GPIO.output(31, container[1][0])
            GPIO.output(33, container[1][1])
            GPIO.output(35, container[1][2])
            GPIO.output(37, container[1][3])        

        num1()
        num2()
        time.sleep(10)
        
except:
    pass
finally:
    destroy()
