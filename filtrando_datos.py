DATA = [ # DATA EN MAYUSCULA PORQUE NO VA A SER MODIFICADA, ES UNA CONSTANTE
    # DATA CONTIENE LISTAS DE DIFERENTES DICCIONARIOS
    { # CONTIENEN LLAVES
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]



def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"] # De todos los trabajadores en data, guardar los nombres, solo si dominan el lenguaje python
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"] # De todos los trabajadores en data, guardar los nombres, solo si su organizacion es platzi
    adults = list(filter(lambda worker: worker["age"] > 18, DATA )) # Voy a guardar solamente los workers, si worker age es mayor a 18
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) # El operador pipe | sirve para sumar/unir diccionarios. Para cada uno de los trabajadores que estan dentro de data (para cada uno de los diccionarios), voy a guardar a ese mismo diccionarios pero sumado a un diccionario nuevo que contiene la llave old con el valor de evaluar la expresion worker age > 70, si esta expresion es true va a guardar verdadero, si es false va a guardar falso
 
    for worker in old_people: # ciclo
        print(worker)

if __name__ == "__main__":
    run()

# ALL PYTHON DEVS --> TODOS LOS DESARROLLADORES DE PYTHON
# ALL PLATZI WORKERS --> TODOS LOS TRABAJADORES DE PLATZI
# ADULTS --> PERSONAS MAYORES A 18 AÑOS
# WORKER --> TRABAJADORES