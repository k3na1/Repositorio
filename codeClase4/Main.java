import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        
        Gimnasio gimnasio = new Gimnasio();
        Scanner scanner = new Scanner(System.in);

        int opc = 0;

        do{
            System.out.println("Menú de opciones");
            System.out.println("1) Inscribir alumno");
            System.out.println("2) Mostrar alumnos");
            System.out.println("3) Actualizar datos alumno");  
            System.out.println("4) Eliminar alumno");
            System.out.println("5) Salir");
            opc = scanner.nextInt();
            scanner.nextLine();

            switch (opc) {
                case 1:
                    gimnasio.anadirAlumno();
                    break;
                case 2:
                    gimnasio.leerAlumno();
                    break;
                case 3:
                    gimnasio.actualizarAlumno();
                    break;
                case 4:
                    gimnasio.eliminarAlumno();
                    break;
                case 5:
                    System.out.println("Saliendo del sistema...");
                    return;
                default:
                    System.out.println("Ingrese una opción válida");
                    break;
            }


        }while(opc != 5);




    }
}