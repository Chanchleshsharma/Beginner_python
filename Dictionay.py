#dictionary constructor is dict()
#dictionary literal is {}
#dictionary is a combination of  key value









a=dict()   # constructor used to create  a empty dictionary
print(a,type(a))


b={}
print(b)


c={1:"krishna",2:"Rahul",3:"chanchlesh",4:"Kunal"}
print(c)
print(c[1])
c[2]="neha"
print(c)

# d={(29,39,49,"Seeta",2+3J),{"son: Sagar","father:Mr.sharma","mother:Mrs.sharma"}}
# print(d)



h =dict()
print(h)
h.update ({1:"sharma",2:"neha" ,3:"Raj"})     # update-----> only
print(h)


print(h.keys())

print(h.values())
print(h.pop(2))      ###neha
print(h)
print(h.popitem())    ##(3, 'Raj')
print(h)
print(h.update({4:"raam",5:"Lakhan",6:"Sanjana"}))
print(h)
print(h.values())    ###dict_values(['sharma', 'raam', 'Lakhan', 'Sanjana'])
print(h.keys())       #### dict_keys([1, 4, 5, 6]) its return keys of dictionary
print(h.setdefault(1,None))
g={}
print(g)
g.update({28,39,49})