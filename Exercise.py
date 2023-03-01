#write a program to print a python version you are using

# import sys
# print("python version")
# print(sys.version)
# print("version")
# print(sys.version_info)

# Find Leap year or not
def is_leap(n):
    if n%400==0:
        return True
    if n% 100==0:
        return False       # print("not leap year")#False
    if n%4==0:
        return True 
    return False
year= int(input("Enter Your Year:"))
print(is_leap(year))