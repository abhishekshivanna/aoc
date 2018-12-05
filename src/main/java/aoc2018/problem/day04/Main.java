package aoc2018.problem.day04;

import java.io.File;


public class Main {
  public static void main(String[] args) {
    ClassLoader classLoader = Main.class.getClassLoader();
    File file = new File(classLoader.getResource("day04/input").getFile());
    Day04 day = new Day04(file);
    System.out.println(day.part1());
    System.out.println(day.part2());
  }
}
