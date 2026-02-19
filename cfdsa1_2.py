a1= int(input("Enter Angle 1: ")) # For single line input use a1,a2,a3 = map(int,input().split()) - enter input with space between
a2= int(input("Enter Angle 2: "))
a3= int(input("Enter Angle 3: "))

if ((a1+a2+a3)==180):
    print("triangle can be formed")
else:
    print("triangle formation not possible")
    
