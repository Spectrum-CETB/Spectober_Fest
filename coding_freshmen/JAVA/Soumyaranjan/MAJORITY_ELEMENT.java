import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Size of the array: ");
        int l = sc.nextInt();
        int[] nums = new int[l];
        for (int i = 0; i < l; i++) {
            nums[i] = sc.nextInt();
        }

        System.out.println(majorityElement(nums));
    }
    static int majorityElement(int[] arr){
        int count = 0, max = 0, temp = -1;
        for (int j : arr) {
            for (int k : arr)
                if (j == k) {
                    count++;
                    if (count > max) {
                        max = count;
                        temp = j;
                    }
                }
            count = 0;
        }
        return temp;
    }
}
