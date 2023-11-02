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
                 switch (opcion) { //Mediante esta variable switch se verifica la opcion elegida. 
                    case "1": {
                        System.out.println("El saldo de la tarjeta es = " + Double.toString(saldo)); //Se utiliza un double.tostring ya que se espera valor en cadena. 
                        break;    
                    }  
                    case "2": {
                        System.out.println("Depositar efectivo");
                        System.out.println("Ingrese el monto a depositar");
                        double deposito = leer.nextDouble(); //Se guardan los valores ingresados en la variable deposito y se utiliza un double por si se quiere ingresar valor decimal.
                        if (deposito>0) {
                            saldo = saldo + deposito;
                            System.out.print("Deposito realizado correctamente");
                            System.out.println(" ");
                            
                        }
                        else {
                            System.out.println("Error.Monto incorrecto"); //Si el valor del deposito es cero o menor que cero imprimira error. 
                        }
                        
                        break;
                    }         
                    case "3" : {
                        System.out.println("Retirar efectivo "); 
                        double montoRetirar; //El dato se guarda dentro de monto retirar, si el retiro es menor que el saldo, si se puede retirar.
                        montoRetirar = leer.nextDouble();
                        if (montoRetirar <= saldo) {
                            saldo = saldo - montoRetirar;
                            System.out.print("Retire su dinero");
                            System.out.println(" ");
                            
                        }
                        else {
                            System.out.println("No se puede retirar un monto mayor"); //Si el saldo a retirar es mayor que el disponible, imprime error.
                        }
                        break;
                    }
                    
                    case "4": {
                        System.out.println("Gracias por utilizar el cajero automatico de Computer Team");
                        break;
                    }
                    default: {
                        System.out.println("Opcion incorrecta"); //Si la opcion no se encuentra dentro del tablero de operaciones imprime error. 
                        break;
                    }
                }                             
            }                                               
        } else {
            System.out.println("Clave incorrecta"); //Se imprime error si la clave no es la que se asigno. 
        }                
    }
}
