# 1.
# name=input("what is you name ")
# print("MY name is ",name)

# 2.
# num1=int(input("Enter number 1 "))
# num2=int(input("Enter number 2 "))

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)


# 3.
# num1=int(input("Enter number 1 "))
# num2=int(input("Enter number 2 "))
# num3=float(input("Enter number 3 "))
# num1=float(num1)
# num2=float(num2)

# print((num1+num2+num3)/3)


# 4
# num=input("Enter a number")
# print(type(num))
# num=float(num)
# print(type(num))
# num=str(num)
# print(type(num))


# 5.
# print(10+3*2**2)

# 6.
# num1=int(input("Enter number 1 "))
# num2=int(input("Enter number 2 "))
# num1=num2+num1
# num2=num1-num2
# num1=num1-num2
# print(num1)
# print(num2)


# 7.
# temp=int(input("Enter the celsius "))
# temp=float(temp)
# ftemp=(temp*(9/5))+32
# print(ftemp)

# 8
# r=int(input("enter the radius"))
# area=3.14*r**2
# print(area)


# 9
# a=int(input("enter num1 "))
# b=int(input("enter num2 "))
# c=int(input("enter num3 "))
# p=float(a)
# r=float(b)
# t=float(c)
# SI=(p*r*t)/100
# print(SI)


# 10
# num=float(input("Enter the number "))
# a=int(num)
# print(a)
# print(num-a)



import math

num = float(input("Enter the number: "))
integer_part = int(num)                 # truncates toward zero
fractional_part_signed = num - integer_part
fractional_part_magnitude = abs(fractional_part_signed)

print(integer_part)
print(fractional_part_magnitude)        # use this if you want 0.78 for -45.78


