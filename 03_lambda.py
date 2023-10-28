### Lambda ###
#Las lambdas se pueden entender como un tipo de funcion anónima, es decir, sin nombre.
sum_two_values = lambda first_value, second_value: first_value + second_value
#lo anterior es: variable donde se guarda = "lamba" "parámetros": "lo que devuelve"
print(sum_two_values(1,9)) #opera similar a una función

multiply_values = lambda first_value, second_value: first_value*second_value
print(multiply_values(2,3))

def sum_three_values(first_value):
    return lambda second_value, third_value: first_value + second_value + third_value #se pueden usar lambdas dentro de funciones
my_sum = sum_three_values(3)(4,5) #pero así se deben meter los parámetros
print(my_sum) #puede servir para separar los parámetros en dos grupos