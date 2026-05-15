# Datos del problema
gravedad_tierra = 9.81   # m/s²
gravedad_luna = 1.62     # m/s²

# Entrada del usuario (ejemplo)
peso_tierra = float(input("¿Cuánto pesas en la Tierra (en kg)? "))

# Cálculo usando la fórmula
# Forma 1: Usando la regla de tres exacta
peso_luna_exacto = peso_tierra * (gravedad_luna / gravedad_tierra)

# Forma 2: Usando el atajo de la división entre 6
peso_luna_aproximado = peso_tierra / 6

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Tu peso en la luna es: {peso_luna_exacto:.2f} kg")
