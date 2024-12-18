"""
Q1 WAP to count length of string using loop ?
ex-: a= "Malayalayam"
   o/p -: 11

  1) Ist approch using len() function
   print(len(a)) # 11

  2)IInd approch using for loop :

  a = str(input("Enter a string : " ))
  cnt=0
  for i in a:
    cnt=cnt+1
  print(cnt)


"""

"""
Q2-> Write a program to convet uppercase character to 
    lowercase and lowercase character to uppercase in the 
    given string ? 
    
1) Ist approch is using methods 
   i) upper()   ex-: a = "lalit"  a.upper()   # LALIT
   ii) lower()  ex-: a = "LALIT"  a.upper()   # lalit
   iii) swapcase ex-: a= "laLiT" a.swapcase()  # LAlIt
   
2) 
"""
a="lalit"
print(a.upper())
print(a.lower())