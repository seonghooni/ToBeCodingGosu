import java.util.*;

class Pair {
    int x;
    int y;
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {

    static int n, k, u, d;
    static int[][] grid;
    static List<Pair> nodes = new LinkedList<>(); // 좌표를 저장하는 곳 [Pair[1,1], Pair[1,2], Pair[1,3], Pair[2,1], ...]
    static List<Pair[]> combi = new LinkedList<>(); // 조합을 저장 [[Pair, Pair], [Pair, Pair], ...]
    static Pair[] selected;
    static boolean[][] visited;
    static int ans = 0;


    public static boolean inRange(int x, int y) {
        return 1 <= x && x <= n && 1 <= y && y <= n;
    }

    public static int bfs(int x, int y) {
        if(visited[x][y])
            return 0;

        int[] dx = new int[]{1, -1, 0, 0};
        int[] dy = new int[]{0, 0, 1, -1};

        int count = 1;
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(x, y));
        visited[x][y] = true;

        while(!queue.isEmpty()) {
            Pair pair = queue.poll();
            x = pair.x; y = pair.y;
            // System.out.print("(" + x + "," + y + ") ");
            int nx, ny;
            for(int i=0; i<4; i++) {
                nx = x + dx[i];
                ny = y + dy[i];

                if(!inRange(nx, ny) || visited[nx][ny])
                    continue;
                
                int differ = Math.abs(grid[nx][ny] - grid[x][y]);
                if(differ >= u && differ <= d){
                    // System.out.println("->"+" (" + nx + "," + ny + ")");
                    queue.offer(new Pair(nx, ny));
                    visited[nx][ny] = true;
                    count += 1;
                }
            }
        }
        // System.out.println();
        return count;
    }

    // 각각의 조합에 대해서 계산
    public static void calc() {

        for(int k=0; k<combi.size(); k++) {

            for(int i=1; i<=n; i++) {
                for(int j=1; j<=n; j++) {
                    visited[i][j] = false;
                }
            }

            int val = 0;
            Pair[] pairs = combi.get(k);

            // System.out.print(k + "번째 ");
            for(int t = 0; t < pairs.length; t++) {
                // System.out.print("(" + pairs[t].x + ", " + pairs[t].y + ") ");
            }
            // System.out.println();

            for(int j=0; j<pairs.length; j++) {
                val += bfs(pairs[j].x, pairs[j].y);
            }
            ans = Math.max(val, ans);
            // System.out.println("= " + ans);
        }
    }

    public static void makeCombi(int idx, int cnt) {
        if(cnt == k){
            combi.add(selected.clone());
            return;
        }
        
        if(idx == nodes.size())
            return;

        selected[cnt] = nodes.get(idx);
        makeCombi(idx+1, cnt+1);
        makeCombi(idx+1, cnt);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        n = sc.nextInt(); k = sc.nextInt(); u = sc.nextInt(); d = sc.nextInt();
        selected = new Pair[k];

        grid = new int[n+1][n+1];
        visited = new boolean[n+1][n+1];

        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                grid[i][j] = sc.nextInt();
                nodes.add(new Pair(i, j));
            }
        }

        makeCombi(0,0);
        calc();

        System.out.println(ans);

        // for(int i=0; i<combi.size(); i++) {
        //     Pair[] com = combi.get(i);
        //     for(Pair pair: com){
        //         System.out.print(pair.x + ", " + pair.y + " /");
        //     }

        //     System.out.println();
        // }
    
    }
}