package aoc2018.problem.day05;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

class Day05 {

    private File inputFile;
    private final String polymer;

    Day05(File file) {
        this.inputFile = file;
        polymer = loadInput();
    }

    private String loadInput() {
        String line = "";
        try (Scanner sc = new Scanner(this.inputFile)) {
            line = sc.useDelimiter("\\A").next();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return line;
    }

    private char getPolarOpposite(char c) {
        return (Character.isLowerCase(c)) ? Character.toUpperCase(c) : Character.toLowerCase(c);
    }

    private String shrink(String polymer) {
        Deque<Character> stack = new LinkedList<>();
        for (char c : polymer.toCharArray()) {
            if (!stack.isEmpty() && c == getPolarOpposite(stack.peekFirst())) {
                stack.removeFirst();
            } else {
                stack.addFirst(c);
            }
        }
        return stack.stream().map(String::valueOf).reduce((acc, e) -> e + acc).get();
    }

    private String getShrunkPolymerWithoutChar(String polymer, char unit) {
        return shrink(polymer.replaceAll(String.format("[%s|%s]", unit, getPolarOpposite(unit)), ""));
    }

    int part1() {
        return shrink(this.polymer).length();
    }

    int part2() {
        int min = Integer.MAX_VALUE, currentLength;
        Set<Character> characterSet = new HashSet<>();
        for (char c : this.polymer.toCharArray()) {
            characterSet.add(Character.toLowerCase(c));
        }
        for (Character c : characterSet) {
            currentLength = getShrunkPolymerWithoutChar(this.polymer, c).length();
            if (currentLength < min) {
                min = currentLength;
            }
        }
        return min;
    }
}
