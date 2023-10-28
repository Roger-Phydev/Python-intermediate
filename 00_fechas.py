### Fechas ###
## Date time ##
from datetime import datetime #en este caso, tenemos un modulo relacionado a fechas.
def print_date(date):#esta función imprime la fecha separando cada valor
    print("Año: ",date.year)
    print("Mes: ",date.month)
    print("Día: ",date.day)
    print("Hora: ",date.hour)
    print("Minutos: ",date.minute)
    print("Segundos: ",date.second)
    print("Time stamp: ",date.timestamp())#esta es una representación única de un tiempo. Contiene toda la información del día, pero en formato estándar simplificado
now = datetime.now() #en este caso, nuestra variable now contiene la fecha actual hasta fracciones de segundo
print_date(now)
year_2024 = datetime(2024,1,1) #para definir una fecha necesitamos por lo menos año, mes y día en ese orden. Los argumentos que faltan se hacen 0 por defecto
print_date(year_2024)
## Time ##
from datetime import time
current_time = time(21,6,12) #aunque parece igual, este dato solo contiene horas y no la fecha, se rellena por hora, minuto y segundo
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
null_time = time() #en este caso será 0hrs, 0 min y 0 segundos
## Date ##
from datetime import date #en este caso solo cuenta con la fecha
current_date = date(2021,9,26)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday()) #dia de la semana: 0=domingo, lunes=1,...,sabado=6
print(date.today())
#De esta forma, se puede concluir que: datetime = date + time
## Operaciones con fechas ##
print(current_date)
current_date = date(current_date.year,current_date.month+3,current_date.day -6) #así se puede modificar la fecha
print(current_date) #hay otra manera de operar con fechas:
from datetime import timedelta
diff = year_2024 - now  #si los objetos son del mismo tipo, en este caso datetime...
print(diff) #la diferencia indica el tiempo que falta para llegar de now a year 2024
diff = year_2024.date() - current_date
print(diff)
#sin embargo, cosas como year_2024.time - current_time no son válidas.
init_time_delta = timedelta(days=200,weeks=3)
end_time_delta = timedelta(days=300,weeks=6) #con esto se pueden definir aumentos de tiempo
print(end_time_delta-init_time_delta)#se pueden restar
print(end_time_delta+init_time_delta) #se pueden sumar, pero no multiplicar ni dividir
#el time delta sirve para trabajar con diferencias de tiempo, no para fechas, sino solo para duración.
