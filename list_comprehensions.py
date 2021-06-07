def run():
    # squares = []
    # for i in range (1, 10):
    #     if i % 3 != 0: # Los numeros divisible por 3 los elimino y los que quedan los elevo a la 2
    #         squares.append(i**2)
    # print(squares)

# RESOLVEMOS EL MISMO PROBLEMA CON LIST COMPREHENSIONS

    # squares = [i**2 for i in range(1, 10) if i % 3 != 0] # Para cada elemento(i) en el rango(1, 9), voy a elevar ese elemento **2, solo si se cumple la condicion (si el elemento divisible por tres es distinto de cero)
    # print(squares)

# RETO:
    squares = [i for i in range(1, 200) if i % 36 == 0]# El numero 36 abarca los numeros divisibles 4, 6 y 9
    print(squares)

if __name__ == "__main__":
    run()