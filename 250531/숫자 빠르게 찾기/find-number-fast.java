import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            // Please write your code here.
            int left = 0;
            int right = n-1;

            int mid = (left + right) / 2;
            while(left <= right) {
                mid = (left + right) / 2;
                if(arr[mid] == x){
                    System.out.println(mid+1);
                    break;
                }

                if(arr[mid] > x)
                    right = mid -1;
                else if(arr[mid] < x)
                    left = mid + 1;

            }

            if(arr[mid] != x)
                System.out.println(-1);
        }
    }
}