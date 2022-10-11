import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        String s = "rat", t = "car";
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
