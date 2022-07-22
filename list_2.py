#sets
import numbers
from os import lstat
from sre_constants import RANGE
from stringprep import map_table_b2


st = {1,4,3,5,6,2,7,4,7,4,3,7,32,65,2}
print (st)
bt = {3,1,4,2,5,6,3,7,9}
n = st.union(bt)
print(n)

#dictionaries
map_={
    'firstname':'yashvi',
    'lastname':'nama',
    'course':'IT'
}
print(map_['firstname'])
#.get is used to avoid the errors while trying to found the element which is not present in the directory

print(map_.get('company'))
print(map_.items())
# print(map_.popitem('nama'))
# print(map_.update('IT'))
print(map_.items())
course = map_.pop('course')
print(map_.items())

#looping
lst = [1,2,3,4,5,6,4,3,4,2]
for i in lst[2:]:
    print(i)
#range
    table  = range (2,7,4)
    print(list(table))
#for i in 'yashvi':
    print(i)
    for i in range(len(lst)):
        print(lst[i])

#nested looping
for i in [1,2,3]:
    for j in ['a','b','c']:
        print (i,j)

#prime number
# n = input()
# print ('enter the number',n)
# for i in [n]:        
#     if(range[2,-1]):
#     {
# print('prime number',n)
#     }
#     else:
#         {
#     print('not a prime number',n)
#         }

i=0
while i<5:
    print(i)
    i += 1 #i=i+1
    