# Stage of life 
age_user = input("Tell me how old you are?: ")

# Transform input's user to a intiger 
age = int(age_user)

if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
else:
    print("You are an elder")
