lbs_in_kg = 2.20462262185
in_in_cm = 0.3937007874
error_count = 0

weight = input("How much do you weigh (lbs or kgs)? ").replace(' ', '')

if weight.find("k") > -1:
    weight_unit = "kg"
elif weight.find("l") > -1:
    weight_unit = "lbs"
else:
    weight_unit = input("Is that in pounds (lbs) or kilograms (kgs)? ").lower()

if max(weight.find("k"), weight.find("l")) == -1:
    weight_value = len(weight)
else:
    weight_value = max(weight.find("k"), weight.find("l"))
weight = float(weight[:weight_value])

if weight_unit[0] == "k":
    unit = "kg"
    weight_in_lbs = round(weight * lbs_in_kg, 2)
    weight_in_kgs = round(weight, 2)
    print(f"You weigh {weight} kg, which is {weight_in_lbs} lbs.")
elif weight_unit[0] == "l":
    unit = "lbs"
    weight_in_kgs = round(weight / lbs_in_kg, 2)
    weight_in_lbs = round(weight, 2)
    print(f"You weigh {weight} lbs, which is {weight_in_kgs} kg.")
else:
    print("Please enter either kgs or lbs as the unit for your weight.")
    error_count += 1

height = input("How tall are you (cms or ins)? ").replace(' ', '')
if height.find("c") > -1:
    height_unit = "cm"
elif height.find("i") > -1:
    height_unit = "in"
else:
    height_unit = input("Is that in inches (in) or centimetres (cm)? ").lower()

if max(height.find("c"), height.find("i")) == -1:
    height_value = len(height)
else:
    height_value = max(height.find("c"), height.find("i"))
height = float(height[:height_value])

if height_unit[0] == "c":
    height_unit = "cm"
    height_in_in = round(height * in_in_cm, 2)
    height_in_cm = round(height, 2)
    print(f"You are {height} cm tall, which is {height_in_in} inches.")
elif height_unit[0] == "i":
    height_unit = "in"
    height_in_cm = round(height / in_in_cm, 2)
    print(f"You are {height} inches tall, which is {height_in_cm} cm.")
else:
    print("Please enter either cm or in as the unit for your height.")
    error_count += 1

if error_count == 0:
    BMI = round(weight_in_kgs / ((height_in_cm / 100) ** 2), 2)
    print(f"Your BMI is {BMI}")
    weight_to_healthy_lower_kgs = round((18.6 - BMI) * ((height_in_cm / 100) ** 2), 2)
    weight_to_healthy_upper_kgs = round((BMI - 24.9) * ((height_in_cm / 100) ** 2), 2)
    weight_to_healthy_lower_lbs = round(weight_to_healthy_lower_kgs * lbs_in_kg, 2)
    weight_to_healthy_upper_lbs = round(weight_to_healthy_upper_kgs * lbs_in_kg, 2)
    if BMI < 18.5:
        print("You are underweight (BMI less than 18.5)")
        print(f"To be within the healthy range, you would need gain {weight_to_healthy_lower_kgs} kgs.")
    elif BMI <= 24.9:
        print("You are within the 'healthy range' (BMI between 18.6 and 24.9)")
    elif BMI <= 29.9:
        print("You are overweight (BMI between 25.0 and 29.9)")
        print(f"To be within the healthy range, you would need to lose {weight_to_healthy_upper_kgs} kgs ({weight_to_healthy_upper_lbs} lbs).")
    elif BMI <= 39.9:
        print("You are obese (BMI between 30.0 and 39.9)")
        print(f"To be within the healthy range, you would need to lose {weight_to_healthy_upper_kgs} kgs ({weight_to_healthy_upper_lbs} lbs).")
    else:
        print("You are severely obese (BMI over 39.9)")
        print(f"To be within the healthy range, you would need to lose {weight_to_healthy_upper_kgs} kgs ({weight_to_healthy_upper_lbs} lbs).")
else:
    print("Please input correct details.")