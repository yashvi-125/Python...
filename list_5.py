from curses import keyname
from multiprocessing.sharedctypes import Value


# # st = input('enter your string:')
# # dict = {}
# # for i in (st):
# #  if i in dict:
# #      dict[i] += 1
# #  else:
# #      dict[i] = 1
# # print (dict )

#_____________________________________

# st = input('enter your string:')
# st.lower = st.upper
# dict = {}
# for i in ():
#  if i in dict:
#      dict[i] += 1
#      st.lower = st
#  else:
#      dict[i] = 1
# print (dict ) 

#________________________

# for i in range(4):
#     if i == 4:
#         break
#     else:
#         print(i)
 
# n = input('enter your string:')
# o,v = n.split()
# lst = []
# for i in n:
#     if o[] == 'push':
#         lst.append (Value)
#     # elif o == 'pop':
#     #     lst('pop').remove (Value)
#     elif o[] == 'stop':
#         break
#     else:
#         print('invalid')
# print(lst)

# ______________________________________________________

# n = input('enter string:')
# n = n.split()
# map = {
#     'maths' : {},
#     'eng': {},
#     'it' : {}
# } 
# i = 0
# while True:
#     if n[0] == 'stop':
#         break
#     else:
#         if n[0] in map:
#             map{n[0].append(n[1])}
#         else :
#             print('invalid')      
# print (map)

map_ = {}
while True:
    stud_info = input()
    # """
    # stop
    # maths shivank
    # maths aman
    # english aman
    # """
    stud_info = stud_info.split()
    # """
    # ["stop"]
    # ["maths", "shivank"]
    # ["maths", "aman"]
    # """
    if stud_info[0] == 'stop':
        break
    else:
        if stud_info[0] in map_:
            map_[stud_info[0]].add(stud_info[1])
        else:
            map_[stud_info[0]] = {stud_info[1]}
            # map_[stud_info[0]].add(stud_info[1])

print(map_)