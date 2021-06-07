# divisors es el nombre de la funcion y (num) es el parametro
def divisors(num): # Funcion que recibe un numero como parametro y retornar una lista con todos los divisores de ese número
    divisors = [] # Lista vacia
    for i in range(1, num + 1): # Ciclo que va del 1 al mismo número que yo ingrese, le sumo 1 ya que no se incluye
        if num % i == 0: # Si el resto de la division es igual a cero (si es divisible) vamos a agregar  nuestra lista de divisores, ese numero (i)
            divisors.append(i)
    return divisors # Devolver los divisores

def run():
    try: # En el try colocamos codigo que esperamos que pueda lanzar un error
        num = int(input("Enter a number: "))
        print(divisors(num))
        print("I finished my program")
    except ValueError: # En el except manejo el error, deja de ejecurtarse try y se ejecuta lo que yo señale con except.
        print("You must enter a number")

#RETO
    # try:
    #     num = int(input("Enter a number: "))
    #     if num < 0:
    #         raise Exception("Negative number is not valid")
    #     print(divisors(num))
    #     print("Finish")

    # except ValueError:
    #     print("You can only add numbers")
    # except Exception:
    #     print("The number cannot be negative")

if __name__ == "__main__":
    run()