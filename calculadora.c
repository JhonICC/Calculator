
#include <stdio.h>

int main() {
    int option, num1, num2;

    printf("****Calculadora****\n");
    printf("1.- Suma\n");
    printf("2.- Resta\n");
    printf("3.- Multiplicacion\n");
    printf("4.- Division\n");
    printf("5.- Salir\n");

    printf("Elige qué deseas hacer: ");
    scanf("%d", &option);

    if (option == 5) {
        printf("Hasta luego :))\n");
    } else if (option >= 1 && option <= 4) {
        printf("Elige el primer número: ");
        scanf("%d", &num1);
        printf("Elige el segundo número: ");
        scanf("%d", &num2);

        switch(option) {
            case 1:
                printf("Resultado: %d\n", num1 + num2);
                break;
            case 2:
                printf("Resultado: %d\n", num1 - num2);
                break;
            case 3:
                printf("Resultado: %d\n", num1 * num2);
                break;
            case 4:
                if (num2 == 0) {
                    printf("No se puede dividir entre cero\n");
                } else {
                    printf("Resultado: %.2f\n", (float)num1 / num2);
                }
                break;
        }
    } else {
        printf("Opción no válida. Intenta otra vez\n");
    }

    return 0;
}
