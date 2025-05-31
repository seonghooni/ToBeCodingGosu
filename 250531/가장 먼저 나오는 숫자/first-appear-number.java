import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < m; i++) {
            int t = sc.nextInt();

            int left = 0;
            int right = n-1;
            
            int min_idx = n;
            int mid = (left + right) / 2;
            while(left <= right) {
                mid = (left + right) / 2;

                if(arr[mid] > t) {
                    right = mid - 1;
                }else if(arr[mid] == t) {
                    min_idx = Math.min(min_idx, mid);
                    right = mid - 1;
                }
                else {
                    left = mid + 1;
                }
            }

            if(min_idx == n)
                System.out.println(-1);
            else
                System.out.println(min_idx+1);
        }
        // Please write your code here.
    }
}