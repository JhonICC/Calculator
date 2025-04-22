# Pide dos números y una operación (+, -, *, /) al usuario.
# Muestra el resultado según la operación que elija.

print("****Calculadora****")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
print("5.- Salir")

option = int(input("Elije que deseas hacer: "))
num1 = int(input("Elije el primer numero: "))
num2 = int(input("Elije el segundo numero: "))

if option == 1:
    print(num1 + num2)
elif option == 2:
    print(num1 - num2)
elif option == 3:
    print(num1 * num2)
elif option == 4:
    # Doble if para que no se pueda dividir entre 0
    if num1 == 0 or num2 == 0:
        print("No se puede dividir entre 0")
    else:
        print(num1/num2)
elif option == 5:
    print("Hasta luego :))")
else:
    print("Introduce una opcion valida")


