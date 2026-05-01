# Get user data 
peso = float(input("Escribe tu peso en kg: "))
altura = float(input("Escribe tu altura en metros: "))

if peso > 0 and altura > 0 :
    imc = peso / (altura * altura)

print(imc)

if imc < 18.5 :
    print(f"Tienes un imc de {imc}, es bajo")
elif imc > 18.5 and imc < 25 :
    print(f"Tienes un imc de {imc}, es normal")
elif imc > 25 and imc < 30 :
    print(f"Tienes un imc de {imc}, tienes sobrepeso")
else:
    print(f"Tienes un imc de {imc}, eres obeso")
