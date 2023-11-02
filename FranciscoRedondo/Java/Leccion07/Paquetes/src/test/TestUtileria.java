
package test;

//import ar.com.codesystem.Utileria;//Esta es la que se recomienda
//import ar.com.codesystem.Utileria;
//import static ar.com.codesystem.Utileria.imprimir; //Solo aplica para metodos estaticos

public class TestUtileria {
    public static void main(String[] args) {
        //Utileria.imprimir("Saludos a todos los alumnos de la tecnicatura");//Se recomienda esta importacion
        //imprimir("Terminamos en unos minutos");
        ar.com.codesystem.Utileria.imprimir("Ahora si estamos terminando");//No es recomendable hacerlo de esta forma, se recomienda hacer una importacion normal.
        
    }
}
