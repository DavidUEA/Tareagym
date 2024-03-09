def convertidor(grados_centigrados):
    faren=(9*(grados_centigrados -32))/5
    kelvin= grados_centigrados+273.15
    return faren, kelvin #->_arreglo

#solicitud de grados centigrados al usuario
grad_cent=float(input("Ingrese valor_grados centigrados="))

#invocar a la función
r_faren, r_kelvin = convertidor(grad_cent)

#imprimimos el resultados
print("Grados Fahrenheit", r_faren, "Grados Kelvin", r_kelvin)