# guess_number.py
import random

print("🎮 JUEGO: ADIVINA EL NÚMERO")
print("Piensa en un número del 1 al 100")
input("Presiona Enter cuando estés listo...")

secreto = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
    try:
        guess = int(input("Adivina el número: "))
        intentos += 1
        
        if guess < 1 or guess > 100:
            print("⚠️ El número debe estar entre 1 y 100")
        elif guess < secreto:
            print("📈 Más alto...")
        elif guess > secreto:
            print("📉 Más bajo...")
        else:
            adivinado = True
            print(f"🎉 ¡Correcto! Lo lograste en {intentos} intentos")
            
            # Bonus: mostrar estadísticas
            if intentos <= 5:
                print("🏆 ¡Impresionante!")
            elif intentos <= 10:
                print("👍 Bien hecho")
            else:
                print("💪 La práctica hace al maestro")
                
    except ValueError:
        print("❌ Por favor ingresa un número válido")
