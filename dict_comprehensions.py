def run():
    # my_dict = {}

    # for i in range(1, 10):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3
    # print(my_dict)

# CREO LO ANTERIOR CON DICTIONARY COMPREHENSIONS:

    # my_dict = {i: i**3 for i in range(1, 10) if i % 3 != 0}
    # print(my_dict) 

# RETO
    my_dict = {i: round(i**0.5, 2) for i in range(1, 10)} # Para cada elemento del 1 al 9, imprimir al elememnto elevado a la 0.5 pero redondeado a la 2 (2 numeros despues de la coma)
    print(my_dict)

if __name__ == "__main__":
    run()