def divisors(num): 
    divisors = [] 
    for i in range(1, num + 1): 
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Enter a number: ") # Si el usuario nos coloca una letra, assert devolvera falso. Si coloca un numero va a devolver verdadero
    assert num.isnumeric(), "You must enter a number" # isnumeric -> es un metodo (condicion) de las string que devuelve verdadero si el string se corresponde a un numero y falso si no se corresponde y , el mensaje de error que nos mostrara
    print(divisors(int(num))) # Ahora si convierto el numero a entero, antes de esto se controla que sea un numero con assert
    print("I finished my program")

# RETO
# def run():
#     num = input("Enter a number: ")
#     assert num.isnumeric() and int(num) > 0, "Enter only positive numbers"
#     print(divisors(int(num)))
#     print("I finished my program")
    

if __name__ == "__main__":
    run()