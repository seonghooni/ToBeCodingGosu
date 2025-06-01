import java.util.*;
import java.io.*;

public class Main {

    static Set<Integer> a = new HashSet<>();
    static Set<Integer> b = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] line = br.readLine().split(" ");
        for(int j=0; j<n; j++) {
            a.add(Integer.parseInt(line[j]));
        }

        n = Integer.parseInt(br.readLine());
        line = br.readLine().split(" ");
        for(int j=0; j<n; j++) {
            if(a.contains(Integer.parseInt(line[j])))
                System.out.print("1 ");
            else
                System.out.print("0 ");
        }
    }
}