print("¿Cuál es el precio de tu producto?")
precio=input()
precio=int(precio)
print("¿Cuál es el porcentaje de descuento?")
descuento=input()
descuento_p=int(descuento)
descuento=descuento_p/100
descuento_t=precio*descuento
print("El precio final es de",precio-descuento_t,"Con un",descuento_p,"% de descuento")
print("el descuento fue de",descuento_t,"pesos")
