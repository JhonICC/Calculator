# Pide dos números y una operación (+, -, *, /) al usuario.
# Muestra el resultado según la operación que elija.

print("****Calculadora****")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
print("5.- Salir")

option = int(input("Elige qué deseas hacer: "))

if option == 5:
    print("Hasta luego :))")
elif option >= 1 and option <= 4:
    num1 = int(input("Elige el primer número: "))
    num2 = int(input("Elige el segundo número: "))

    if option == 1:
        print("Resultado:", num1 + num2)
    elif option == 2:
        print("Resultado:", num1 - num2)
    elif option == 3:
        print("Resultado:", num1 * num2)
    elif option == 4:
        if num2 == 0:
            print("No se puede dividir entre cero")
        else:
            print("Resultado:", num1 / num2)
else:
    print("Opción no válida. Intenta otra vez")
