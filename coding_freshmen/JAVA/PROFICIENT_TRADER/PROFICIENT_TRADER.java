public class Main {
    public static void main(String[] args) {

        int[] arr = {7,1,5,3,6,4};
        System.out.println(maxProfit(arr));
    }
    static int maxProfit(int[] arr){
        int max = 0, profit = 0;
        for (int i = 0; i < arr.length-1; i++) {
            profit = arr[i+1] - arr[i];
            if (profit > max){
                max = profit;
            }
        }
        return max;
    }
}
