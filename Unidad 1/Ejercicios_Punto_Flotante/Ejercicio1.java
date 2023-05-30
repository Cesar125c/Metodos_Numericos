/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package NumeroRepresentacion;

/**
 *
 * @integrantes Kevin Chicaiza, Alex Muzo, Emily Guerron, Cesar Cueva, Carlos Robayo
 * Metodos Numericos
 * Paralelo 002
 * Fecha: 29/05/2026
 * Tema: Punto flotante
 */


/*
Ejercicio1. Indique la representación de los siguientes números, razonando su respuesta:
a) -16 en complemento a 2 con 5 bits
b) -16 en complemento a 1 con 5 bits
c) +13 en signo magnitud con 5 bits
d) -14 en complemento a dos con 5 bits

*/
public class Ejercicio1 {
    public static void main(String[] args) {
        //se definen los numeros que vamos a convertir a binario y la invocacion de las funciones autilizar

        // a) -16 en complemento a dos con 5 bits
        int a = -16;
        String aComplementoDos = complementoDos(a, 5);
        System.out.println("a) -16 en complemento a dos con 5 bits: " + aComplementoDos);
        
        // b) -16 en complemento a uno con 5 bits
        int b = -16;
        String bComplementoUno = complementoUno(b, 5);
        System.out.println("b) -16 en complemento a uno con 5 bits: " + bComplementoUno);

        // c) +13 en signo magnitud con 5 bits
        int c = 13;
        String cSignoMagnitud = signoMagnitud(c, 5);
        System.out.println("c) +13 en signo magnitud con 5 bits: " + cSignoMagnitud);

        // d) -14 en complemento a dos con 5 bits
        int d = -14;
        String dComplementoDos = complementoDos(d, 5);
        System.out.println("d) -14 en complemento a dos con 5 bits: " + dComplementoDos);
    }

    // Función para calcular el complemento a uno
    public static String complementoUno(int number, int bits) {
        //Calcula el valor máximo que puede ser representado en complemento a uno con el número de bits dado
        int max = (int) Math.pow(2, bits - 1) - 1;
        //Calcula el valor mínimo que puede ser representado en complemento a uno
        int min = -max;

        //Verifica si el número dado está dentro del rango representable en complemento a uno 
        if (number >= min && number <= max) {
            StringBuilder binary = new StringBuilder(Integer.toBinaryString(Math.abs(number)));
            while (binary.length() < bits) {
                binary.insert(0, "0");
            }

            if (number < 0) {
                binary = complement(binary);
            }

            return binary.toString();
        }
        //Si el número dado está fuera del rango representable
        else {
            return "El número no es representable en " + bits + " bits";
        }
    }

    // Función para calcular el complemento a dos
    public static String complementoDos(int number, int bits) {
        //Calcula el valor máximo que puede ser representado en complemento a dos
        int max = (int) Math.pow(2, bits - 1) - 1;
        int min = -max - 1;

        if (number >= min && number <= max) {
            
            //Comprueba si el número original es mayor convierte el número dado en una representación binaria 
            if (number >= 0) {
                StringBuilder binary = new StringBuilder(Integer.toBinaryString(number));
                while (binary.length() < bits) {
                    binary.insert(0, "0");
                }
                return binary.toString();
            } 
            //Si el número original es negativo
            else {
                int complement = (int) Math.pow(2, bits) + number;
                String binary = Integer.toBinaryString(complement);
                return binary.substring(binary.length() - bits);
            }
        } else {
            return "El número no es representable en " + bits + " bits";
        }
    }

    // Función para calcular la representación en signo magnitud
    public static String signoMagnitud(int number, int bits) {
        int max = (int) Math.pow(2, bits - 1) - 1;
        int min = -max;

        if (number >= min && number <= max) {
            //Convierte el valor absoluto del número dado en una representación binaria
            StringBuilder binary = new StringBuilder(Integer.toBinaryString(Math.abs(number)));
            
            //oVerifica si la longitud de la representación binaria es menor que el número de bits menos uno. Si es así, se agregan ceros a la izquierda para completar los bits faltantes
            while (binary.length() < bits - 1) {
                binary.insert(0, "0");
            }

            //Si el número es negativo, se inserta un uno al principio de la representación binaria para indicar el signo negativo
            if (number < 0) {
                binary.insert(0, "1");
            } else {
                //Si el número es positivo, se inserta un cero al principio de la representación binaria 
                binary.insert(0, "0");
            }

            return binary.toString();
        } else {
            return "El número no es representable en " + bits + " bits";
        }
    }

    // Función para calcular el complemento de un número en binario
    public static StringBuilder complement(StringBuilder binary) {
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '0') {
                binary.setCharAt(i, '1');
            } else {
                binary.setCharAt(i, '0');
            }
        }
        return binary;
    }
}

