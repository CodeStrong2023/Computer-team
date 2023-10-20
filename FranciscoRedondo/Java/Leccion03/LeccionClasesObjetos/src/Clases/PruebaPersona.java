
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Francisco"; //El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Redondo";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = "+persona2);
        System.out.println("persona1 = " + persona1);
        persona2.nombre = "Manuel";
        persona2.apellido = "Dominguez";
        persona2.obtenerInformacion();
    }
    
}
