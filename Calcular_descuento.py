


def calcular_descuento(compra1, descuento=10):
    suma_com= descuento * compra1/100
    return  suma_com



compra1= float(input("ingrese su valor total de la compra:"))


valor= calcular_descuento(compra1,20)
descuento= 20
valor_final = compra1 - valor


print("El valor de su descuento es:", valor,)
print("Su compra de:", compra1, "con descuento del", descuento,"% , "" Su pago total es de:", valor_final)