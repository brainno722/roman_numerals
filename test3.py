import re
import itertools

def roman_to_int(my_roman):
    lookup = {'I':1, 'IV':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman_list = list(my_roman.upper())[::-1]
    print(roman_list)
    for i in roman_list:
        if not lookup.get(i):
            print('Invalid characters')
            return

def int_to_roman(my_int):
    lookup = {'one': {'1':'I', '4':'IV', '5':'V', '9':'IX'}, 'ten': {'1':'X', '4':'XL', '5':'L', '9':'XC'},
              'hundred': {'1':'C', '4':'CD', '5':'D', '9':'CM'}, 'thousand': {'1':'M'}}
    int_list = list(my_int)[::-1]
    digit_list = ['one', 'ten', 'hundred', 'thousand']
    working_dict = dict(itertools.zip_longest(digit_list, int_list))
    roman_chars = []
    for k, v in working_dict.items():
       if lookup[k].get(v):
           roman_chars.append(lookup[k][v])
       else:
           if v:
               v2 = int(v)//5
               if v2 > 0:
                   roman_chars.append(lookup[k]['5']+lookup[k]['1']*(int(v)%5))
               else:
                   roman_chars.append(lookup[k]['1']*(int(v)%5))
    print(''.join(roman_chars[::-1]))

user_input = input('Enter a number to convert to Roman Numeral or vice versa:\n')

if user_input.isdigit():
    int_to_roman(user_input)
else:
    roman_to_int(user_input)
