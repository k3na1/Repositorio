public class Alumno {

    private String nombre, membresia;
    private int id, edad;
    
    public Alumno(int id, String nombre, String membresia, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.membresia = membresia;
        this.edad = edad;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getMembresia() {
        return membresia;
    }

    public void setMembresia(String membresia) {
        this.membresia = membresia;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    @Override
    public String toString() {
        return "Alumno [id=" + id + ", nombre=" + nombre + ", membresia=" + membresia + ", edad=" + edad + "]";
    }

    

}