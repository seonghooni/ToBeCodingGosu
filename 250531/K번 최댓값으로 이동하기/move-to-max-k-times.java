import java.util.*;
public class Main {
    
    static final int MAX_N = 100;
    static int n, k;
    static int[][] grid = new int[MAX_N+1][MAX_N+1];
    static boolean[][] visited = new boolean[MAX_N+1][MAX_N+1];
    static int finalX, finalY; // 최종 x,y
    static int[] dx = new int[]{1,-1,0,0};
    static int[] dy = new int[]{0,0,1,-1};

    public static boolean inRange(int x, int y){
        return 1 <= x && x <= n && 1 <= y && y <= n;
    }

    public static void init() {
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                visited[i][j] = false;
            }
        }
    }

    public static void calc() {
        Queue<int[]> queue = new LinkedList<>();

        int max_val = 0;
        int num = grid[finalX][finalY];
        visited[finalX][finalY] = true;
        queue.offer(new int[]{finalX, finalY});

        int x; int y;
        int nx; int ny;

        while(!queue.isEmpty()){
            int[] arr = queue.poll();
            x = arr[0]; y = arr[1];
            // System.out.println(x + ", " + y + " 처리 / max_val = " + max_val);
            
            for(int i=0; i<4; i++) {
                nx = x + dx[i];
                ny = y + dy[i];

                if(!inRange(nx, ny))
                    continue;
                
                if(grid[nx][ny] < num && !visited[nx][ny]){
                    queue.offer(new int[]{nx, ny});
                    visited[nx][ny] = true;

                    if(grid[nx][ny] > max_val) {
                        max_val = grid[nx][ny];
                        finalX = nx;
                        finalY = ny;
                    }else if(grid[nx][ny] == max_val) {
                        if(finalX > nx) {
                            finalX = nx;
                            finalY = ny;
                        }else if(finalX == nx) finalY = Math.min(ny, finalY);
                    }
                }

            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }

        finalX = sc.nextInt();
        finalY = sc.nextInt();

        for(int i=0; i<k; i++) {
            int beforeX = finalX;
            int beforeY = finalY;
            calc();

            if(finalX ==beforeX && finalY == beforeY)
                break;
            init();
        }

        System.out.println(finalX + " " + finalY);
    }
}