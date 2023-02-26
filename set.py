# set constructor is set()
# Empty set {}






s={}
print(s)
t=set()
print(t,type(t))

# Set does not support nesting 
# print(dir(set()))  # this is For set methods 


u={2,3,4,5,7,8}
v={2,4,5,6}
# u={45,67,10.4,"sharma",(112,22.33,"chanchlesh")}
# v={3,2,4,5,4.3,"Rose"}
# print(u.add(24))
print(u.difference(v))
print(u)
print(u.difference_update(v))
print(u)


