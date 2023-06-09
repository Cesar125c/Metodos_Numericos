/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author usuario
 */
import java.math.BigDecimal;
import java.util.Scanner;
public class Main {

    public static final Scanner leer = new Scanner(System.in);
    public static void main(String[] args) {

        double value;
        System.out.println("Ingrese un valor para x, mayor que 250");

        value = valorX.ingresarValor();

        BigDecimal result = calcularExpresion.regresar(value);

        System.out.println("El resultado es: " + result);




    }
}