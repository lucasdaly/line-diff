import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class program {
    public static void main(){
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a file to scan");
        String file = scanner.nextLine();
        
        File newFile = new File("test folder/" + file + " New.java");
        File oldFile = new File("test folder/" + file + " Old.java");


        try (Scanner myReader = new Scanner(newFile)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data);
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
