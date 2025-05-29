import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] arr = new int[N+1];
        for (int i = 1; i <= N; i++) {
            arr[i] = sc.nextInt();
        }


        int[][] dp = new int[N+1][K+1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= K; j++) {
                dp[i][j] = -1;
            }
        }

        dp[0][0] = 0;
        for(int i = 1; i <= N; i++) {
            if(arr[i]>0) dp[i][0] = arr[i];
            else dp[i][1] = arr[i];
        }

        // Please write your code here.
        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= K; j++) {
                
                if(arr[i] > 0 && dp[i-1][j] != -1) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j] + arr[i]);
                }

                if(arr[i] < 0 && j > 0 && dp[i-1][j-1] != -1) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1] + arr[i]);
                }
            }
        }

        // for(int[] row: dp){
        //     System.out.println(Arrays.toString(row));
        // }

        int result = 0;

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= K; j++) {
                result = Math.max(dp[i][j], result);
            }
        }
        // for (int i=1; i<=K; i++) {
        //     result = Math.max(dp[N][i], result);
        // }

        System.out.println(result);
    }
}