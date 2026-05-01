# Get user data 
peso = float(input("Escribe tu peso en kg: "))
altura = float(input("Escribe tu altura en metros: "))

if peso > 0 and altura > 0:
    imc = round(peso / (altura * altura), 2)
    print(f"tu imc es {imc}")

    if imc < 18.5:
        print(f"Tienes un imc de {imc}, es bajo")
    elif imc < 25:
        print(f"Tienes un imc de {imc}, es normal")
    elif imc < 30:
        print(f"Tienes un imc de {imc}, tienes sobrepeso")
    else:
        print(f"Tienes un imc de {imc}, eres obeso")
else:
    print("Debes ingresar Peso y Altura mayores a 0")
