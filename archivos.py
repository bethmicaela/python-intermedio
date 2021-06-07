def read(): # Lee el archivo numbers.txt que contiene los numeros
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f: # Abro el archivo, with(manejador contextual) impide que nuestro archivo se rompa si el programa se cierra inesperadamente. El parámetro"r" significa que va a leer el archivo. El parametro encoding="utf-8" sirve para que no haya errores con tildes o ñ por ejemplo.
        for line in f: # Recorrer cada linea dentro de nuestro archivo
            numbers.append(int(line))
    print(numbers)
    
def write():
    names = ["María", "Fernanda"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f: # "a" Agrega escritura al final y "w" Sobreescribe(borra) el texto anterior con lo que edito.
        for name in names: # Recorrer cada elemento de nuestra lista names
            f.write(name) # Escribir cada elemento
            f.write("\n") # Escribir salto de linea
    # Se ejecuta en consola pero se visualiza en el archivo names.txt
def run():
    write()

if __name__ == "__main__":
    run()