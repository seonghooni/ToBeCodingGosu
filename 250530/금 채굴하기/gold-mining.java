import java.util.Scanner;

public class Main {

    static int n;
    static int[][] dx = new int[3][];
    static int[][] dy = new int[3][];

    static {
        dx[0] = new int[] {0};
        dx[1] = new int[] {0, 0, 0, 1, -1};
        dx[2] = new int[] {0, 0, 0, 0, 0, 1, 1, 1, 2, -1, -1, -1, -2};
        dy[0] = new int[] {0};
        dy[1] = new int[] {0, 1, -1, 0, 0};
        dy[2] = new int[] {0, 1, 2, -1, -2, 0, 1, -1, 0, 0, 1, -1, 0};
    }

    public static boolean in_range(int x, int y){
        return 1 <= x && x <= n && 1 <= y && y <= n;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n+1][n+1];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.

        int max_count = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                for(int level=0; level<3; level++){
                    int cost = 0;
                    int value = 0;
                    int count = 0;
                    int length = dx[level].length;
                    for(int k=0; k<length; k++) {
                        int nx = i + dx[level][k];
                        int ny = j + dy[level][k];

                        if(in_range(nx,ny)){
                            cost += 1;
                            if(grid[nx][ny] == 1) {
                                value += m;
                                count += 1;
                            }
                        }
                    }
                    if(value-cost >= 0) max_count = Math.max(max_count, count);
                }
            }
        }

        System.out.println(max_count);
    }

}