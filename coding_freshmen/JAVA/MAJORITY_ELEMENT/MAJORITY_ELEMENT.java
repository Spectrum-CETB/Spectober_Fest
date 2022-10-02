public class Main {
    public static void main(String[] args) {

        int[] nums = {7,1,5,7,8,12,24,7,7,7};
        System.out.println(majorityElement(nums));
    }
    static int majorityElement(int[] arr){
        int count = 0, max = 0, temp = -1;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j]){
                    count++;
                    if (count > max){
                        max = count;
                        temp = arr[i];
                    }
                }
            }
            count = 0;
        }
        return temp;
    }
}
