/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @integrantes Kevin Chicaiza, Alex Muzo, Emily Guerron, Cesar Cueva, Carlos Robayo
 * Metodos Numericos
 * Paralelo 002
 * Fecha: 09/06/2023
 */
public class valorX {
    public static double ingresarValor() {

        double aux;

        do{
            aux = Main.leer.nextDouble();
        }while(aux<250);

        return aux;
    }
    
}
