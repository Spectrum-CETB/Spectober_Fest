import java.util.Arrays;
import java.util.Scanner;

class sort {


    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int i,n;
        n= sc.nextInt();
        int[] arr = new int[n];
        for(i=0;i<n;i++)
            arr[i]=sc.nextInt();
        Arrays.sort(arr);

        System.out.printf("Modified arr[] : %s", Arrays.toString(arr));
    }
}