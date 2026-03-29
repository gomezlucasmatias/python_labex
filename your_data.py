# Get user input
user_name = input('What is your name?: ')
user_age = input('How old are you: ')

# Transform user_age to int 
age = int(user_age)

# Performance with inputs 
years_to_100 = 100 - age
is_an_adult = age >= 18

# Making output with f-string
output = f"""
--- User Information: ---
Hello {user_name}!
You are {user_age} years old.
You will be 100 years old in {years_to_100} years.
Are you an adult?: {is_an_adult}.
--- End Of Information --- 
"""

# Print informations 
print(output)


