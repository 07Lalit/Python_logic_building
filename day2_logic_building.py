                         # Question 1
"""
Q1-> Write a program to print pattern like this ?

X           X
  X       X
    X   X
      X
    X   X
  X       X
X           X

#code -:

n = 7
for i in range(0,n):
    for j in range(0,n):
        if(i==j or i+j==n-1):
            print(f"X",end=" ")
        else:
            print(" ",end=" ")
    print()


"""
                        # Question 2
"""
Q2 Write a program to print pattern like this ? 
-> 
W           W  
  E       E    
    L   L      
      C       
    O    O     
  M        M   
E            E 


#code -:


n = 7 
a="WELCOME"
for i in range(0,n):
    for j in range(0,n):
        if(i==j  ):
            print(f"{a[j]}",end=" ")
            
        elif(i+j==n-1):
            print(f"{a[i]} ",end=" ")
            
        else:
            print(" ",end=" ")
    print()
    


"""