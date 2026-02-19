size = int(input("Enter the size: "))
if size==28:
    print("Small size")
elif size == 30:
    print("Medium size")
elif size == 38:
    print("Large size")
elif size == 42:
    print("XL size")
else:
    print("Invalid size")

''' Chatgpt optimal solutions
size = input("Enter the size: ")

sizes = {
    "28": "Small size",
    "30": "Medium size",
    "38": "Large size",
    "42": "XL size"
}

print(sizes.get(size, "Invalid size"))'''

'''size = int(input("Enter size: "))

match size:
    case 29:
        print("Small")
    case 30:
        print("Medium")
    case 38:
        print("Large")
    case 42:
        print("XLarge")
    case _:
        print("Invalid")'''
