
#Matias Lopez NC 0117

# ==============================================================================
# 1. PYTHON CONDITIONS (CONDICIONALES SIMPLES)
# ==============================================================================

print("--- 1. PYTHON CONDITIONS ---")

# Ejemplo 1: Validación de salario
salario_1 = 3500
if salario_1 > 3000:
    print("Ejemplo 1: Aplica para crédito bancario.")

# Ejemplo 2: Comprobación de nivel de batería
bateria_2 = 15
if bateria_2 < 20:
    print("Ejemplo 2: Advertencia: Batería baja.")


# ==============================================================================
# 2. PYTHON IF...ELIF (CONDICIONALES MÚLTIPLES)
# ==============================================================================

print("\n--- 2. PYTHON IF...ELIF ---")

# Ejemplo 1: Clasificación de temperatura corporal
temp_1 = 38.5
if temp_1 < 36.0:
    print("Ejemplo 1: Hipotermia.")
elif temp_1 <= 37.5:
    print("Ejemplo 1: Temperatura normal.")
elif temp_1 > 37.5:
    print("Ejemplo 1: Fiebre detectada.")

# Ejemplo 2: Categorización por experiencia laboral (en años)
exp_2 = 4
if exp_2 < 2:
    print("Ejemplo 2: Nivel Junior.")
elif exp_2 <= 5:
    print("Ejemplo 2: Nivel Semi-Senior.")


# ==============================================================================
# 3. PYTHON IF...ELSE (CONDICIONALES CON ALTERNATIVA)
# ==============================================================================

print("\n--- 3. PYTHON IF...ELSE ---")

# Ejemplo 1: Verificación de mayoría de edad
edad_1 = 20
if edad_1 >= 18:
    print("Ejemplo 1: Es mayor de edad.")
else:
    print("Ejemplo 1: Es menor de edad.")

# Ejemplo 2: Control de acceso con estado de membresía
membresia_activa_2 = False
if membresia_activa_2:
    print("Ejemplo 2: Acceso concedido al gimnasio.")
else:
    print("Ejemplo 2: Acceso denegado. Renueve su membresía.")


# ==============================================================================
# 4. PYTHON FOR LOOPS (BUCLES DETERMINADOS)
# ==============================================================================

print("\n--- 4. PYTHON FOR LOOPS ---")

# Ejemplo 1: Recorrer una lista de herramientas
herramientas_1 = ["Martillo", "Destornillador", "Llave inglesa"]
print("Ejemplo 1 - Inventario:")
for herramienta in herramientas_1:
    print(f"  - Herramienta: {herramienta}")

# Ejemplo 2: Iterar sobre una tabla de multiplicar
print("Ejemplo 2 - Tabla del 5:")
for i in range(1, 4):
    print(f"  5 x {i} = {5 * i}")


# ==============================================================================
# 5. PYTHON WHILE LOOPS (BUCLES INDETERMINADOS)
# ==============================================================================

print("\n--- 5. PYTHON WHILE LOOPS ---")

# Ejemplo 1: Contador descendente de lanzamiento
cuenta_1 = 3
print("Ejemplo 1 - Conteo regresivo:")
while cuenta_1 > 0:
    print(f"  Despegue en {cuenta_1}...")
    cuenta_1 -= 1

# Ejemplo 2: Simulación de acumulación de ahorro
ahorro_2 = 0
meta_2 = 150
print("Ejemplo 2 - Acumulación de ahorro:")
while ahorro_2 < meta_2:
    ahorro_2 += 50
    print(f"  Ahorro actual: ${ahorro_2}")# ==============================================================================
# EJERCICIOS DE PYTHON: ESTRUCTURAS DE CONTROL DE FLUJO
# Caso: Hombres (2 ejemplos por cada estructura de control)
# ==============================================================================
print("Matias Lopez NC 0117")
