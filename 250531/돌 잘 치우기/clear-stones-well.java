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

    static final int MAX_N = 100;
    static int n, m, k;
    static int[][] grid = new int[MAX_N+1][MAX_N+1];
    static Pair[] pairs;
    static List<Pair> stones = new ArrayList<>();
    static int stoneCount = 0;
    static List<int[]> combinations = new ArrayList<>(); // 조합 경우의 수를 저장 = kCm 만큼
    static boolean[][] visited = new boolean[MAX_N+1][MAX_N+1];
    static int ans;
    static int[] dx = new int[]{0, 0, 1, -1};
    static int[] dy = new int[]{1, -1, 0, 0};

    public static void findCombi(int idx, int size, int[] selected) {
        if (size == m) {
            combinations.add(selected.clone());
            return;
        }

        if (idx == stoneCount)
            return;

        for(int i=idx; i<stoneCount; i++){
            selected[size] = i;
            findCombi(i+1, size+1, selected);
        }
    }

    // combi의 index를 받아, 계산하는 함수 (visited 초기화)
    public static void calc(int idx) {
        // visited 초기화
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                visited[i][j] = false;
            }
        }

        int[] positions = combinations.get(idx);

        for(int i=0; i<positions.length; i++){
            Pair stone = stones.get(positions[i]);

            int x = stone.x;
            int y = stone.y;

            grid[x][y] = 0;
        }

        int count = 0;
        for(int i=0; i<pairs.length; i++) {
            Pair pair = pairs[i];
            count += bfs(pair.x, pair.y, visited);
        }

        ans = Math.max(ans, count);

        // 원상복구
        for(int i=0; i<positions.length; i++){
            Pair stone = stones.get(positions[i]);

            int x = stone.x;
            int y = stone.y;

            grid[x][y] = 1;
        }
    }

    public static boolean inRange(int x, int y) {
        return 1<=x && x<=n && 1<=y && y<=n;
    }

    public static int bfs(int x, int y, boolean[][] visited) {
        if(visited[x][y])
            return 0;

        Queue<int[]> queue = new LinkedList<>();

        queue.offer(new int[]{x, y});
        visited[x][y] = true;
        int count = 1;

        while(!queue.isEmpty()) {
            int[] node = queue.poll();
            x = node[0]; y = node[1];
            int nx, ny;

            for(int i=0; i<4; i++) {
                nx = x + dx[i];
                ny = y + dy[i];

                if(!inRange(nx,ny))
                    continue;
                
                if(!visited[nx][ny] && grid[nx][ny] == 0) {
                    queue.offer(new int[]{nx, ny});
                    visited[nx][ny] = true;
                    count += 1;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        k = sc.nextInt();
        m = sc.nextInt();

        pairs = new Pair[k];

        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                grid[i][j] = sc.nextInt();

                if(grid[i][j] == 1) {
                    stones.add(new Pair(i,j));
                    stoneCount++;
                }
            }
        }

        for(int i=0; i<k; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            Pair pair = new Pair(x, y);
            pairs[i] = pair;
        }

        findCombi(0, 0, new int[m]);


        for(int i=0; i<combinations.size(); i++) {
            calc(i);
        }

        System.out.println(ans);
    }
}