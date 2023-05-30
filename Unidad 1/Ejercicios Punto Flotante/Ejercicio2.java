/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @integrantes Kevin Chicaiza, Alex Muzo, Emily Guerron, Cesar Cueva, Carlos Robayo
 * Metodos Numericos
 * Paralelo 002
 * Fecha: 29/05/2026
 * Tema: Punto flotante
 */

/**
 * Ejercicio 2. Indique la representación de los siguientes números:
    a) -64 en complemento a uno con 7 bits
    b) -64 en complemento a dos con 7 bits
    c) 12 en signo magnitud con 6 bits
    d) 18 en complemento a dos con 5 bits
    Solución:
    a) -64 en complemento a uno con 7 bits
    El rango de representación es [-63, 63], por tanto, el número no es representable
    b) -64 en complemento a dos con 7 bits
    64 en binario con 7 bits es 1000000. Se complementa 0111111 y se suma 1, siendo el resultado 100000
    c) 12 en signo magnitud con 6 bits
    001100
    d) 18 en complemento a dos con 5 bits
    El rango de representación es [-16, 15], por tanto, el número no es representable.
 */
public class Ejercicio2 {
    public static void main(String[] args) {
        // a) -64 en complemento a uno con 7 bits
        String a = complementoUno(-64, 7);
        System.out.println("a) -64 en complemento a uno con 7 bits: " + a);

        // b) -64 en complemento a dos con 7 bits
        String b = complementoDos(-64, 7);
        System.out.println("b) -64 en complemento a dos con 7 bits: " + b);

        // c) 12 en signo magnitud con 6 bits
        String c = signoMagnitud(12, 6);
        System.out.println("c) 12 en signo magnitud con 6 bits: " + c);

        // d) 18 en complemento a dos con 5 bits
        String d = complementoDos(18, 5);
        System.out.println("d) 18 en complemento a dos con 5 bits: " + d);
    }

    public static String complementoUno(int number, int bits) {
        StringBuilder binary = new StringBuilder(Integer.toBinaryString(Math.abs(number)));
        while (binary.length() < bits) {
            binary.insert(0, "0");
        }

        if (number < 0) {
            for (int i = 0; i < binary.length(); i++) {
                char c = binary.charAt(i);
                binary.setCharAt(i, (c == '0') ? '1' : '0');
            }
        }

        return binary.toString();
    }

    public static String complementoDos(int number, int bits) {
        StringBuilder binary = new StringBuilder(Integer.toBinaryString(Math.abs(number)));
        while (binary.length() < bits) {
            binary.insert(0, "0");
        }

        if (number < 0) {
            boolean carry = true;
            for (int i = binary.length() - 1; i >= 0; i--) {
                char c = binary.charAt(i);
                if (carry) {
                    if (c == '0') {
                        binary.setCharAt(i, '1');
                        carry = false;
                    } else {
                        binary.setCharAt(i, '0');
                    }
                }
            }
        }

        return binary.toString();
    }

    public static String signoMagnitud(int number, int bits) {
        StringBuilder binary = new StringBuilder(Integer.toBinaryString(Math.abs(number)));
        while (binary.length() < bits - 1) {
            binary.insert(0, "0");
        }

        if (number < 0) {
            binary.setCharAt(0, '1');
        } else {
            binary.setCharAt(0, '0');
        }

        return binary.toString();
    }
    
}
