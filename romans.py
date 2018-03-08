import re
import itertools

def roman_to_int(my_roman):
    lookup = {'I':(1,3,1), 'IV':(4,1,1), 'V':(5,1,1), 'IX':(9,1,1), 'X':(10,3,10), 'XL':(40,1,10), 'L':(50,1,10),
              'XC':(90,1,10), 'C':(100,3,100), 'CD':(400,1,100), 'D':(500,1,100), 'CM':(900,1,100), 'M':(1000,3,1000)}
    rom1 = my_roman.upper()
    v1, v2, v3, list1, list2, match2c, bad_char = [], [], [], [], [], [], []
    total = 0
    stop = None
    for i1 in range(len(rom1)):
        if not lookup.get(rom1[i1]):
            # print('Invalid character(s): [{}]'.format('whitespace' if rom1[i1] == ' ' else rom1[i1]))
            bad_char += rom1[i1]
            stop = 'now'
        else:
            list1.append((rom1[i1], i1))
    if stop:
      print('Invalid character(s): {}'.format(bad_char))
      return
    # print('list1: {}'.format(list1)) #ok
    rex1 = re.compile(r'IV|IX|XL|XC|CD|CM')
    match1 = re.findall(rex1, rom1)
    match2 = [i2.span() for i2 in re.finditer(rex1, rom1)]
    # print('match2: {}'.format(match2))
    for i2b in match2:
        match2c += [i2b[0], i2b[1]-1]
    # print('match2c: {}'.format(match2c))
    list2 = [i3 for j3, i3 in enumerate(list1) if j3 not in match2c]
    # print('list2: {}'.format(list2)) #ok
    for m1 in range(len(match1)):
      if match1.count(match1[m1]) > 1:
        print('Only 1 of {} allowed, not {}'.format(match1[m1], match1.count(match1[m1])))
        return
      else:
        v1.append([lookup[match1[m1]], match2[m1][0]])
    # print('v1: {}'.format(v1))
    for m2 in range(len(list2)):
      if list2.count(list2[m2]) > 3:
        print('Only 3 of {} allowed, not {}'.format(list2[m2], list2.count(list2[m2])))
        return
      else:
        v2.append([lookup[list2[m2][0]], list2[m2][1]])
    # print('v2: {}'.format(v2))
    v3 = sorted(v1+v2, key=lambda x:x[1])
    # print('v3: {}'.format(v3)) # ok
    for m3 in range(len(v3)):
      if m3+1 < len(v3):
        if v3[m3][0][0] < v3[m3+1][0][0]:
          print('Wrong order: larger value at the end.')
          return
        else:
          total += v3[m3][0][0]
          if v3[m3][0][2] == v3[m3+1][0][2]:
            if v3[m3][0][0] == 5*v3[m3+1][0][0]:
              pass
            elif v3[m3][0][1] == 3 and v3[m3+1][0][1] == 3:
              pass
            else:
              print("Invalid input: Same {}'s digit".format(v3[m3][0][1]))
      else:
        total += v3[m3][0][0]
    assert int_to_roman(str(total)) == rom1
    return total
    # print('total: {}'.format(total))
def int_to_roman(my_int):
    lookup = {'one': {'1':'I', '4':'IV', '5':'V', '9':'IX'}, 'ten': {'1':'X', '4':'XL', '5':'L', '9':'XC'},
              'hundred': {'1':'C', '4':'CD', '5':'D', '9':'CM'}, 'thousand': {'1':'M'}}
    int_list = list(my_int)[::-1]
    digit_list = ['one', 'ten', 'hundred', 'thousand']
    working_dict = dict(itertools.zip_longest(digit_list, int_list))
    if int(working_dict['thousand']) > 3:
      print('Number cannot be greater than 3999')
      return
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
    result_roman = ''.join(roman_chars[::-1])
    return result_roman

user_input = input('Enter a number to convert to Roman Numeral or vice versa:\n')

if user_input.isdigit():
    result1 = int_to_roman(user_input)
    if result1: print(result1)
else:
    result2 = roman_to_int(user_input)
    if result2: print(result2)
