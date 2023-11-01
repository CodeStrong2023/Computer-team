/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se aplique:
-variables: evita el cambio de valor que almacena la variable
-metodos: evita que se modifique la definicion o comportamiento de un metodo desde una subclase (hija)
-clases evita que se creen clases hijas
Otra caracteristica es que normalmente, cuando trabajamos con variables se combina con el modificador de acceso estatico
para convertir una variable en una constante, es decir que no se puede modificar su valor, el ejemplo de esto es la clase Math
en la cual todos sus atributos son de tipo static y final, es por esto que la variable pi* se conoce como una constante.
*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 41991755;
        System.out.println("miDni = " + miDni);
        //miDni = 41991757; No se puede modificar
        //Persona.CONSTANTE_AQUI = 9; //No se modifica;
        System.out.println("Mi atributo constante es:  = " +Persona.CONSTANTE_AQUI );
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); No se puede asignar una nueva referencia por que es final
        persona1.setNombre("Francisco Redondo");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        persona1.setNombre("Lucas Sarmiento");
        System.out.println("persona1 nombre = " + persona1.getNombre());
    }
}
