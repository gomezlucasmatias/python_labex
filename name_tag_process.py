# Create input for get full name user 
name = input('Put your full name: ')

# Convert full name entrace to Upper case 
name_uppercase = name.upper()

# Reeplace spaces into of full name for underscores 
name_with_underscore = name_uppercase.replace(" ", "_")

# Added prefix to complete tag name process 
name_tag = "ASTRONAUT_" + name_with_underscore

# Generate output with f-string
output = f'''
Original name: {name}
Processed name tag: {name_tag}
'''
# Show result 
print(output)
print('===Tag has been created===')
