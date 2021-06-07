def run():
    my_list= ["Micaela", 1, 4.9, False] # Corchetes
    my_dict= {"Firstname": "Micaela", "Lastname": "Alarcon"} # Llaves

    super_list= [ # lista de diccionarios
        {"Firstname": "Marco", "Lastname": "Polo"},# Los elementos de una lista se separan por comas
        {"Firstname": "Wilson", "Lastname": "Vuelve"},
        {"Firstname": "Freddie", "Lastname": "Mercury"}
    ]

    super_dict= { # diccionario de listas
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.6, 5.8, 9.7]
    }

    # for i in super_list:
    #     for key, values in i.items():
    #         print(key, "-", values)

    for key, values in super_dict.items(): # Recorre las llaves y valores al mismo tiempo de un diccionario en un ciclo
        print(key, "-", values) # "-" sirve para separar

if __name__ == "__main__": # Ejecutamos la funcion run()
    run()