1.
# salary=int(input("Enter the salary "))
# tax=0
# if salary<30000:
#     tax=5/100*salary
# if salary>=30000 and salary>70000:
#     tax=15/100*salary
# if salary>70000:
#     tax=25/100*salary
# print(tax)   

# 2.
# def even(a,b):
#     for i in range(a,b):
#         if(i%2==0):
#             print(i)
# a=int(input("Enter the num1 "))
# b=int(input("Enter the num2 "))
# even(a,b)

# other solution ignore it please
# def hello():
#     global x
#     x=89
#     print(x)

# hello()
# print(x*x)


# 3. 
# def sol(num):
#     while num>0:
#         print(num%10)
#         num=num//10

# a=int(input("Enter the number "))

# sol(a)


# 4.
# def countDigit(num):
#     digit=0
#     while num>0:
#         digit+=1
#         num=num//10
#     print(digit)

# a=int(input("Enter the number"))
# countDigit(a)


# 5.
# def sumOfDigit(num):
#     sum=0
#     while num>0:
#         sum+=num%10
#         num//=10
#     return sum
# a=int(input("enter the number "))
# print(sumOfDigit(a))

# 6.
# def divisibleBy3(num):
#     for x in range(num):
#         if x%3==0 and x%5==0:
#             if x>0:
#               print(x)
# a=int(input("enter the number "))
# divisibleBy3(a)

# 7
# def classi():
#     while True:
#         a=input("Enter the number or Quit ")
#         if(a.lower()=="quit"):
#             print("Bye bye ")
#             break
#         else:
#             if int(a)>0:
#                 print("positive")
#             elif int(a)==0:
#                 print("zero")
#             else:
#                 print("negative")

# classi()
    

# 8
# def cal(a,b,o):
#     res=eval(f"a{o}b")

#     print(res)
    
# a=int(input("Enter first number "))
# b=int(input("Enter second number "))
# c=input("enter the operation ")

# cal(a,b,c)

# 9
def is_prime(n):
    if n<=1:
        return False
    for x in range(2,n-1):
        if n%x==0:
            return False
    return True


a=int(input("Enter the number "))
print(is_prime(a))
 

    


# 10.
# ori=int(input("Enter the original number"))
# def game():
#     while True:
#         gu=int(input("Enter the guessed number "))
#         if ori<gu:
#             print("Too High")
#         elif ori==gu:
#             print("correct")
#             break
#         else:
#             print("Too low")
    
# game()




 
  



        



