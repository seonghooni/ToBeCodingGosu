import java.util.Scanner;

public class Main {

    static int n, m;
    static int[][] grid;

    public static int getArea(int k) {
        return k * k + (k+1) * (k+1); 
    }
    
    // 주어진 k에 대하여 채굴 가능한 금의 개수를 반환합니다.
    public static int getNumOfGold(int row, int col, int k) {
        int numOfGold = 0;
    
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++)
                if(Math.abs(row - i) + Math.abs(col - j) <= k)
                    numOfGold += grid[i][j];
    
        return numOfGold;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int m = sc.nextInt();
        grid = new int[n+1][n+1];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.

        int max_count = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                for(int level=2*(n-1); level>=0; level--){
                    int golds = getNumOfGold(i, j, level);

                    if(golds * m >= getArea(level)){
                        max_count = Math.max(max_count, golds);
                        break;
                    }
                }
            }
        }

        System.out.println(max_count);
    }

}