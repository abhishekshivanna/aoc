package aoc2018.problem.day05;

import java.io.File;

class Main {
    public static void main(String[] args) {
        ClassLoader classLoader = aoc2018.problem.day04.Main.class.getClassLoader();
        File file = new File(classLoader.getResource("day05/input").getFile());
        Day05 day = new Day05(file);
        System.out.println(day.part1());
        System.out.println(day.part2());
    }

}
