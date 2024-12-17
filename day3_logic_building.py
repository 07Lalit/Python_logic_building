"""
Q1 Write a program in python to reverse a 
   string 
#1) using slicing operator
   s= str(input("Enter a string  : "))
   print(s)
   print(s[ : :-1])

#2) using for loop

  var= str(input("Enter a string  : "))
  rev = str()
  for i in range(len(var)-1,-1,-1):
      rev = rev+var[i]
      print(rev)
  print(rev)

"""

"""
Q2- WAP in python to print how many vowels and consonants 
  in the given string?
  
var = str(input("Enter a string : "))
consonent = 0
vowel = 0
for i in range(0,len(var),1):
    if(var[i]=="a" or var[i]== "e" or var[i]=="i" or var[i]== "o" or var[i]== "u"):
        vowel = vowel+1
    else:
        consonent = consonent+1
    
print(f"length of {var} is {len(var)}  ")
print(f" count of vowel : {vowel}")
print(f" count of onsonent : {consonent}")



"""
