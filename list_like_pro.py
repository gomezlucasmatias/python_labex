# Create t# Prints the multiplication table of a user-selected number up to 10
table = int(input("Whata multiplicatioin table do you want to know?: "))

list = [table*i for i in range(1, 11)]

print(list)
