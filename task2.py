year = int(input("Enter year: "))
if year % 4 != 0:
    print("usually year")
elif year % 100 == 0:
    if year % 400 == 0:
        print("intercalary year")
    else:
        print("usual year")
else:
    print("intercalary year")

