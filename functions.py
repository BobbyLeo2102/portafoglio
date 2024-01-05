from numpy import double

def suma():
    a = float(input("Inserte el primer digito ==> "))
    b = float(input("Inserte el segundo digito ==> "))
    resultado = a + b
    print("El resultado de la suma es ==> ", resultado)

def resta():
    a = float(input("Inserte el primer digito ==> "))
    b = float(input("Inserte el segundo digito ==> "))
    resultado = a - b
    print("El resultado de la resta es ==> ", resultado)

def mult():
    a = float(input("Inserte el primer digito ==> "))
    b = float(input("Inserte el segundo digito ==> "))
    resultado = a * b
    print("El resultado de la multiplicacion es ==> ", resultado)

def division():
    a = float(input("Inserte el primer digito ==> "))
    b = float(input("Inserte el segundo digito ==> "))
    if b != 0:
        resultado = a / b
        print("El resultado de la division es ==> ", resultado)
    else:
        try:
            resultado = a / b
        except ZeroDivisionError:
            print("Insertar numero diferente de cero \n")