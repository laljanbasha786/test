# #1 ans

# units=int(input("enter the units"))
# if units<=100:
#     print(units*5+50)

# elif units>101 and units<=200:
#     print(units*7+50)

# else:
#     print(units*10+50)


# 2 Ans    


# firstnumber=int(input("enter a value"))
# secondnumber=int(input("enter a value"))
# thirdnumber=int(input("enter a value"))

# if firstnumber>secondnumber and firstnumber>thirdnumber:
#     print(f"1 number is largest",{firstnumber})
# elif secondnumber>firstnumber and secondnumber>thirdnumber:
#     print(f"2 number is largest",{secondnumber})
# else:
#     print(f"3 number is largest",{thirdnumber})


# 6 Ans

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz",i)
#     elif i%3==0:
#         print("Fizz",i)
#     elif i%5==0:
#         print("Buzz",i)
#     else:
#         print(i)


# # 4 Ans

# n=int(input("enter the number"))

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(n))


# #  5 Ans

n=int(input("enter the value"))

a=0
b=1
for i in range(1,n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c






