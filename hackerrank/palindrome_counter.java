// Too slow

// Goldman Sachs 2023 intern application

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'countPalindromes' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING s as parameter.
     */
     
    public static int palindromes(String s, int i) {
        int count = 0;
        for (int j = 0; j < s.length() - i + 1; j++) {
            StringBuilder s2 = new StringBuilder(s.substring(j, j + i));
            if (s2.toString().equals(s2.reverse().toString())) {
                count += 1;
            }
        }
        return count;
    }

    public static int countPalindromes(String s) {
        int count = s.length();
        for (int i = 2; i < s.length() + 1; i++) {
            count += palindromes(s, i);
        }
        return count;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        int result = Result.countPalindromes(s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
