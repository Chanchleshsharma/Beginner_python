# set constructor is set()
# Empty set {}






s={}
print( type(s),s)
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


w={34,45,65,55}
x={34,55,543,34}
# print(w.intersection(x))
# print(w.intersection_update(x))
# print(w)

# print(w+x)   # its a error 


y=list(w)
print(y)


for i in w:
    print(i)

new={45,55,66,92,True,"hello",4.7}

# new .add(20)
new.pop()
new.remove(45)

print(new)

### Note----> Only Immutable Value are allowed in set

s={10,30,50,30}
print(min(s))

print(max(s))
print(sum(s))
print(len(s))

s1={28,95,51,62}
s2={95,98,56,51,55}
s3=s1.union(s2)
print(s3)

s4=set("india")
print(s4)
s5=set(range(1,10))
print(s5)

#__________--------------------------------------------------
# s=set()
# size=int(input("enter Your size of set:"))
# for i in range(size):
#     v=int(input("Enter Your value:"))
#     s.add(v)
# print(s)


#_Without set comprehension_______________________________________________________________
set1={1,2,3,4,5,6,7,8,9,10,11,12,13,14}
# new_set=set()
# for i in set1:
#     new_set.add(i+1)
# print(new_set)
  

# # Set comprehension
set={i*i for i in range(5)}
set2={i+1 for i in range(5)}
print(set) 
print(set2) 
#########


# set1._hash(460)
# print(set1)

  