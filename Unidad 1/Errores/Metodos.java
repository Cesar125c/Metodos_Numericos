
package Errores;

/**
 *
 * @integrantes Kevin Chicaiza, Alex Muzo, Emily Guerron, Cesar Cueva, Carlos Robayo
 * Metodos Numericos
 * Paralelo 002
 * Fecha: 19/05/2023
 */
public class Metodos {

    public static void main(String[] args) {
        double aStar = 0.51e2; // a* = 0.51*10^2
        double a = 0.50e2; // a = 0.50*10^2
        
        double absoluteError = Math.abs(aStar - a);
        double relativeError = absoluteError / Math.abs(a);

        System.out.println("Error absoluto: " + absoluteError);
        System.out.println("Error relativo: " + relativeError);
    }
}
