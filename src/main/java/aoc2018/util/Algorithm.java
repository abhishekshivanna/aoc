package aoc2018.util;

public class Algorithm {

    public static int editDistance(String s1, String s2) {
        int distance=0;
        int min_len = Math.min(s1.length(), s2.length());
        for (int i=0; i<min_len; i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                distance++;
            }
        }
        distance += Math.abs(s1.length() - s2.length());
        return distance;
    }
}
