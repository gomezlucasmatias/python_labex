ask_for_age = input('How old are you? ')

# Convert data input user
age = int(ask_for_age)

if age >= 18:
    print(f"You are {age} old, You ara an adult")
else:
    print("You aren't an adult yet")
