/*
PROYECTO DE CAJERO AUTOMATICO DEL GRUPO COMPUTER TEAM
INTEGRANTES:
    - REDONDO FRANCISCO.
    - SARMIENTO LUCAS.
*/

package ProyectoFinalCajero;

import java.util.Scanner;

public class CajeroAutomatico {
    public static void main(String[] args) {
        int balance = 100000, retirar, deposito ;
        Scanner sc = new Scanner(System.in);
        //Se crea la clase Scanner para que el usuario pueda elegir una opcion
        while(true){
            System.out.println("Cajero Automatico de Computer Team");
            System.out.println("1 - Retirar dinero");
            System.out.println("2 - Depositar dinero");
            System.out.println("3 - Chequeo de balance");
            System.out.println("4 - Salir del cajero");
            System.out.println("Elige la operacion que deseas realizar");
            
            int choice = sc.nextInt();
            switch(choice){
                case 1:
            System.out.println("Ingrese el monto a retirar : ");
            // Obtener el retiro de dinero del usuario
            retirar = sc.nextInt();
                if(balance >= retirar ){
                    balance = balance - retirar;
                    System.out.println("Por favor, retire su dinero");
                }
                
                else {
                        System.out.println("Dinero insuficiente");
                        System.out.println("");
                        break;
                        
                    case 2:
                        System.out.println("Ingrese el dinero a depositar");
                        deposito = sc.nextInt();
                        balance = balance + deposito;
                        
                        System.out.println("El dinero ha sido depositado con exito");
                        System.out.println("");
                        break;
                        
                    case 3:
                        System.out.println("Dinero disponible :" +balance);
             
                }
            }
        }
    }
}
