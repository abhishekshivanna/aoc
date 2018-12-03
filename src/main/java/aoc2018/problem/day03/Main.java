package aoc2018.problem.day03;

import java.io.File;
import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) {
        ClassLoader classLoader = Main.class.getClassLoader();
        File file = new File(classLoader.getResource("day03/input").getFile());
        Day03 day = new Day03(1000, 1000, file);
        System.out.println(day.part1());
        System.out.println(day.part2());
    }
}
