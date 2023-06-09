/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
import java.math.BigDecimal;
import java.math.RoundingMode;

public class calcularExpresion {

    public static BigDecimal regresar(double value) {
        BigDecimal result;
        if(value > 700) {
            return BigDecimal.ONE; //Para valores mayores a 700 se regresa directamente 1
        } else {

            BigDecimal expValue = BigDecimal.valueOf(Math.exp(value));

            BigDecimal expMenos1 = expValue.subtract(BigDecimal.ONE);



            result = expValue.divide(expMenos1, 20, RoundingMode.UP);


        }
        return result;
    }
}