import java.util.ArrayList;
import java.util.Scanner;

public class Gimnasio {
 
    // Lista de alumnos
    private ArrayList<Alumno> listaAlumnos;
    //  Scanner
    private Scanner scanner;

    // Constructor
    public Gimnasio(){
        listaAlumnos = new ArrayList<>();
        scanner = new Scanner(System.in);
    }

    public void anadirAlumno(){ // C Añadir Alumnos
        int bucle = 1;
        do{
            System.out.println("Ingresa los datos del alumno\nID alumno:");
            int id = scanner.nextInt(); 
            scanner.nextLine(); // Eliminar espacio en blanco de línea 21
            if (id >= 1){ // Consultamos si el número es mayor o igual a 1
                bucle = 0;
                System.out.println("Nombre alumno:");
                String nombre = scanner.nextLine();
                System.out.println("Membresía alumno:");
                String membresia = scanner.nextLine();
                System.out.println("Edad alumno:");
                int edad = scanner.nextInt();
                scanner.nextLine(); // Eliminar espacio en blanco de línea 25
        
                Alumno alumno = new Alumno(id, nombre, membresia, edad);
                listaAlumnos.add(alumno);
            }else{
                System.out.println("ID no puede ser un número negativo o 0");
            }
        }while (bucle==1);
    }

    public void leerAlumno(){ // R Mostrar Alumnos
        //Validar si la lista está vacía
        if (listaAlumnos.isEmpty()){
            System.out.println("No hay alumnos inscritos");
        }else{
            for (Alumno alumno : listaAlumnos){
                System.out.println(alumno);
            }
        }
    }

    public void actualizarAlumno(){ // U Actualizar alumno
        System.out.println("Ingrese la ID del alumno");
        int id = scanner.nextInt();
        scanner.nextLine();

        for (Alumno alumno : listaAlumnos){
            if (alumno.getId()==id){
                System.out.println("Ingrese nuevo nombre");
                String nuevoNombre = scanner.nextLine();
                System.out.println("Ingrese nueva edad");
                int nuevaEdad = scanner.nextInt();
                scanner.nextLine();
                System.out.println("Ingrese nuevo tipo de membresía");
                String nuevaMembresia = scanner.nextLine();

                // Actualizo datos
                alumno.setNombre(nuevoNombre);
                alumno.setEdad(nuevaEdad);
                alumno.setMembresia(nuevaMembresia);

                System.out.println("Datos actualizados");
                return;
            }
        }
    }

    public void eliminarAlumno(){ // D Borrar alumno
        System.out.println("Ingrese ID a eliminar");
        int idEliminar = scanner.nextInt();
        scanner.nextLine();
        // Variable almacenar producto a eliminar
        Alumno idPorEliminar = null;
        // Iterar
        for(Alumno alumno : listaAlumnos){
            if (alumno.getId() == idEliminar){
                idPorEliminar = alumno;
                break;
            }
        }

        if(idPorEliminar != null){
            listaAlumnos.remove(idPorEliminar);
            System.out.println("Alumno borrado del sistema");
        }else{
            System.out.println("Alumno no encontrado en el sistema");
        }
            

    }

}
