import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class program {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a file to scan");
        String file = scanner.nextLine();
        
        File newFile = new File("test folder/" + file + " New.java");
        File oldFile = new File("test folder/" + file + " Old.java");


        try (Scanner myReader = new Scanner(newFile)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String normalized = data.replaceFirst("\\s+", "");
                System.out.println(normalized);
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        try (Scanner myReader = new Scanner(oldFile)){
            while (myReader.hasNextLine()){
                String data = myReader.nextLine();
                String normalized = data.replaceFirst("\\s+", "");
                System.out.println(normalized);
            }
        }catch (FileNotFoundException e){
            System.out.println("error");
            e.printStackTrace();
        }
    }
}
