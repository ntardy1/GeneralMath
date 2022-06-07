// A Script to factor An Integer
// and print a list of its factors
import java.util.ArrayList;
import java.util.Scanner;
public class Factorer {
    public static void main(String []args){
        System.out.print("Input Number: ");
        Scanner scan = new Scanner(System.in);
        int number = scan.nextInt();
        scan.close();
        ArrayList<Integer> factors = new ArrayList<Integer>();
        for (int i = 1; i <= number; i++){
            if (number % i == 0){
                factors.add(i);
            }
        }
        System.out.println("Factors: " + factors);
    }
}