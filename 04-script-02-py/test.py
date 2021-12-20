#!/usr/bin/env python3
import os
import sys

hello_string = 'Hello'
print(hello_string)
print(type(hello_string))

my_list = ['a', 23, 'hello', 'a', 'a']
my_tuple = (13, 'yes', 'no', 'no', 'no')
my_set = {'H', 'e', 'l', 'o', 'H', 'e'}
my_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 2: 'Apr', 2: 'Mar'}

print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)

# print (my_list[1])
# print (my_tuple[1])
# print (list(my_set))
# print (my_dict[ 1])

my_list.append('world')
# my_tuple.
my_set.add('w')
my_dict[5] = "May"
my_dict[2] = "Feb"

print(my_list)
# print (my_tuple)
print(my_set)
print(my_dict)

print(sys.platform)

my_string = ""
my_list2 = list()
my_tuple2 = tuple()
my_set2 = set()
my_frozen_set = frozenset()
my_dict2 = dict()

print(sys.getsizeof(my_string))
print(sys.getsizeof(my_list2))
print(sys.getsizeof(my_tuple2))
print(sys.getsizeof(my_set2))
print(sys.getsizeof(my_frozen_set))
print(sys.getsizeof(my_dict2))

print(sys.argv[0])
# print(sys.argv[1])

print(os.getlogin())
