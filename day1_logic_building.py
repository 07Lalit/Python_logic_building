"""
                            Day1 of logic building
                            ----------------------

Q-> Write a program using nested loop to print
   pattern like this ?
=>

0 0 0 0 0 0 0 0 0 10
0 0 0 0 0 0 0 0 9
0 0 0 0 0 0 0 8
0 0 0 0 0 0 7
0 0 0 0 0 6
0 0 0 0 5
0 0 0 4
0 0 3
0 2
1

n=10
for i in range(0,n):
    for j in range(n-i-1):
        print("0",end=" ")
    for k in range(1):
        print(f"{n-i}",end=" ")
    print()


"""