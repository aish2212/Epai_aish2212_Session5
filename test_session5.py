import pytest
import random
import string
import session5
import os
import inspect
import re
import math, cmath
from timeit import default_timer as timer

SIDES = random.choice([3, 4, 5, 6])
LENGTH = random.randint(1, 100)
TEMP = random.uniform(-100, 100)
NUMBER = 5
RANDOM_NUMBER = random.randint(1, 20)
START = random.randint(1, 10)
END = random.randint(11, 20)
SPEED = random.uniform(1, 100)

README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter', 
]

#1
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

#2
def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

#3
def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

#4    
def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

#5
def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

#6
def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

#7		
def test_functions_list():
    code_lines = inspect.getsource(session5)
    assert 'time_it' in code_lines, 'time_it function is not present'
    assert 'squared_power_list' in code_lines, 'squared_power_list function is not present'
    assert 'temp_converter' in code_lines, 'temp_converter function is not present'
    assert 'polygon_area' in code_lines, 'polygon_area function is not present'
    assert 'speed_converter' in code_lines, 'speed_converter function is not present'

#time_it
#8   
def test_time_import_or_not():
    code_lines = inspect.getsource(session5)
    assert 'timer' in code_lines, 'timer not used! You must use timer for calc time'

#9
def test_time_it_call():
    q1 = session5.time_it(session5.speed_converter, 100, 'm', 's', repetitons=5)
    q2 = session5.time_it(session5.temp_converter, 100, 'F', repetitons=5)
    q3 = session5.time_it(session5.squared_power_list, 5, 0, 7, repetitons=5)
    q4 = session5.time_it(session5.polygon_area, 5,3, repetitons=5)
    q5 = session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)
    assert q1 >0, 'time not calculated'
    assert q2 >0, 'time not calculated'
    assert q3 >0, 'time not calculated'
    assert q4 >0, 'time not calculated'
    assert q5 >0, 'time not calculated'

#squared_power_list    
#10
def test_squared_power_list_valid_number():
    q1=session5.squared_power_list(-10,0,5)
    assert q1=='select valid number'
    
#11
def test_squared_power_list_invalid_list_range():
    q1=session5.squared_power_list(10,5,3)
    assert q1=='start value should be less than end'

#12
def test_squared_power_list_calculations():
    q1=session5.squared_power_list(NUMBER,0,7)
    assert q1 == [1, 5, 25, 125, 625, 3125, 15625, 78125]

#13
def test_squared_power_list_invalidnumber_listrange():
    q1=session5.squared_power_list(-10,5,3)
    assert q1=='select valid number and proper range of the list'
    
#14
def test_squared_power_list_valid_range():
    q1=session5.squared_power_list(RANDOM_NUMBER,START,END)
    assert len(q1) == ((END-START)+1)

#Temperature converter    
#15        
def test_valid_temperature_range_and_scale():
    q1=session5.temp_converter(5,'d')
    assert q1=='Please enter the correct temperature units'
    
#16 
def test_valid_temperature_Celsius_converter():
    temp = ((TEMP-32) * (5/9))
    q1=session5.temp_converter(TEMP,'f')
    q2=session5.temp_converter(TEMP,'F')
    assert math.isclose(q1, temp, rel_tol=1e-4)
    assert math.isclose(q2, temp, rel_tol=1e-4)

#17
def test_valid_temperature_Fahrenheit_converter():
    temp = ((TEMP*(9/5))+32)
    q1=session5.temp_converter(TEMP,'c')
    q2=session5.temp_converter(TEMP,'C')
    assert math.isclose(q1, temp, rel_tol=1e-4)
    assert math.isclose(q2, temp, rel_tol=1e-4)

#POLYGON AREA
#18
def test_polygon_area_valid_length():
    q1=session5.polygon_area(-2,4)
    assert q1=='Please enter valid length of the sides'
    
#19
def test_polygon_area_valid_sides():
    q1=session5.polygon_area(2,2)
    assert q1=='Please enter number of sides in range of 3 to 6'

