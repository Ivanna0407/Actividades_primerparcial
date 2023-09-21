def converción (kilometros):
  metros=kilometros*1000
  return metros

print("Cuantos kilometros hay?")
kilometros=int(input())

print("Son",converción(kilometros),"metros")
