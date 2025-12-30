### File Handling ###

import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open('./my_file.txt', 'w+') 

txt_file.write("Mi nombre es Jona\nMi apellido es Alfaro\n24 años\nY mi lenguaje preferido es Python")

# Posiciona el cursor al inicio del fichero
txt_file.seek(0)

# Lee e imprime todo el contenido del fichero
print(txt_file.read())

# Lee e imprime 10 caracteres desde el inicio del fichero
txt_file.seek(0)
print(txt_file.read(10))

# Lee e imprime el resto de la línea actual desde la posición 11
print(txt_file.readline())

# Lee e imprime la siguiente línea
print(txt_file.readline())

# Lee e imprime las líneas restantes del fichero
for line in txt_file.readlines():
    print(line)

# Escribe una nueva línea en el fichero
txt_file.write("\nAunque también me gusta C#")

# Posiciona el cursor al inicio del fichero, lee e imprime todo su contenido
txt_file.seek(0)
print(txt_file.read())

# Cierra el fichero
txt_file.close()

# Agrega una nueva línea en el fichero
with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY PHP")

# os.remove("Intermediate/my_file.txt")

# .json file

json_file = open('./my_file.json', 'w+')

json_test = {
  "name": "Jonathan",
  "surname": "Alfaro",
  "age": 24,
  "languages": ["Python", "C#", "php"],
  "website": "https://github.com/Virgi02i87167"
}

json.dump(json_test, json_file, indent=4)

json_file.close()

with open("./my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv

csv_file = open("./my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Jonathan", "Alfaro", 24, "Python", "https://github.com/Virgi02i87167"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("./my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)