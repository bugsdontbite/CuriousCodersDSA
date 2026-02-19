mark = int(input("enter your mark: "))
if mark>=90and mark<=100:
    print("You Secured A grade")
elif((mark>=80 and mark<90)):
    print("you secured B grade")
elif((mark>=60 and mark<80)):
    print("you secured C grade")
elif((mark>=35 and mark<60)):
    print("you secured D grade")
elif(mark<35 and mark>=0):
    print("You have failed")
else:
    print("please enter a valid mark")

    """ optimal code by chatgpt
mark = int(input("Enter your mark: "))

if mark < 0 or mark > 100:
    print("Please enter a valid mark")
elif mark >= 90:
    print("You secured A grade")
elif mark >= 80:
    print("You secured B grade")
elif mark >= 60:
    print("You secured C grade")
elif mark >= 35:
    print("You secured D grade")
else:
    print("You have failed")"""
    
        
            
