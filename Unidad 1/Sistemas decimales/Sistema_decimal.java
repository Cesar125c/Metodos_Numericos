
package Sistema_decimal;

/**
 *
 * @integrantes Kevin Chicaiza, Alex Muzo, Emily Guerron, Cesar Cueva, Carlos Robayo
 * Metodos Numericos
 * Paralelo 002
 * Fecha: 19/05/2023
 */
public class Sistema_decimal {
     public static void main(String[] args) {
        // Paso 1: Convertir 101111 (2) a decimal
        String binario = "101111";
        int decimal1 = Integer.parseInt(binario, 2);
        System.out.println("Ejercicio 1: ");
        System.out.println("101111 (2) = " + decimal1 + " (10)");

        // Paso 2: Convertir 27025 (10) a binario
        int decimal2 = 27025;
        String binario2 = Integer.toBinaryString(decimal2);
        System.out.println("Ejercicio 2: ");
        System.out.println("27025 (10) = " + binario2 + " (2)");

        // Paso 3: Convertir 42 (8) a decimal
        String octal = "42";
        int decimal3 = Integer.parseInt(octal, 8);
        System.out.println("Ejercicio 3: ");
        System.out.println("42 (8) = " + decimal3 + " (10)");

        // Paso 4: Convertir 64 (10) a binario
        int decimal4 = 64;
        String binario4 = Integer.toBinaryString(decimal4);
        System.out.println("Ejercicio 4: ");
        System.out.println("64 (10) = " + binario4 + " (2)");

        // Paso 5: Convertir 145 (10) a binario
        int decimal5 = 145;
        String binario5 = Integer.toBinaryString(decimal5);
        System.out.println("Ejercicio 5: ");
        System.out.println("145 (10) = " + binario5 + " (2)");

        // Paso 6: Convertir C (16) a decimal
        String hexadecimal = "C";
        int decimal6 = Integer.parseInt(hexadecimal, 16);
        System.out.println("Ejercicio 6: ");
        System.out.println("C (16) = " + decimal6 + " (10)");

        // Paso 7: Convertir ABCD (16) a decimal
        String hexadecimal2 = "ABCD";
        int decimal7 = Integer.parseInt(hexadecimal2, 16);
        System.out.println("Ejercicio 7: ");
        System.out.println("ABCD (16) = " + decimal7 + " (10)");
    }
    
}
