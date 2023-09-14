#Ivanna Martínez de Alba A00573772
print("¿Cuantos adultos van a la fiesta?")
adultos=int(input())
print("¿Cuantos niños van a la fiesta?")
niños=int(input())
print("¿Cual es el porcentaje de descuento?")
descuento=int(input())
presiosillasadultos=adultos*25
presiosillasniños=niños*20
sillastotal=presiosillasadultos+presiosillasniños
mesasadultos=adultos/10
mesasniños=niños/10
mesas=mesasadultos+mesasadultos
carpas=mesas/6
costocarpas=carpas*630
costomesasadulto=mesasadultos*170
costomesasniños=mesasniños*170
costomesas=costomesasadulto+costomesasniños
costototal=presiosillasadultos+presiosillasniños+costocarpas+costomesas
impuesto=costototal*(16/100)
costofinal=costototal+impuesto
descuentototal=(costofinal*(descuento/100))
costodesceunto=costofinal-descuentototal
print("Total de sillas",sillastotal)
print("Mesas de adulto",costomesasadulto)
print("Mesas de niño",costomesasniños)
print("Carpas",costocarpas)
print("Costo sin impuesto",costototal)
print("Impuesto",impuesto)
print("Costo final con impuesto pero sin desceunto",costofinal)
print("Desceunto",descuentototal)
print("Costo final con descuento",costodesceunto)
