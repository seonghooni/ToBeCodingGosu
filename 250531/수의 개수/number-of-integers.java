import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        Map<Integer, Integer> map = new HashMap<>();


        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            arr[i] = a;

            int count;
            if(map.containsKey(a)){
                count = map.get(a)+1;
            }else
                count = 1;
            map.put(a, count);
        }
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            // Please write your code here.

            int left = 0;
            int right = n-1;

            boolean result = false;
            while(left <= right) {
                int mid = (left + right) / 2;

                if(arr[mid] == x){
                    result = true;
                    break;
                }

                if(arr[mid] > x)
                    right = mid -1;
                else
                    left = mid + 1;
            }   

            if(result)
                System.out.println(map.get(x));
            else
                System.out.println(0);


        }
    }
}