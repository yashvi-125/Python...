from ast import Dict
from asyncio import QueueEmpty
from multiprocessing.sharedctypes import Value


# fname = 'yashvi'
# lname = 'nama'
# if fname == 'yashvi' and lname == 'asd':
#     print('yes firstname is yashvi')
# else:
#      print('no firstname is not yashvi')

# if 'yashvi' in [a,b,c]:
#     print('yashvi is in list')
# elif 'p' in 'yashvi':
#     print('yashvi has p in spelling')
# elif 'a' in 'yashvi':
#     print('yashvi has a in spelling')
# else:
#     print('conditions not true')
 
# some_string = input() # from this line, user ll have to give some input.

# for i in some_string: # this perticuler ll be resonsible for iterating over an individual char of string
#     # print(i, ord(i))
#     if ord(i) % 2 == 0:
#         print(f'{i} is at even position at {ord(i)}')

# n = input()
# n = int(n)
# lst = []
# for i in range(0,n):

#     print(lst)

# take n*2 input form the user in which first set will define the data type and secon set shows the data in the dictionary:

n = int( input('enter the number of inputs'))
a = n*2
dict={
    'str' : [],
    'num' : [],
    'float' : []
}
lst=[]
for i in range(0,a):
    set1 = input('enter the data type {n}')
    set2 = input('enter the data{n}')
    if n == 'str':
        dict['str'].append(Value)
    elif n == 'int':
        dict['int'].append(Value)
    elif n == 'float':
        dict['float'].append(Value)
    else:
        print('qiscwoidnoci')
print (dict)

