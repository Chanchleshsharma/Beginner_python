x=[10,30,40,50]
print(x)

a,b,c,d=x
print(a)
print(b)
print(c)
print(d)

a,b,*c=x
print(c)
*a,b,c=x

print(a)


list=[91,45,77,89,35,86,90,91]
y=sorted(list,reverse=True)
print(y)
*z,u,v=y
print(z)