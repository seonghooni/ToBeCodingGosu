import java.util.*;

public class Main {

    static final int MAX_N = 100;

    static int[][] grid = new int[MAX_N][MAX_N];
    static boolean[][] visited = new boolean[MAX_N][MAX_N];

    static int n;
    static int k;

    public static boolean inRange(int x, int y) {
        return 1 <= x && x <= n && 1 <= y && y <= n;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        k = sc.nextInt();

        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                grid[i][j] = sc.nextInt();
                visited[i][j] = false;
            }
        }

        Queue<int[]> queue = new LinkedList<>();

        int count = 0;

        for(int i=0; i<k; i++) {
            int row = sc.nextInt();
            int col = sc.nextInt();

            queue.offer(new int[]{row, col});
            visited[row][col] = true;
            count += 1;
        }

        int[] dx = new int[]{1, -1, 0, 0};
        int[] dy = new int[]{0, 0, 1, -1};

        while(!queue.isEmpty()) {
            int[] s = queue.poll();
            int x = s[0];
            int y = s[1];

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(!inRange(nx,ny)) continue;

                if(!visited[nx][ny] && grid[nx][ny] == 0) {
                    queue.offer(new int[]{nx, ny});
                    visited[nx][ny] = true;
                    count += 1;
                }
            }
        }

        System.out.println(count);
    }
}