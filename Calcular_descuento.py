


def calcular_descuento(descuento,compra1):
    suma_com= descuento * compra1/100

    return  suma_com



compra1= float(input("ingrese su valor total de la compra:"))
descuento= float(input("ingrese su valor del descuento:"))

valor= calcular_descuento(compra1,descuento)

valor_final = compra1 - valor


print("El valor de su descuento es:", valor,)
print("Su compra de:", compra1, "con descuento del", descuento,"%" " tiene el descuento de:", valor_final)