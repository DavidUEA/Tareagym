informacion_personal = {"nombre": "David", "edad": 30, "ciudad": "Riobamba", "Profesion": "Ingeniero"}

#Imprimir diccionario Principal
print(f"Diccionario principal: {informacion_personal}")

#accedemos y modificamos el valor ciudad
informacion_personal["ciudad"] = "Quito"
print(f"Diccionario Actualizado: {informacion_personal}")

#Verifica si tiene la clave "telefono" existe en el diccionario
# Si no existe, agrégala con un número
if informacion_personal == "telefono":
    print("Si tiene el telefono")
else:
    print("No tiene el telefono")
    informacion_personal["Telefono"] = input("Ingrese el telefono: ")
print(f"Diccionario Actualizado: {informacion_personal}")

#Eliminamos la clave edad
del informacion_personal["edad"]
print(f"Diccionario Actualizado: {informacion_personal}")