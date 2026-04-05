#!/usr/bin/env python3
# Programa para calcular si un estudiante aprueba o no

calificacion = float(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90:
    letra = "A"
    estado = "Excelente ✨"
elif calificacion >= 80:
    letra = "B"
    estado = "Muy bien 👍"
elif calificacion >= 70:
    letra = "C"
    estado = "Bien ✅"
elif calificacion >= 60:
    letra = "D"
    estado = "Suficiente ⚠️"
else:
    letra = "F"
    estado = "Reprobado ❌"

print(f"\n📊 Calificación: {calificacion}")
print(f"📝 Letra: {letra}")
print(f"🎯 Estado: {estado}")

if calificacion >= 70:
    print("🎉 ¡Felicidades, aprobaste!")
else:
    print("😢 Sigue esforzándote, puedes mejorar!")
