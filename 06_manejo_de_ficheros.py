### Manejo de ficheros ###

# fichero txt:
txt_file = open("Intermedio/my_file.txt","r+") #aquí usamos la operación open para abrirlo, luego su ruta y un w para escribir, o r para leer y r+,w+ para ambos
#si no existe el fichero, lo crea.
#print(txt_file.read(10)) #lee los primeros 10 caracteres
#print(txt_file.read(10)) #lee otros 10 caracteres
#print(txt_file.readline(-1)) #lee una línea o lo que reste de ella
#print(txt_file.readlines()) #lee las lineas que queden y las vuelve una list
for a in txt_file.readlines():
    print(a)#imprimimos cada linea por separado
txt_file.write("\nAunque también me gusta la física teórica") #escribe una nueva línea con el salto de línea aunque al inicio si todavía no se ha leído
print(txt_file.read())
txt_file.close() #con esto cierra el fichero, deja de ejecutarse
import os #usando este modulo
# os.remove("Intermedio/my_file.txt")              #podemos borrar el archivo mediante su ruta

# fichero .json
import json #este modulo sirve para trabajar con archivos json
json_file = open("Intermedio/my_file.json","w+") #funciona igual al caso anterior, pero siempre crea el archivo o lo reinicia
json_test = {
    "name": "Brian",
    "last name": "Parra",
    "age": "27",
    "languages": ["Python","Swift","Kotlin"]} #aqui tenemos un diccionario, similar a los archivos json
json.dump(json_test,json_file,indent=None) #en este caso, dice qué escribe y donde lo escribe, indent ayuda a que sea más legible el archivo
#en el caso none se hace lo más compacto posible y con 1,2,3,etc. se va extendiendo para hacerlo más legible. Además es el espacio delante de la línea
json_file.close() #lo cerramos
with open("Intermedio/my_file.json") as my_other_file: #lo volvemos a abrir y lo leemos
    for ln in my_other_file.readlines():
        print(ln) 
json_dict = json.load(open("Intermedio/my_file.json")) #asignamos la estrucutura a un diccionario
print(type(json_dict)) #y en efecto, se trata de un diccionario. Con esto ya le podemos aplicar lo que sabemos sobre diccionarios.

#Fichero .csv
import csv
csv_file = open("Intermedio/my_file.csv","w+")
csv_writer = csv.writer(csv_file)
csv_file.writelines(["name","lastname","age","language"])
csv_file.writelines(["Brian","Parra","27","Python"])
csv_file.close()
with open("Intermedio/my_file.csv") as my_another_file:
    for ln in my_another_file.readlines():
        print(ln)

#Fichero .xlsx
# import xlrd #en este caso debe instalarse el modo}

#Fichero .xml
import xml
