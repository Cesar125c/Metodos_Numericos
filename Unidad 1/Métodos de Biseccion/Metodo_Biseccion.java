/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @integrantes Kevin Chicaiza, Alex Muzo, Emily Guerron, Cesar Cueva, Carlos Robayo
 * Metodos Numericos
 * Paralelo 002
 * Fecha: 13/06/2023
 * Tema: Metodo Biseccion
 */
import java.util.Scanner;

public class Metodo_Biseccion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ingresar los valores iniciales
        System.out.print("Ingrese el valor de 'a': ");
        double a = scanner.nextDouble();

        System.out.print("Ingrese el valor de 'b': ");
        double b = scanner.nextDouble();

        System.out.print("Ingrese la tolerancia: ");
        double tolerance = scanner.nextDouble();

        // Llamada al método de bisección
        double root = bisectionMethod(a, b, tolerance);

        // Mostrar el resultado
        System.out.println("La raíz aproximada es: " + root);
    }

    public static double bisectionMethod(double a, double b, double tolerance) {
        double c = (a + b) / 2;

        while (Math.abs(a - b) > tolerance) {
            if (function(a) * function(c) < 0) {
                b = c;
            } else {
                a = c;
            }

            c = (a + b) / 2;
        }

        return c;
    }

    // Función de ejemplo: f(x) = x^3 - x - 2
    public static double function(double x) {
        return Math.pow(x, 3) - x - 2;
    }
}
