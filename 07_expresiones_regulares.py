### Expresiones regulares ###
import re #este es el modulo para expresiones regulares

# Match #
my_string = "Esta es la lexión número 7: Lexión de Expresiones regulares" #usaremos una cadena de texto para este tema
my_other_string = "Esta no es la lección número 6: Lección de manejo de ficheros"
print(re.match("Esta es la lección",my_string)) #aquí busca si la expresión se encuentra presente en my_string pero desde el inicio
#indica entre que caracteres está la oración:
print(my_string[0:19])
print(re.match("Esta es la lexión",my_other_string)) #en este caso no lo encontrará
print(re.match("Expresiones regulares",my_string)) #en este caso tampoco, pues se encuentra al final
match = re.match("Esta es la lexión",my_string)
print(match.span()) #esta es la lista donde aparece la oración
start,end = match.span() #aqui tomamos los valores de inicio y fin de la cadena
print(my_string[start:end])

# Search #
search = re.search("lexión",my_string,re.I) #este busca en toda la cadena hasta encontrarla re.I ignora mayúsculas y minúsculas
print(search)
start,end = search.span()
print(my_string[start:end]) #siempre encuentra la primer ocurrencia

# Findall #
find_all = re.findall("lexión",my_string,re.I) #aquí funciona similar a la anterior
print(find_all) #pero aquí guarda las veces ocurridas, no solo la primera

# Split #
print(re.split(":",my_string)) #separa usando un patrón y lo vuelve una lista

# Sub #
print(re.sub("Expresiones","expresiones",my_string)) #sustituimos la primer cadena por la segunda en la correspondiente variable
#print(re.sub("lexión|Lexión","Lección",my_string)) #aquí, usamos | para separar cadenas que se cambiarán
print(re.sub("[L|l]exión","Lección",my_string))    #esta es otra posibilidad


## Patrones ##
#Un patrón hace referencia a una especie de expresión que cumple ciertas características, teniendo así, englobadas varias palabras posibles
#Esto es diferente a lo que hemos hecho, pues esos ejemplos solo buscan una expresión muy concreta, aquí es más libre y holgado
pattern = r"[Ll]exión|Expresiones" #este ya es un ejemplo, pues contiene tres posibles palabras, r sirve para señalar que es un patrón
print(re.findall(pattern,my_string))

pattern = r"[a-z]"
print(re.findall(pattern,my_string)) #aqui pinta todas las letras de la a a la z en minúscula

pattern = r"[0-9]"
print(re.findall(pattern,my_string)) #aqui aparecen solo números de 0 a 9
print(re.search(pattern,my_string)) #con los patrones sirve también el search, pero no match

pattern = r"\d"
print(re.findall(pattern,my_string)) #aqui omite letras

pattern = r"\D"
print(re.findall(pattern,my_string)) #aquí omite números

pattern = r"[l]."
print(re.findall(pattern,my_string)) #busca algo que tenga l+otra letra.

pattern = r"[t].*"
print(re.findall(pattern,my_string)) #muestra de donde aparece la t acompañada de algo en adelante

pattern = r"[0,9]"
print(re.findall(pattern,my_string))

#E-mail:
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$" #este patrón busca:
    #algo que empiece por una combinación de letras cualesquiera,numeros del 0 al 9, punto, el simbolo + y -
    #seguido de un @, seguido de otra combinación de caracteres
    #seguido de algo que tenga un punto. al inicio y otro caracter
    # y que continue hasta que termine (señalado con +$)
    return re.match(pattern,email) #devuelve si concuerda
email = "brian10"
print(is_valid_email(email)) #aquí no encuentra
email+= "@hotmail"
print(is_valid_email(email)) #aún no es nada
email+=".com"
print(is_valid_email(email)) #ahora ya sirve

## Herramienta para construcción de patrones ##
#Por último, es necesario saber que existe una página que ayuda sobre como construir un patrón a partir de una expresión de ejemplo
#El link es : https://regex101.com/