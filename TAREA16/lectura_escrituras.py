archivo = open("my_notes.txt", "r")
notes = archivo.readline()
notes1 = archivo.readline()
notes2 = archivo.readline()

print(notes)
print(notes1)
print(notes2)
archivo.close()