#20   
def test_polygon_area_invalid_sides_length():
    q1=session5.polygon_area(-2,2)
    assert q1=='Please enter valid length and valid number of sides'
    
#21
def test_polygon_area_calculation():
    area = ((SIDES * LENGTH**2) / (4*math.tan(math.pi/SIDES)))
    q1=session5.polygon_area(LENGTH,SIDES)
    assert math.isclose(q1, area, rel_tol=1e-4) 

#speed converter    
#22
def test_validity_speed():
    q1=session5.speed_converter(-100,dist='m', time='s')
    assert q1=='The speed have to be of positive value'
    
#23
def test_speed_converter_dist_time_format():
    q1=session5.speed_converter(SPEED,dist='h', time='v')
    assert q1=='The format of distance or time is wrong'
    
#24
def test_speed_converter_kilometre_ms_s_m_hr_day():
    q1=session5.speed_converter(SPEED,dist='km', time='ms')
    q2=session5.speed_converter(SPEED,dist='km', time='s')
    q3=session5.speed_converter(SPEED,dist='km', time='m')
    q4=session5.speed_converter(SPEED,dist='km', time='day')
    assert q1 == (SPEED * 1)/3600000,'Wrong speed conversion'
    assert q2 == (SPEED * 1)/3600,'Wrong speed conversion'
    assert q3 == (SPEED * 1)/60,'Wrong speed conversion'
    assert q4 == (SPEED * 1)/0.041666667,'Wrong speed conversion'

#25
def test_speed_converter_metre_ms_s_m_hr_day():
    q1=session5.speed_converter(SPEED,dist='m', time='ms')
    q2=session5.speed_converter(SPEED,dist='m', time='s')
    q3=session5.speed_converter(SPEED,dist='m', time='m')
    q4=session5.speed_converter(SPEED,dist='m', time='day')
    q5=session5.speed_converter(SPEED,dist='m', time='hr')
    assert q1 == (SPEED * 1000)/3600000,'Wrong speed conversion'
    assert q2 == (SPEED * 1000)/3600,'Wrong speed conversion'
    assert q3 == (SPEED * 1000)/60,'Wrong speed conversion'
    assert q4 == (SPEED * 1000)/0.041666667,'Wrong speed conversion'
    assert q5 == (SPEED * 1000)/1,'Wrong speed conversion'

#26
def test_speed_converter_ft_ms_s_m_hr_day():
    q1=session5.speed_converter(SPEED,dist='ft', time='ms')
    q2=session5.speed_converter(SPEED,dist='ft', time='s')
    q3=session5.speed_converter(SPEED,dist='ft', time='m')
    q4=session5.speed_converter(SPEED,dist='ft', time='day')
    q5=session5.speed_converter(SPEED,dist='ft', time='hr')
    assert q1 == (SPEED * 3280.8399)/3600000,'Wrong speed conversion'
    assert q2 == (SPEED * 3280.8399)/3600,'Wrong speed conversion'
    assert q3 == (SPEED * 3280.8399)/60,'Wrong speed conversion'
    assert q4 == (SPEED * 3280.8399)/0.041666667,'Wrong speed conversion'
    assert q5 == (SPEED * 3280.8399)/1,'Wrong speed conversion'

#27
def test_speed_converter_yard_ms_s_m_hr_day():
    q1=session5.speed_converter(SPEED,dist='yrd', time='ms')
    q2=session5.speed_converter(SPEED,dist='yrd', time='s')
    q3=session5.speed_converter(SPEED,dist='yrd', time='m')
    q4=session5.speed_converter(SPEED,dist='yrd', time='day')
    q5=session5.speed_converter(SPEED,dist='yrd', time='hr')
    assert q1 == (SPEED * 1093.6133)/3600000,'Wrong speed conversion'
    assert q2 == (SPEED * 1093.6133)/3600,'Wrong speed conversion'
    assert q3 == (SPEED * 1093.6133)/60,'Wrong speed conversion'
    assert q4 == (SPEED * 1093.6133)/0.041666667,'Wrong speed conversion'
    assert q5 == (SPEED * 1093.6133)/1,'Wrong speed conversion'

	


        
