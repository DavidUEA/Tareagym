


def calcular_descuento(compra1, descuento):
    suma_com= descuento * compra1/100

    return  suma_com



compra1= float(input("ingrese su valor total de la compra:"))


valor= calcular_descuento(compra1,20)
descuento= 20

valor_final = compra1 - valor
print("GRACIAS POR TU COMPRA")

descuent2=10
descuento2=calcular_descuento(compra1,descuent2)
descuento2= descuent2*compra1/100


print("El descuento normal en nuestro local es de:",descuent2,"%")
print("Tendrias solo un descuento de: $",descuento2)
print("Sin embargo por ser un Cliente Especial te aplicamos un descuento del: ",descuento,"%")
print(" te descontamos el valor de: $", valor,)
print("Su compra de:", compra1, ", con descuento especial del", descuento,"% , "" Su pago total seria de:", valor_final)
print("CONTINUA COMPRANDO EN NUESTRO LOCAL PARA CONTINUAR CON LOS DESCUENTOS ESPECIALES")