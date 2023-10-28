### Aquí se resuelven algunos retos sencillos ###
"""
FIZZBUZZ
Escribe un código que imprima los números del 1 al 100 (incluidos y con salto de línea)
con los siguientes cambios:
- en los multiplos de 3 pone "fizz" en lugar del número
- en los mulltiplos de 5 pone "buzz" en lugar del número
- en caso de ser multiplo de ambos, pone "fizzbuzz"
"""
def fizzbuzz():
    for i in range(1,101):#serán los número del 1 al 100 inclusive
        if i%3==0 and i%5==0: #se comienza con este, pues en caso de no cumplirse. Es importante que la primer condición sea la más restrictiva
            print("fizzbuzz")
        elif i%3==0: #los dos casos restantes son más sencillos
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
fizzbuzz()
"""
¿ES ANAGRAMA?
Escribe un código que reciba dos palabras (string) y retorne verdadero o falso según sean anagramas o no.
-un anagrama es una reordenación no trivial de otra palabra
-no es necesario saber si las palabras existen
-por lo anterior, una palabra no es anagrama de si misma
"""
def is_anagram(word_one,word_two):
    if word_one.lower() == word_two.lower():
        return False #con esto, prohibimos que una palabra sea anagrama de si misma
    return sorted(word_one.lower()) == sorted(word_two.lower()) #si ordenamos las palabras y quedan igual, serán anagrama
#en lo anterior, usamos sorted que convierte a lista y la ordena.
print(is_anagram("amor","AmOr"))
print(is_anagram("RoMA","AmOr"))
"""
SUCESIÓN DE FIBONACCI
escribe un programa que escriba los primeros 50 números de la sucesión de Fibonacci empezando por cero.
-dados dos números contiguos de la serie, el siguiente es la suma de ambos.
"""
def fibonacci():
    prev = 0
    next = 1
    for i in range(50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()
"""
PRIMOS
Crea un código que diga si un número es primo o no y al final imprima todos los primos del 1 al 100
"""
def is_prime():
    for j in range(2,101):
        divisor=2
        while j%divisor!=0:
            divisor+=1
        if divisor == j: #si el divisor es él mismo
            print(j) #lo imprimimos
is_prime()
"""
INVIRTIENDO CADENAS
crear un programa que invierta el orden de una cadena de texto sin usar funciones internas de Python
"""
def reverse(text):
    reversed_text = ""#este será nuestro texto volteado
    length = len(text)
    for i in range(0,length):
        reversed_text+= text[length-i-1] #usamos concatenación de caracteres
    return reversed_text
print(reverse("hola"))