package aoc2018.problem.day02;

import java.io.File;
import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        ClassLoader classLoader = Main.class.getClassLoader();
        File file = new File(classLoader.getResource("day02/input").getFile());
        Day02 day = new Day02(file);
        System.out.println(day.part1());
        System.out.println(day.part2());
    }
}
