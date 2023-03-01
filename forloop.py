#  for lOop

# a=[11,22,44,33,22]
# # i=0
# while i<len(a):
#     print(a[i])
#     i+=1

    ## Range()function is a python built in function which help us to create a iteration
b=[1,2,4,3,2]
for i in b:
    print(i)

lst=[]
n=int(input("Enter Your range.:"))
for i in range(n):
    v=int(input("enter your value:"))
    lst.append(v)
print(lst)