package problem.day01;

import java.io.File;
import java.io.FileNotFoundException;

public class Main {
    private static Day01 day01;

    public static void main(String[] args) throws FileNotFoundException {
        ClassLoader classLoader = Main.class.getClassLoader();
        File file = new File(classLoader.getResource("day01/input").getFile());
        day01 = new Day01(file);
        System.out.println(day01.part1());
        System.out.println(day01.part2());
    }
}
