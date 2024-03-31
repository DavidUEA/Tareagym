archivo = open("my_notes.txt", "r")
notes = archivo.readline()
notes1 = archivo.readline()
notes2 = archivo.readline()

print(notes)
print(notes1)
print(notes2)
archivo.close()

archivo = open("my_notes.txt", "a")
linea = ["EMAIL: DCHANGO90.DC"]
archivo.writelines(linea)
print(archivo)
archivo.close()
archivo = open("my_notes.txt", "r")
nota4= archivo.read()
print(nota4)
