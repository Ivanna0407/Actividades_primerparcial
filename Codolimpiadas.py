def area_triangulo(base,altura):
  area=(base*altura)/2
  return area

print("Cual es la base?")
base=int(input())
print("Cual es la altura?")
altura=int(input())

print("El area de tu triangulo es",area_triangulo(base,altura),"cm cuadrados")
