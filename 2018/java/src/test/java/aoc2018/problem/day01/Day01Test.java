package aoc2018.problem.day01;

import org.junit.Assert;
import org.junit.Test;

import java.io.File;
import java.io.FileNotFoundException;

public class Day01Test {
    @Test
    public void shouldGiveSumOfNumbers() {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day01/test_input").getFile());
        Day01 day01 = new Day01(file);
        Assert.assertEquals(-1, day01.part1());
    }

    @Test
    public void shouldReturnFirstRepeatSum() {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day01/test_input").getFile());
        Day01 day01 = new Day01(file);
        Assert.assertEquals(-1, day01.part2());
    }
}