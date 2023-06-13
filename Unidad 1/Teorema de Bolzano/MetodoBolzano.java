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
 * Tema: Metodo bolzano
 */
public class MetodoBolzano {
        public static double MetodoBolzano(double a, double b, double epsilon) {
        double fa = funcion(a);
        double fb = funcion(b);
        
        if (fa * fb >= 0) {
            System.out.println("El teorema de Bolzano no se cumple en el intervalo dado.");
            return Double.NaN;
        }
        
        double c;
        
        while (Math.abs(b - a) > epsilon) {
            c = (a + b) / 2;
            double fc = funcion(c);
            
            if (Math.abs(fc) < epsilon) {
                return c;
            }
            
            if (fa * fc < 0) {
                b = c;
                fb = fc;
            } else {
                a = c;
                fa = fc;
            }
        }
        
        return (a + b) / 2;
    }

    public static void main(String[] args) {
        double a = 0.0; // Extremo izquierdo del intervalo
        double b = 3.0; // Extremo derecho del intervalo
        double epsilon = 0.0001; // Tolerancia
        
        double resultado = MetodoBolzano(a, b, epsilon);
        
        if (!Double.isNaN(resultado)) {
            System.out.println("Aproximación de la raíz: " + resultado);
        }
    }
    
    
    
        private static double funcion(double a) {
            throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
        }
    }
    
