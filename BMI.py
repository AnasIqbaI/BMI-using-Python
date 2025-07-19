weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height / 100) ** 2
print("Your BMI is:", BMI)

if BMI <= 18.4:
    print("You are underweight.")

elif BMI <= 24.9:
    print("You have a normal weight.")
    
elif BMI <= 29.9:
    print("You are overweight.")
    
elif BMI <= 34.9:
    print("You are obese (Class 1).")

elif BMI <= 39.9:
    print("You are obese (Class 2).")

else:
    print("You are obese (Class 3).")

