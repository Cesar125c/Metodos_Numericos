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


/*
Ejercicio1. Indique la representación de los siguientes números, razonando su respuesta:
a) -16 en complemento a 2 con 5 bits
b) -16 en complemento a 1 con 5 bits
c) +13 en signo magnitud con 5 bits
d) -14 en complemento a dos con 5 bits

*/
public class Ejercicio1 {
    public static void main(String[] args) {
        // -16 en complemento a dos con 5 bits
       int numA = -16;
        String representacionA = obtenerRepresentacionComplementoDos(numA, 5);
        System.out.println("a) -16 en complemento a dos con 5 bits: " + representacionA);

        // -16 en complemento a uno con 5 bits
        int numB = -16;
        String representacionB = obtenerRepresentacionComplementoUno(numB, 5);
        System.out.println("b) -16 en complemento a uno con 5 bits: " + representacionB);

        // +13 en signo magnitud con 5 bits
        int numC = 13;
        String representacionC = obtenerRepresentacionSignoMagnitud(numC, 5);
        System.out.println("c) +13 en signo magnitud con 5 bits: " + representacionC);

        // -14 en complemento a dos con 5 bits
        int numD = -14;
        String representacionD = obtenerRepresentacionComplementoDos(numD, 5);
        System.out.println("d) -14 en complemento a dos con 5 bits: " + representacionD);
    }

 public static String obtenerRepresentacionComplementoDos(int num, int bits) {
        int maxValor = (int) Math.pow(2, bits - 1) - 1;
        int minValor = -(int) Math.pow(2, bits - 1);
        if (num >= minValor && num <= maxValor) {
            if (num >= 0) {
                String binarioPositivo = Integer.toBinaryString(num);
                while (binarioPositivo.length() < bits) {
                    binarioPositivo = "0" + binarioPositivo;
                }
                return binarioPositivo;
            } else {
                String binarioNegativo = Integer.toBinaryString(num & ((1 << bits) - 1));
                while (binarioNegativo.length() < bits) {
                    binarioNegativo = "1" + binarioNegativo;
                }
                return binarioNegativo;
            }
        } else {
            return "Desbordamiento";
        }
        }
    

    public static String obtenerRepresentacionComplementoUno(int num, int bits) {
        if (num >= -(Math.pow(2, bits-1)) && num <= (Math.pow(2, bits-1))-1) {
            if (num >= 0) {
                String binarioPositivo = Integer.toBinaryString(num);
                while (binarioPositivo.length() < bits) {
                    binarioPositivo = "0" + binarioPositivo;
                }
                return binarioPositivo;
            } else {
                return "Desbordamiento";
            }
        } else {
            return "Desbordamiento";
        }
    }





    public static String obtenerRepresentacionSignoMagnitud(int num, int bits) {
        int maxValor = (int) Math.pow(2, bits - 1) - 1;
        int minValor = -(int) Math.pow(2, bits - 1) + 1;
        if (num >= minValor && num <= maxValor) {
            if (num >= 0) {
                String binarioPositivo = Integer.toBinaryString(num);
                while (binarioPositivo.length() < bits) {
                    binarioPositivo = "0" + binarioPositivo;
                }
                return binarioPositivo;
            } else {
                String binarioNegativo = Integer.toBinaryString(Math.abs(num));
                while (binarioNegativo.length() < bits) {
                    binarioNegativo = "0" + binarioNegativo;
                }
                return "1" + binarioNegativo;
            }
        } else {
            return "Desbordamiento";
        }
    }
    
}
