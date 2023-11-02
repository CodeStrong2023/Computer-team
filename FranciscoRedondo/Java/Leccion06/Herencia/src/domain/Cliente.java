
package domain;

import java.util.Date;

public class Cliente extends Persona {
    //Atributos
    private int idClientes;
    private Date fechaRegistro; //Importar clase date
    private boolean vip; //Very important persona
    private static int contadorCliente; //Tipo estatico
    
    //Constructor
    public Cliente(Date fechaRegistro, boolean vip, String nombre,
                  char genero, int edad, String direccion){
        super(nombre, genero, edad, direccion);
        this.idClientes = ++Cliente.contadorCliente;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }


    public int getIdClientes() {
        return this.idClientes;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append("idClientes=").append(idClientes);
        sb.append(", fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", =").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
}
