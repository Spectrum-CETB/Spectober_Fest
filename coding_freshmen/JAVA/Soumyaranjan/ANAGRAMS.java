import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = sc.next();

        System.out.println(anagram(s, t));

    }

    static boolean anagram(String s, String t) {

        char[] Str1 = (s).toCharArray();
        char[] Str2 = (t).toCharArray();
        Arrays.sort(Str1);
        Arrays.sort(Str2);
        return Arrays.equals(Str2, Str1);
    }
}
