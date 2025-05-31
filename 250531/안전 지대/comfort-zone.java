import java.util.*;
public class Main {

    static int max_town = 0;
    static int max_k = 0;
    static int[] dx = new int[]{1, -1, 0, 0};
    static int[] dy = new int[]{0, 0, 1, -1};
    static int n, m;


    public static boolean inRange(int x, int y) {
        return 1 <= x && x <= n && 1 <= y && y <= m;
    }


    public static int dfs(int x, int y, int k, int[][] grid, boolean[][] visited) {
        if(visited[x][y] || grid[x][y] <= k)
            return 0;
        
        int count = 1;
        visited[x][y] = true;

        int nx, ny;
        for(int i=0; i<4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if(!inRange(nx, ny))
                continue;

            if(visited[nx][ny] || grid[nx][ny] <= k)
                continue;
            
            count += dfs(nx, ny, k, grid, visited);
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        int[][] grid = new int[n+1][m+1];
        boolean[][] visited = new boolean[n+1][m+1];
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= m; j++)
                grid[i][j] = sc.nextInt();
        
        // Please write your code here.
        for(int k = 1; ; k++) {

            for(int i = 1; i <= n; i++){
                for(int j = 1; j <= m; j++) {
                    visited[i][j] = false;
                }
            }

            int town = 0;
            for(int i = 1; i <= n; i++) {
                for(int j = 1; j <= m; j++) {
                    int c = dfs(i,j,k,grid,visited);
                    if(c==0)
                        continue;
                    town += 1;   
                }
            }
            if(town > max_town) {
                max_town = town;
                max_k = k;
            }
            if(town==0)
                break;
        }
        
        System.out.println(max_k + " " + max_town);
    }
}