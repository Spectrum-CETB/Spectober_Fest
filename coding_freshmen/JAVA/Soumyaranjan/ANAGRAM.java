import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        int[] index = largestSum(arr);
        int[] ans = Arrays.copyOfRange(arr, index[0], index[1] + 1);

        System.out.println(Arrays.toString(ans) + " has the largest sum " + sum(arr, index[0], index[1]));
    }

    static int[] largestSum(int[] arr) {
        int s = 0, max = Integer.MIN_VALUE, sum = 0, e = arr.length - 1;
        int[] ans = { 0, 0 };
        for (int i = 1; i < arr.length; i++) {
            s = 0;
            e = i - 1;
            for (int j = 0; j < arr.length; j++) {
                sum = sum(arr, s, e);
                if (sum > max) {
                    max = sum;
                    ans[0] = s;
                    ans[1] = e;
                }
                s++;
                e++;
                if (e > 8) {
                    break;
                }
            }
        }
        return ans;
    }

    static int sum(int[] arr, int s, int e) {
        int sum = 0;
        for (int k = s; k <= e; k++) {
            sum += arr[k];
        }
        return sum;
    }
}