# Assignment: EPAi Session 5, Functional Parameters

# Objective

Write a function which gives out average run time per call, such that it's definition is:
- def time_it(fn, *args, repetitons= 1, **kwargs): your code comes here.

We should be able to call it like this:
- time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5)
- time_it(squared_power_list, 2, start=0, end=5, repetitons=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
- time_it(polygon_area, 15, sides = 3, repetitons=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
- time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) # 100 is the base temperature given to be converted
- time_it(speed_converter, 100, dist='km', time='min', repetitons=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph

## Functions
# time_it
- This function provides the average run time per call.
- The input to the function are
  - function to be called
  - arguments of the function
  - Number of repetations of function called.

# squared_power_list
- This function provides the list of squared number.
- The input is the number you are calculating power of.
- For example if the number = 2, the squared list is 1, 2, 4, 8, 16, 32,...
- The other user inputs are start and end value of the list to be returned.

# polygon_area
- This function calculates the area of a polygon 
- Number of sides possible is of range 3 to 6
- The user input are:
   - Length of the side (length)
   - Number of sides (sides)
- Area of the polygon = (sides * length**2) / (4 * math.tan(math.pi / sides))

# temp_converter
- This is the temperature converter which converts the temperature given by the user from either Fahrenheit to Celsius or Celsius to Fahrenheit depending on the input from user.
- The input given by the user involves,
  - temperature value
  - temp given in whether 'f' or 'c'
- Fahrenheit to Celsius --> temp = (temp-32) * 5/9
- Celsius to Fahrenheit --> temp = (temp*(9/5))+32

# speed_converter
- This function calculates the area of a polygon maximum of sides = 6.
- The user input are:
   - Length of the side
   - Number of sides

## Tests

- test_readme_exists
	- test to check whether README.md file exists

- test_readme_contents
    - test whether the README.md file have description  
	
- test_readme_file_for_formatting
    - test whether the readme file have proper formatting 

- test_readme_proper_description
	- check if readme has all these fields "__and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__"

- test_indentations
    - check whether the source file have proper indentations and space according to PEP8

- test_function_name_had_cap_letter
	- test if the func name declared properly
	
- test_functions_list
    - test if all the function are declared such as "__and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__"
	
- test_time_import_or_not
    - test whether the timer module is imported or not.

- test_time_it_call
    - test whether the average run time is calculated or not.

- test_squared_power_list_valid_number
    - test whether valid number is given by user for squared_power_list function.
	
- test_squared_power_list_invalid_list_range
    - test whether valid range of list is given by user or not. i.e start value of the list must be less than the end.
	
- test_squared_power_list_calculations
    - test whether the squared_power_list function calculates the list of squared number properly or not.
	
- test_squared_power_list_invalidnumber_listrange
    - test the case when both the number and list range given are not proper.
	
- test_squared_power_list_valid_range
    - test whether number of list of squared numbers created is proper.

- test_valid_temperature_range_and_scale
    - test whether the temperature units given is proper, either 'c' or 'f'.
	
- test_valid_temperature_Celsius_converter
    - test whether the temperature in Fahrenheit is converted to temperature in Celsius.
	
- test_valid_temperature_Fahrenheit_converter
    - test whether the temperature in Celsius is converted to temperature in Fahrenheit.
	
- test_polygon_area_valid_length
    - test whether the length of the sides is greater than zero.
	
- test_polygon_area_valid_sides
    - test whether the number of sides is of proper.
	
- test_polygon_area_invalid_sides_length
    - test the case when both the number of sides and the length of the sides is not proper.
	
- test_polygon_area_calculation
    - test when the polygon area calculation is proper.
	
- test_validity_speed
    - test whether the speed is of positive value.
	
- test_speed_converter_dist_time_format
    - test whether the distance and time format given is proper and valid.
   
- test_speed_converter_kilometre_ms_s_m_hr_day
    - test speed conversion from 
	  - km/hr to km/ms 
	  - km/hr to km/s
	  - km/hr to km/m 
	  - km/hr to km/day is proper or not.
	  
- test_speed_converter_metre_ms_s_m_hr_day
    - test speed conversion from 
	  - km/hr to m/ms 
	  - km/hr to m/s
	  - km/hr to m/m 
	  - km/hr to m/day
      - km/hr to m/hr is proper or not.
	  
- test_speed_converter_ft_ms_s_m_hr_day
    - test speed conversion from 
	  - km/hr to ft/ms 
	  - km/hr to ft/s
	  - km/hr to ft/m 
	  - km/hr to ft/day 
	  - km/hr to ft/hr is proper or not.
	  
- test_speed_converter_yard_ms_s_m_hr_day
    - test speed conversion from 
	  - km/hr to yrd/ms 
	  - km/hr to yrd/s
	  - km/hr to yrd/m 
	  - km/hr to yrd/day 
	  - km/hr to yrd/hr is proper or not.
