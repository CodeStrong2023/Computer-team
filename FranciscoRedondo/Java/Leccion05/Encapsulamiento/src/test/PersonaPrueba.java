
package test;

import Dominio.*;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Francisco", 57000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        
   //Modificar a traves de los metodos
   
   persona1.setNombre("Juan Ignacio");
   //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar        
   //System.out.println("Nombre es: "+persona1.nombre);//Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo es: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el boolean: "+persona1.isEliminado());
    //Tarea: crear otro objeto de tipo Persona, asignas valores de manera inicial e imprimir, luego modificar sus valores y volver a imprimir
        System.out.println("persona1 = " + persona1);
    }
}

