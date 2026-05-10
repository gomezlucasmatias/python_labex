# Define an empty list
empty = []

# Define something
something = input("Give your favorite word to see if it hides a small robot in it: ")

# Fill the list with something
for letra in something.lower():
    empty.append(letra)
    print(empty)
    for letra in empty:
        if letra == 'h':
            print('[`w`]')
        elif letra == 's':
            print(']º_º[')
        elif letra == 'a':
            print("{*-*}")
        elif letra == 'e':
            print("('__')")
        elif letra == 'd':
            print("|o.o|")
    
        
