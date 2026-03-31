# Obtein user age 
user_age = input("How old are you? ")

# Convert user date to integer number 
age = int(user_age)

# Compare user's age using if structure 
if age < 13:
    print("You are a kid")
elif age > 13 and age < 18:
    print("You are a teenager")
elif age > 18 and age < 40:
    print("You are an adult")
else:
    print("You are a Senior")
