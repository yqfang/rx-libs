from __future__ import print_function


#So there are many types of objects which can be used with a for loop. These are called iterable objects.


# 1. for .. in loop over a list
def loop_over_list(str_list):
    for s in str_list:
        print(s)
loop_over_list(['1', '2'])


# 2. for .. in loop over a string
def loop_over_str(str):
    for c in str:
        print(c)
loop_over_str("hello")

# 3. for ..in loop over a dict

def loop_over_dict(dict):
    for key in dict:
        print("key: {0}, value: {1}".format(key, dict[key]))

loop_over_dict({'Alice': 3, 'Peter': 4})


# 4. for .. in loop over file

def loop_over_file(file_name):
    file = open(file_name)
    for l in file:
        print(l)

loop_over_file("1.1_basic_for_in_iterator.py")


# An iterable is any object, not necessarily a data structure, that can return an iterator (with the purpose of returning all of its elements). That sounds a bit awkward, but there is an important difference between an iterable and an iterator. Take a look at this example:
# >>> x = [1, 2, 3]
# >>> y = iter(x)
# >>> z = iter(x)
# >>> next(y)
# 1
# >>> next(y)
# 2
# >>> next(z)
# 1
# >>> type(x)
# <class 'list'>
# >>> type(y)
# <class 'list_iterator'>