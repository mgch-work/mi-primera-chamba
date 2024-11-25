print("holiii")

deportes=["Fútbol","Voleibol","Natación","Basquetbol"]
print(deportes)
print(deportes[2])
#posición de Natacion
#posición de Natacion
pos=deportes.index("Natación")
print("La posición de natación es:",pos)
print(deportes.index("Natación"))


#Agregar otro deporte al final
deportes.append("Hanball")
deportes.insert(2,"box")
print(deportes)

cantidad_saludos=int(input("cuantos saludos quieres?"))

for i in range(cantidad_saludos):
   print("hola")

num_deportes=int(input("cuantos deportes agregaras"))
for i in (range(num_deportes)):
    dep=input("ingresa deporte ")
    deportes.append(dep)

print(deportes)