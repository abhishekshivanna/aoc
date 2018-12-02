package aoc2018.problem.day02;

import com.sun.tools.javac.util.Pair;
import aoc2018.util.Algorithm;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day02 {

    private final File inputFile;

    public Day02(File inputFile) {
        this.inputFile = inputFile;
    }

    Pair<Boolean, Boolean> twoThreeExists(String line) {
        boolean two=false, three=false;
        int f;
        Map<Character, Integer> charFreq = new HashMap<>();
        for (char c : line.toCharArray()) {
            f = charFreq.getOrDefault(c, 0);
            charFreq.put(c, f+1);
        }
        for (Map.Entry<Character,Integer> entry : charFreq.entrySet()) {
            if (entry.getValue() == 2) {
                two = true;
                if (three) break;
            }
            if (entry.getValue() == 3) {
                three = true;
                if (two) break;
            }
        }
        return new Pair<>(two, three);
    }

    String getCommonPart(String s1, String s2) {
        StringBuilder sb = new StringBuilder();
        int min_len = Math.min(s1.length(), s2.length());
        for (int i=0; i<min_len; i++) {
            if (s1.charAt(i) == s2.charAt(i)) {
                sb.append(s1.charAt(i));
            }
        }
        return sb.toString();
    }

    int part1() throws FileNotFoundException {
        int twoCount=0, threeCount=0;
        Pair<Boolean, Boolean> p;
        try (Scanner sc = new Scanner(this.inputFile)) {
            while (sc.hasNextLine()) {
                p = twoThreeExists(sc.nextLine());
                if (p.fst) twoCount++;
                if (p.snd) threeCount++;
            }
        }
        return twoCount * threeCount;
    }

    String part2() throws FileNotFoundException {
        List<String> ids = new ArrayList<>();
        try (Scanner sc = new Scanner(this.inputFile)) {
            while (sc.hasNextLine()) {
                ids.add(sc.nextLine());
            }
        }
        for(int i=0; i<ids.size(); i++) {
            for(int j=i+1; j<ids.size(); j++) {
                if (Algorithm.editDistance(ids.get(i), ids.get(j)) == 1) {
                    return getCommonPart(ids.get(i), ids.get(j));
                }
            }
        }
        return "";
    }
}
