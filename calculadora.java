
import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int option;

        System.out.println("****Calculadora****");
        System.out.println("1.- Suma");
        System.out.println("2.- Resta");
        System.out.println("3.- Multiplicacion");
        System.out.println("4.- Division");
        System.out.println("5.- Salir");

        System.out.print("Elige qué deseas hacer: ");
        option = sc.nextInt();

        if (option == 5) {
            System.out.println("Hasta luego :))");
        } else if (option >= 1 && option <= 4) {
            System.out.print("Elige el primer número: ");
            int num1 = sc.nextInt();
            System.out.print("Elige el segundo número: ");
            int num2 = sc.nextInt();

            switch (option) {
                case 1:
                    System.out.println("Resultado: " + (num1 + num2));
                    break;
                case 2:
                    System.out.println("Resultado: " + (num1 - num2));
                    break;
                case 3:
                    System.out.println("Resultado: " + (num1 * num2));
                    break;
                case 4:
                    if (num2 == 0) {
                        System.out.println("No se puede dividir entre cero");
                    } else {
                        System.out.println("Resultado: " + ((double)num1 / num2));
                    }
                    break;
            }
        } else {
            System.out.println("Opción no válida. Intenta otra vez");
        }

        sc.close();
    }
}
