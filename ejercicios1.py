#EJERCICIO 1
"""
numero = int(input("Introduce un numero"))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

"""
#print("Es par") if numero % 2 == 0 else print("Es impar")


#EJERCICIO 2
"""
numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce otro numero: "))
numero3 = int(input("Introduce el tercer numero: "))

if numero1 >= numero2 and numero1 >= numero3:
    print(numero1 ," es el mayor")
elif numero2 >= numero1 and numero2 >= numero3:
    print(numero2, " es el mayor")
else:
    print(numero3, " es el mayor")

"""

#EJERCICIO 3
"""
numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce otro numero: "))

if numero1 % numero2 == 0:
    print(numero1, " es multiplo de ", numero2)
elif numero2 % numero1 == 0:
    print(numero2, " es multiplo de ", numero1)
else:
    print("No son multiplos")
"""

#EJERCICIO 4

numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce el segundo numero: "))

#numero1 = 3
#numero2 = 8
#aux = 8
print("numero 1 es ", numero1, " y numero 2 es: ", numero2)
if numero1 > numero2:
    aux = numero1
    numero1 = numero2
    numero2 = aux

print("numero 1 es ", numero1, " y numero 2 es: ", numero2)









































