### Compresión de listas ###
my_original_list = [35,24,62,52,30,30,17]
my_list = [i for i in my_original_list] #de esta manera se comprime la lista, pero queda igual que la anterior
my_list_1 = [i for i in range(1,8)] #esta forma crea valores del 1 al 7:
#incluso de forma más rápida con list(range(1,8))
print(my_original_list, my_list,my_list_1)
#la gracia de esto, es poder operar con listas de forma directa:
sq_list = [i**2 for i in my_original_list] #aquí almacenamos el cuadrado de los npumero de  my_original_list
print(my_original_list,sq_list)
def isodd(n):
    if n%2==0:
        return 1
    else:
        return 0
#podemos mezclar con funciones:


pair_list = [isodd(i) for i in my_original_list]
l=0
for i in pair_list:
    l+=i
print(f"numero de pares en la lista {my_original_list}, es {l}") #e incluso aprovechar para saber la cantidad de pares en una lista