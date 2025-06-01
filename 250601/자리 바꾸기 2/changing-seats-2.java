import java.util.*;
import java.io.*;

public class Main {

    static Set<Integer>[] sets;
    static Integer[] arr;
    static Integer[][] orders;

    public static void swap(int idx1, int idx2) {
        int a = arr[idx1];
        int b = arr[idx2];

        sets[a].add(idx2);
        sets[b].add(idx1);

        arr[idx1] = b;
        arr[idx2] = a;
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int k = Integer.parseInt(line[1]);

        sets = new HashSet[n+1];
        arr = new Integer[n+1];
        orders = new Integer[k][2];

        for(int i=1; i<=n; i++) {
            sets[i] = new HashSet<>();
        }

        for(int i=1; i<=n; i++){
            arr[i] = i;
            sets[i].add(i);
        }

        for(int i=0; i<k; i++) {
            line = br.readLine().split(" ");
            int a = Integer.parseInt(line[0]);
            int b = Integer.parseInt(line[1]);

            orders[i] = new Integer[]{a, b};
        }

        for(int i=0; i<3*k; i++) {
            int kk = i % k;
            swap(orders[kk][0], orders[kk][1]);
            // System.out.println(orders[kk][0] + " <-> " + orders[kk][1]);
        }

        for(int i=1; i<=n; i++) {
            System.out.println(sets[i].size());
        }
    }
}