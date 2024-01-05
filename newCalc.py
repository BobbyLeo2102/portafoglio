import functions as f #<== import this file as a module


          
print("*" * 47) #simple graphics before entering into the menu 
print("*" * 10 + "Calcolatrice in costruzione" + "*" * 10)
print("*" * 47)
print("\n\n")


while True: #I use this loop to keep the app working unless the user doesn't want it.
    operacion = input("Inserte el simbolo de la operación aritmética que desea realizar (o 'exit' para salir) ==> ")

    if operacion == "exit":
        break

    if operacion == "+":
        resultado = f.suma()  # call the first function of the list
    elif operacion == "-":
        resultado = f.resta()  # call the second function of the list, and so on...
    elif operacion == "*":
        resultado = f.mult() 
    elif operacion == "/":
        resultado = f.division()  
    else:
        print("Operación no válida")
        continue

# -----------------------------------------------------------------------------
