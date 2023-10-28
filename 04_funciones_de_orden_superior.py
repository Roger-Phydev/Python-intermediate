### Funciones de orden superior ###
def sum_one(value): #esta es una función común
    return value + 1
def sum_two_values_and_one(first_value,second_value): 
    return sum_one(first_value+second_value)#esta función usa la función anterior, pero aún no es de orden superior
def sum_two_values_and_add_high(first_value,second_value,f_sum_one): #esta función si es de orden superior
    return f_sum_one(first_value+second_value) #acepta una función como parámetro
print(sum_two_values_and_one(5,6)) #12
print(sum_two_values_and_add_high(5,6,sum_one)) #12
def sum_six(value):
    return value + 6
print(sum_two_values_and_add_high(5,6,sum_six)) #podemos cambiar la función por otra, en este caso da 17

### Closures ###

def sum_ten(value_zero=0):
    def add(value): #aquí hay una función definida
        return value + 10 + value_zero
    return add # y regresa una función
print(sum_ten()(121)) #131.
print(sum_ten(9)(121)) #140
#Un closure es una función que devuelve una función

### Funciones de orden superior de default ###
numbers = [2,5,10,21]

# Map #
def multiply_two(number):
    return 2*number
print(list(map(multiply_two,numbers))) #le pasamos una función y un iterable, en este caso: una lista.
#en este caso, aplica la función a cada elemento del iterable
print(list(map(lambda number: 2*number,numbers))) #hace lo mismo, pero ahora con una lambda, esto simplifica el código

# Filter #
def filter_greater_than_ten(number):
    if number>10:
        return True
    else: 
        False
print(list(filter(filter_greater_than_ten,numbers))) #en este caso, filtra usando una función
#booleana como criterio, es decir, que solo diga True o False y según el resultado, lo añade o no.
print(list(filter(lambda number: number>10,numbers))) #esta es la forma más simple con lambda

# Reduce #
from functools import reduce #se debe importar
print(reduce(sum_two_values_and_one,numbers)) #aplica la función a los dos primeros, luego el resultado lo toma
#como primer valor y el siguiente elemento como segundo. Continúa hasta llegar al final

