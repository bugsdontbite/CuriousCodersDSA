n = int (input())
for i in range(1 , n+1):
    for j in range (1 , i+1):
        print("*",end="")
    print()
for a in range (n+1,n+n):
    for b in range (-a+n+4,0,-1):
        print("*",end="")
    print()
