
import java.util.*;
class Solution {
    private static final String[] numerals =
            {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    private static final int[] values = {
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

    public int romanToInt(String s) {
        int result = 0;
        for (int i = 0; i < numerals.length; i++) {
            while (s.startsWith(numerals[i])) {
                result += values[i];
                s = s.substring(numerals[i].length());
            }
        }
        return result;
    }
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the roman number");
        String r= sc.nextLine();
        r=r.toUpperCase(Locale.ROOT);
        Solution obj = new Solution();
        int result = obj.romanToInt(r);
        System.out.println("Integer = "+ result);
    }
}