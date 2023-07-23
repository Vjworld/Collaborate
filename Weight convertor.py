#User enters their weight in either Lb (pound) or Kg (kilograms)
#program shall return converted weight in Lb when user enters in Kg and vice versa

user_weight = float(input("Hi, Please enter your weight in Lb or Kg -> "))
unit = input("Enter weight in Lbs or Kgs -> Type L for Pound and K for Kilograms -> ")

if unit.upper() == "L":
    print("You entered weight in pound as ->" + str(user_weight) + "Lb")
    converted = user_weight * 0.45
    print(f"Your weight in kilograms is -> {converted} Kgs")
else:
    print("You entered weight in kilograms as ->" + str(user_weight) + "Kg")
    converted = user_weight // 0.45
    print(f"Your weight in pounds is {converted} Lbs")
