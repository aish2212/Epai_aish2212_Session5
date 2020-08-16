from timeit import default_timer as timer
import math


def time_it(fn, *args, repetitons=1, **kwargs):
    total_time = 0
    for i in range(1, repetitons+1):
        start = timer()
        fn(*args)
        end = timer()
        diff_time = end - start
        total_time += diff_time
    avg_time = total_time / repetitons
    return avg_time


def squared_power_list(number, start, end):
    '''
    This function provides the list of squared number.
    The input is the number you are calculating power of.
    For example if the number = 2, the squared list is 1, 2, 4, 8, 16, 32,...
    The other user inputs are start and end value of the list to be returned.
    '''
    squared_list = list()
    if number > 0 and start < end:
        for i in range(start, end+1):
            squared_list.append(number**i)
    elif number < 0 and start > end:
        squared_list = "select valid number and proper range of the list"
    elif start > end:
        squared_list = "start value should be less than end"
    elif number < 0:
        squared_list = "select valid number"
    return squared_list


def temp_converter(temp, temp_given_in):
    '''
    This is the temperature converter which converts the temperature given by the user from
    either Fahrenheit to Celsius or Celsius to Fahrenheit depending on the input from user.
    The input given by the user involves,
    - temperature value
    - temp given in whether 'f' or 'c'
    '''
    if(temp_given_in not in ('c', 'f', 'C', 'F')):
        temp = "Please enter the correct temperature units"
    elif(temp_given_in in ('f', 'F')):
        temp = (temp-32) * 5/9
    elif(temp_given_in in('c', 'C')):
        temp = (temp*(9/5))+32
    return temp


def polygon_area(length, sides):
    '''
    This function calculates the area of a polygon maximum of sides = 6.
    The user input are:
    - Length of the side
    - Number of sides
    '''
    if((sides < 3 or sides > 6) and length <= 0):
        area = "Please enter valid length and valid number of sides"
    elif(sides < 3 or sides > 6):
        area = "Please enter number of sides in range of 3 to 6"
    elif(length <= 0):
        area = "Please enter valid length of the sides"
    elif(length > 0 or (3 <= sides <= 6)):
        area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    return area


def speed_converter(speed, dist, time):
    '''
    This is a speed converter. It converts the speed of Kmph format to the format requested by the user.
    The user have to give the speed in Kmph.
    parameters include
    - speed given by the user.
    - distance unit to be converted. Possible distance units are 'km', 'm' , 'ft, 'yrd'.
    - time unit to be converted, Possible time units are 'ms', 's', 'm', 'hr', 'day'.
    '''
    if dist == 'm':
        d = 1000
    elif dist == 'ft':
        d = 3280.8399
    elif dist == 'yrd':
        d = 1093.6133
    elif dist == 'km':
        d = 1
    else:
        d = 0

    if time == 'ms':
        t = 3600000
    elif time == 's':
        t = 3600
    elif time == 'm':
        t = 60
    elif time == 'hr':
        t = 1
    elif time == 'day':
        t = 0.041666667
    else:
        t = 0

    if((d == 0) or (t == 0)):
        return "The format of distance or time is wrong"
    elif speed < 0:
        return "The speed have to be of positive value"
    else:
        speed = (speed * d)/t
        return speed
