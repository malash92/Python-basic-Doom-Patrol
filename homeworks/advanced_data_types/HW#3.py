#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print (id(int_a)) #id int_a 1508162320
print (id(str_b)) #id str_b 7696704
print (id(set_c)) #id set_c 19980040
print (id(lst_d)) #id lst_d 7251432
print (id(dict_e)) #id dict_e 19810336
#2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print (id(lst_d)) # id lst_d +4,5 '7430984'
#3. Define the type of each object from step 1.
print (type(int_a)) #class 'int'
print (type(str_b)) #class 'str'
print (type(set_c)) #class 'set'
print (type(lst_d)) #class 'list'
print (type(dict_e)) #class 'dict'
#4*. Check the type of the objects by using isinstance.
print (isinstance(int_a, int)) #True
print (isinstance(str_b, str)) #True
print (isinstance(set_c, set)) #True
print (isinstance(lst_d, list)) #True
print (isinstance(dict_e, dict)) #True
#5. String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# With .format and curly braces {}
print ("Anna has {} apples and {} peaches.".format('five','three')) #Anna has five apples and three peaches.
#6. By passing index numbers into the curly braces.
print ("Anna has {0} apples and {1} peaches.".format(5,3)) #Anna has 5 apples and 3 peaches.
#7. By using keyword arguments into the curly braces.
print ("Anna has {first} apples and {second} peaches.".format(first="five",second="three"))#Anna has five apples and three peaches.
#8. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {apple:5d} apples and {peach:3d} peaches.".format(apple=5, peach=3)) #Anna has     5 apples and   3 peaches.
# 9. With f-strings and variables
chsl1 = 5
chsl2 = 3
print (f"Anna has {chsl1} apples and {chsl2} peaches.") #Anna has 5 apples and 3 peaches.
# 10. With % operator
print ("Anna has %s apples and %s peaches." % (chsl1, chsl2)) #Anna has 5 apples and 3 peaches.
# 11. With variable substitutions by name (hint: by using dict)
dct2 = {"apple": chsl1,"pea": chsl2}
print ("Anna has %(apple)d apples and %(pea)d peaches." % dct2) # Anna has 5 apples and 3 peaches.
# 12. Convert (1) to list comprehension
# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
lst = [num ** 2 if num % 2 == 1 else num **4 for num in range(10)]
print(lst) #[0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]
#13. Convert (2) to regular for with if-else
# (2) list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print (list_comprehension) # [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]
#14. Convert (3) to dict comprehension.
# (3)  d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print (d) # {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}
# 15*. Convert (4) to dict comprehension.
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
dict_comrehension1 = {num:(num ** 2 if num % 2 == 1 else num // 0.5) for num in range(1,11)}
print (dict_comrehension1) # {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}
# 16. Convert (5) to regular for with if.
# (5) dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
dict_comrehension = {}
for x in range (0, 10):
    if x**3 % 4 == 0:
       dict_comrehension[x] = x **3
print (dict_comrehension) #{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
# 17. Convert (6) to regular for with if-else.
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
dict_comrehension = {}
for x in range(10):
    if x ** 3 % 4  == 0:
        dict_comrehension[x] = x ** 3
    else:
        dict_comrehension[x] = x
print(dict_comrehension) # {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}
#18.  Convert (7) to lambda function
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
foo = lambda x, y: x if x < y else y
print (foo(5, 8)) # 5
# 19*. Convert (8) to regular function
#(8) foo = lambda x, y, z: z if y < x and x > z else y
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print (foo(1, 4, 9)) #4
# 20. lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]  Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print (sorted(lst_to_sort)) #[1, 5, 13, 15, 18, 24, 33, 55]
# 21. Sort lst_to_sort from max to min
print (sorted(lst_to_sort, reverse=True)) #[55, 33, 24, 18, 15, 13, 5, 1]
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort1 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort1) #[10, 36, 2, 48, 66, 30, 26, 110]
#23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(pow, list_A, list_B))
print (list_C)
#24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce
spsk = reduce(lambda x,y: x * y, lst_to_sort)
print (spsk) #764478000
# 25.  Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort2 = list(filter(lambda elem:elem % 2 == 1, lst_to_sort))
print(lst_to_sort2) #[5, 1, 33, 15, 13, 55]
# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
lst3=list(filter(lambda x: x<0, range(-10, 10)))
print(lst3) #[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3) #[2, 3, 5, 7]