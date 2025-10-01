weight = float(input("Enter your weight: "))
unit = input("Enter weight unit (K or L): ")

if(unit == "K"):
    result = weight*2.20462
    unit = "Lbs."
    print(f"Your weight is {round(result, 4)} {unit} ")
elif(unit == "L"):
    result = weight*0.453592
    print(f"Your weight is {round(result, 4)} {unit} ")
    unit = "KGs."
else:
    print(f"{unit} is not valid ")
