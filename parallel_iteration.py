####Parallel Iteration


roll=[101,102,103,104]
name=["sonu","monu","chintu"]

# for i in zip(roll,name):      # zip function return value as tuple
#     print(i)

for r,n in zip (roll,name):
    print(r,n)


rl=[10,11,12,13,14]
nm=["ram","shyam","raju"]   ## MInimum lenght of both list to see and then dressing in for loop

for i in zip(rl,nm):
    print(i)