#abrir el archivo modo lectura
archivo = open("my_notes.txt", "r")
#lectura del archivo por lineas
notes = archivo.readline()
notes1 = archivo.readline()
notes2 = archivo.readline()
#imprimir el archivo por lineas
print(notes)
print(notes1)
print(notes2)
#cerramos el archivo
archivo.close()
#cerramos el archivo modo escritura para
#ingresar un dato
archivo = open("my_notes.txt", "a")
#dato a ingresar
linea = ["EMAIL: DCHANGO90.DC"]
archivo.writelines(linea)
#imprimimos el archivo con el dato ingresado
#sin borrar los archivos que se encontraban
#en el texto
print(archivo)
archivo.close()
#lectura del archivo con el dato agregado
archivo = open("my_notes.txt", "r")
nota4= archivo.read()
print(nota4)
