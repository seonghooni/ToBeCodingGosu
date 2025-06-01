import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String[] lines = br.readLine().split(" ");

            String command = lines[0];
            Integer number = Integer.parseInt(lines[1]);

            if(command.equals("find")){
                System.out.println(set.contains(number));
            }else if(command.equals("add")) {
                set.add(number);
            }else{
                set.remove(number);
            }
        }

        
    }
}