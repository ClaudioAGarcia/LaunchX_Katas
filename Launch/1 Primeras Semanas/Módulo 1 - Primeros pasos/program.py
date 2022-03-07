#program.py
#Nombre: Claudio Antonio Garibay Garcia


sum = 1 + 2 # 3

product= sum *2

#funcion print() lo que este adentro se imprime en consola
print('suma = ', sum)
print('producto de operacion = ', product)

print('hola consola')

#type() sirve para saber que tipo de dato es

print(type(sum))

#Operades de Asignacion

# a_1 += 2 # x incrementado en 2. Si antes contenía 2, ahora tiene un valor de 4
# a_2 -+ 2 # x decrementado por 2. Si antes contenía 2, ahora tiene un valor de 0.
# a_3 /= 2 # x dividido por 2. Si antes contenía 2, ahora tiene un valor de 1.
# a_4 *= 2 # x multiplicado por 2. Si antes contenía 2, ahora tiene un valor de 4.

#Importar parte de biblioteca de fechas

from datetime import date

#obetner fecha de hoy

date.today()

#Imprimir fecha en terminal/consola
print(date.today())

#combersion str()int()
print('El dia de hoy es : ' + str(date.today()))

#Entrada de datos

print('Hola, bienvenido! cual es tu nombre?')
name = input('Introduce tu nombre ')
print('Un gusto conocerte ' + name)

#Calculadora

print('Calculadora para sumar')
n_1 = input('Introduce el primer numero :')
n_2 = input('Introduce el segudno numero :')
print('resultado : ' + str(int(n_1) + int(n_2)) )