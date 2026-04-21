# Prints the multiplication table of a user-selected number up to 10
table = int(input("Whata multiplicatioin table do you want to know?: "))

list = [table*i for i in range(1, 11)]

print(f"""
      ###Table of {table} up to x 10 is:###

      {table} x 1 = {list[0]}
      {table} x 2 = {list[1]}
      {table} x 3 = {list[2]}
      {table} x 4 = {list[3]}
      {table} x 5 = {list[4]}
      {table} x 6 = {list[5]}
      {table} x 7 = {list[6]}
      {table} x 8 = {list[7]}
      {table} x 9 = {list[8]}
      {table} x 10 = {list[9]}
      """)
