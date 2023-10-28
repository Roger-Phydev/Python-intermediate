### Tipos de errores ###
#aquí veremos todos los tipos de errores en Phyton, como es probocado y como lo señala Python
#Para apreciar cada tipo de error, se debe borrar el símbolo # de la 2da línea en adelante de cada caso

# Syntax Error #
# print "hola mundo"       #aquí hay un error por falta de paréntesis
print("Hola mundo") #esta es la solución

# Name Error #
#print(variable)           #este error es debido a que no existe la variable, no está definida
variable = 0
print(variable)

# Index Error #
my_list = ["Python","swift","Kotlin","Dart","Javascript"]
# print(my_list[10])       #aquí el error es debido a que el indice es mayor del valor len(my_list) -1, el máximo accesible

# Modulenotfound Error #
# import maths        #en este caso se debe a que el módulo no existe
import math #esta es la solución

# Attribute Error #
import math
# print(math.PI)        #el error se debe a que se usa el nombre equivocado (debería ser pi y no PI)
print(math.pi) #así se debe hacer

# Key Error #
my_dict = {"Nombre":"Brian","Apellidos":"Parra Hernández","Edad":"27"}
#print(my_dict["Apelidos"])     #el error es por no escribir bien la key
print(my_dict["Apellidos"]) #solución

# Type Error #
# print(my_list["Nombre"])  #en este caso le estamos pidiendo una propiedad de diccionario a una lista que no posee tal propiedad

# Import Error #
# from math import sen #en este caso el error ocurre por pedir un objeto o función mal escrito o que no existe
from math import sin #en este caso ya funciona
print(sin(1))

# Value Error #
#my_int = int("10 años")    #aquí el error es que esta transformación no ocurrirá
my_int = int("10")
print(my_int) #algo así si se puede hacer

# Zerodivision Error #
x=10
# print((x**2-100)/(x-10))         #aquí el error tan simple como que se está dividiendo entre cero
print(x+10) #en este caso, podemos usar límites para evitar este error
