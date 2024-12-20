"""
Q1  WAP to find the GCD of a given number ? (means HCF)
-> GCD stands for greatest common divisor it is also called as HCF (highest common factor) .
   GCD of two positive number is nothing but it is the greatest number which will divide both the number completely

   There are two ways to do it -:

1) using gcd() function which is inside math module in python .

# first you need to import math module

import math

num1= int(input("Enter a number1 : "))  #64
num2= int(input("Enter a number2 : "))  #48
ans = math.gcd(num1,num2)
print(f"GCD of {num1} and {num2} is : {ans }")

# using ecluid's algorithm
1) Initlization : start with two number a & b
2) loop until remainder is zero : continue the process until b becomes zero .
3) calculate remainder : In each Iteration find the remainder of a divided by b .
4) update values :
      i) Assign the value of  b to a temporary variable temp.
      ii) Update b to the remainder . calculated in the previous step.
      iii) update a to be the value stored in the temp .
5) result: When b become zero , a will contains the GCD of the two original numbers .


# taking input form user
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

# Initialize variables a & b with the input values a & b
a= num1
b= num2

# use the Euclidean algorithm to find the GCD
while(b!=0):
    temp = b
    b = a%b
    a = temp
    print(f"temp (means b value is ) : {temp}, b (a%b) ={b}, a (temp)= {a}")

# the variable 'a' now contains the GCD
print(f"The GCD of {num1} and {num2} = {a}")


"""

                      # 2 question

"""
Q2 WAP to find LCM of two numbers ? 
-> LCM -: lcm is a smallest non zero common number, which is the multiple of both the number .
          or 
          It is the smallest positive integer that is divisible by both a & b .
          
# taking input form user
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

# Initialize variables a & b with the input values a & b
a= num1
b= num2

# use the Euclidean algorithm to find the GCD
while(b!=0):
    temp = b
    b = a%b
    a = temp
    print(f"temp (means b value is ) : {temp}, b (a%b) ={b}, a (temp)= {a}")

# the variable 'a' now contains the GCD & also make a variable lcm and write it's forumla 

lcm = abs(num1*num2)/(a)
print(f"The LCM of {num1} and {num2} = {lcm}")


"""

# num1 = 64
# for i in range(2,101):
#     if(num1%i == 0):
#         print(i,end=" ")
# print()
#
# num2= 48
# for i in range(2,101):
#     if (num2%i==0):
#         print(i,end=" ")
# print()