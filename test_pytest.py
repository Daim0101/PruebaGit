
import logging

# Configurar el registro
logging.basicConfig(level=logging.DEBUG, filename='myapp.log', filemode='w')


def test_resta():
    num1 = 1 #int(input("Introduce el primer número: "))
    num2 = 2 #int(input("Introduce el segundo número: "))
    result = num1 - num2
    print("La suma es:", result)

def test_suma():
    num1 = 1 #int(input("Introduce el primer número: "))
    num2 = 2 #int(input("Introduce el segundo número: "))

    result = num1 + num2
    print("La suma es:", result)
