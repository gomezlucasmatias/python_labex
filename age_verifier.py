ask_for_age = input('How old are you? ')

# Convert data input user
age = int(ask_for_age)


# Compare input age to adult aren
if age >= 18:
    print(f"You are {age} years old, You're an adult")
else:
    print("You aren't an adult yet")
