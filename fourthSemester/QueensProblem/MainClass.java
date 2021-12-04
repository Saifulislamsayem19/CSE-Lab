package fourthSemester.QueensProblem;

import java.util.Scanner;

public class MainClass {

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);

        System.out.println("How many Queens?");
        int n = s.nextInt();

        Queens Q = new Queens(n);
        Q.callplaceNqueens();

    }
}
