set =frozenset()
print(set,type(set))

set2=frozenset([12,22,33,44,55,66,77,88])

print(set2)

set3=frozenset((12,22,33,44,55,66,77,88))

print(set3)

fs=frozenset(range (8))
for i in fs:
    print(i)
    print(type(fs))