# 1. Crear un Diccionario con información ficticia
informacion_personal = {
    "nombre": "Jordan Arriaga",
    "edad": 24,
    "ciudad": "Quito"
}

# 2. Acceder y Modificar Valores
# Modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"

# Agregar la clave "profesion"
informacion_personal["profesion"] = "Ingeniero"

# 3. Verificar Existencia de Claves
# Verificar si "telefono" existe y agregarlo si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# 4. Eliminar una Clave
# Eliminar la clave "edad"
del informacion_personal["edad"]

# 5. Imprimir el Diccionario Final
print(informacion_personal)
