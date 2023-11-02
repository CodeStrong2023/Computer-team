/*
PROYECTO DE CAJERO AUTOMATICO DEL GRUPO COMPUTER TEAM
INTEGRANTES:
    - REDONDO FRANCISCO.
    - SARMIENTO LUCAS.
*/

package ProyectoJavaSegundoSemestre;

import java.util.Scanner;

public class ProyectoCajeroAutomatico {
    public static void main(String[] args) {
        System.out.println("-----------------------------------------------------");
        System.out.println("| Bienvenidos al Cajero Automatico de Computer Team |"); //Impresion mensaje de Bienvenida. 
        System.out.println("-----------------------------------------------------");
        Scanner leer = new Scanner(System.in); //Lectura mediante clase Scanner para ingresar datos por teclado
        System.out.println("-------------------------------------------");
        System.out.println("|Ingresa tu tarjeta para comenzar a operar|");
        System.out.println("-------------------------------------------");
        String tarjeta = leer.next(); 
        System.out.println("-------------------------------------------");
        System.out.println("|Ingresa tu clave para acceder a la cuenta|");
        System.out.println("-------------------------------------------");
        String clave = leer.next();
        if (clave.equals("12345")){ //Se usa variable equals y no una variable == ya que esta ultima es para datos primitivos. 
            
            double saldo = 100000; //Se utiliza variable double por si el saldo inicial se quiere hacer con numeros con coma. 
            String opcion = "0";
            
            while (!opcion.equals("4")){
                System.out.println("----------------------------------");
                System.out.println("| CAJERO AUTOMATICO COMPUTER TEAM |");
                System.out.println("| 1. Consultar saldo              |");
                System.out.println("| 2. Realizar deposito            |"); //Impresion del tablero de operaciones
                System.out.println("| 3. Retirar efectivo             |");
                System.out.println("| 4. Salir del cajero             |");
                System.out.println("----------------------------------");
                opcion = leer.next();
               