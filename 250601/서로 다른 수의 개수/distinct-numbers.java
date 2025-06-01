import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] line = br.readLine().split(" ");


        Set<Integer> set = new HashSet<>();
        for(int i=0; i<n; i++) {
            int num = Integer.parseInt(line[i]);
            set.add(num);
        }

        System.out.println(set.size());
    }
}