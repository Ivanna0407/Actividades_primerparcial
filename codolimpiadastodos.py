def multipicacion (a,b):
  x=a*b
  return x
def división (a,b):
  x=a//b
  return x

print("Dame el primer número:")
a=int(input())
print("Dame el segundo número;")
b=int(input())
print("la multiplicación es:",multipicacion(a,b),"La división es ",división(a,b))

#ejercicio 2
def converción (kilometros):
  metros=kilometros*1000
  return metros

print("Cuantos kilometros hay?")
kilometros=int(input())

print("Son",converción(kilometros),"metros")
#ejercicio 3
def area_triangulo(base,altura):
  area=(base*altura)/2
  return area

print("Cual es la base?")
base=int(input())
print("Cual es la altura?")
altura=int(input())

print("El area de tu triangulo es",area_triangulo(base,altura),"cm cuadrados")
