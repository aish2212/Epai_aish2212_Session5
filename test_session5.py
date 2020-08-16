import pytest
import random
import string
import session5
import os
import inspect
import re
import math, cmath

import decimal
from decimal import Decimal

ZERO_INPUT_VALUE = 0
INPUT_VALUE_1 = Decimal(random.choice([-1, 1, 0]))
INPUT_VALUE_2 = Decimal(random.choice([-1, 1, 0]))

README_CONTENT_CHECK_FOR = [
    'Qualean',
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__',
]

FUNCTION_LIST = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__'
    '__add__'
    '__eq__'
    '__float__'
    '__ge__'
    '__gt__'
    '__invertsign__'
    '__le__'
    '__lt__'
    '__mul__'
    '__sqrt__'
    '__bool__'
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
    ALL_FUNCTIONS_PRESENT = True
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        if function not in FUNCTION_LIST:
            assert ALL_FUNCTIONS_PRESENT == False, "You have not added all the functions/class"
        else:
            ALL_FUNCTIONS_PRESENT == True
