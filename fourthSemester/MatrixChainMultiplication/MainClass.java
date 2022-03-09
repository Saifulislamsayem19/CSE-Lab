package FourthSemester.MatrixChainMultiplication;

import java.util.Scanner;

public class MainClass {
    public static void main(String... arg)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter number of Matrix: ");
        int n = s.nextInt();
        int []arr = new int[n+1];
        System.out.println("Enter the Matrix order: ");
        for(int i = 0; i<n+1; i++){
            arr[i] = s.nextInt();
        }

        System.out.println("Minimum matrix multiplications: "  + new Matrix().matOrder(arr, n+1));
    }
}
