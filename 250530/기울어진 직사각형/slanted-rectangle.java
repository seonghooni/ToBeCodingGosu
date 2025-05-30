import java.util.Scanner;

public class Main {

    static final int MAX_N = 20;
    static int n;
    static int[][] grid = new int [MAX_N+1][MAX_N+1];

    public static boolean inRange(int x, int y) {
        return 1 <= x && x <= n && 1 <= y && y <= n;
    }

    public static int getScore(int x, int y, int k, int l) {
        int[] dx = new int[]{-1, -1, 1, 1};
        int[] dy = new int[]{1, -1, -1, 1};
        int[] depth = new int[]{k,l,k,l};

        int sum = 0;
        // 방향
        for(int d=0; d<4; d++){
            // 길이만큼 처리
            for(int s=0; s<depth[d]; s++) {
                x += dx[d]; y += dy[d];

                if(!inRange(x, y))
                    return 0;

                sum += grid[x][y];
            }
        }

        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for(int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++){
                grid[i][j] = sc.nextInt();
            }
        }

        int max_length = n / 2;
        int ans = 0;

        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                for(int k=1; k<=n-1; k++) {
                    for(int l=1; l<=n-1; l++) {
                        ans = Math.max(ans, getScore(i,j,k,l));
                    }
                }
            }
        }        

        System.out.println(ans);
    }
}
