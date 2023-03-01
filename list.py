lst=[13,23,55.0,"sharma"]
lst2=[24,54,40,50]
print(lst.index(23))
print(lst.insert(2,44))  # None---> permanent changes

print(lst)
lst2.extend([888])
print(lst2)

lst2.extend([777])
print(lst2)

# lst2.pop()
# print(lst2)
print(lst2.pop())    #777
print(lst.remove(13))   # None
print(lst)     #  here remove 13 and return [23, 44, 55.0, 'sharma']


print(lst.reverse())
print(lst)


# Write a to sum of all list elements
list=[10,30,50,60]
# for x in list:
#     # print (sum(list(x)))



print(sum(list)+sum(lst2))