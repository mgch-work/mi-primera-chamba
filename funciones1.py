#Funciones en python
#Crear una función llamada saludar que reciba el nombre de la persona
def saludar(nombre):
    print("Hola ", nombre)
#Crear una función llamada suma_numeritos que reciba 4 numeros
def suma_numeritos(num1, num2, num3, num4):
    sum=num1+num2+num3 +num4
    return sum
#Crear una función llamada area_triangulo, que reciba la base y altura
def area_triangulo(base, altura):
    area=(base*altura)/2
    return area
#Usar esas funciones
nombrecito=input("Ingresa tu nombre")
saludar(nombrecito)
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
n3=int(input("Ingresa el tercer numero "))
n4=int(input("Ingresa el cuarto numero "))
print(suma_numeritos(n1,n2,n3, n4))




