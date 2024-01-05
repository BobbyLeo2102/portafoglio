import functions as f


          
print("*" * 47)
print("*" * 10 + "Calcolatrice in costruzione" + "*" * 10)
print("*" * 47)
print("\n\n")


while True:
    operacion = input("Inserte el simbolo de la operación aritmética que desea realizar (o 'exit' para salir) ==> ")

    if operacion == "exit":
        break

    if operacion == "+":
        resultado = f.suma()  # Llama a la primera función de la lista
    elif operacion == "-":
        resultado = f.resta()  # Llama a la segunda función de la lista
    elif operacion == "*":
        resultado = f.mult() 
    elif operacion == "/":
        resultado = f.division()  
    else:
        print("Operación no válida")
        continue

    #print("Resultado de la operación:", resultado)



# -----------------------------------------------------------------------------
