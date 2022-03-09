package FourthSemester.MatrixChainMultiplication;

public class Matrix {

    public final int INT_MAX = 100000;

    public int matOrder(int[] array, int n) {

        int [][]minMul = new int [n][n];

        for(int i=1; i<n; i++){
            minMul[i][i] = 0;
        }

        for(int l=2; l<n; l++){
            for(int i=1; i<n-l+1; i++){
                int j = i+l-1;
                minMul[i][j] = INT_MAX;
                for(int k=i; k <= j-1; k++ ){

                    int q = minMul[i][k] + minMul[k+1][j] + array[i- 1]*array[k]*array[j];
                    if (q < minMul[i][j]) {
                        minMul[i][j] = q;
                    }
                }
            }
        }

        return minMul[1][n-1];
    }
}
