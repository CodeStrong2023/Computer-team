/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
y mostrar cuantos numeros se han introducido.
Lohacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
*/
package Ciclos04;
import javax.swing.JOptionPane;

public class EjercicioCiclos04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero: "+numero+" es POSITIVO");
            conteo++;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "Ha ingresado "+conteo+" numeros que no son negativo");
    }
}
