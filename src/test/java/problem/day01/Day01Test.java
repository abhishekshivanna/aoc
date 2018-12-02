package problem.day01;

import org.junit.Assert;
import org.junit.Test;
import problem.day01.Day01;

import java.io.File;
import java.io.FileNotFoundException;

public class Day01Test {
    @Test
    public void shouldGiveSumOfNumbers() throws FileNotFoundException {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day1/test_input").getFile());
        Day01 day01 = new Day01(file);
        Assert.assertEquals(day01.part1(), -1);
    }

    @Test
    public void shouldReturnFirstRepeatSum() throws FileNotFoundException {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day1/test_input").getFile());
        Day01 day01 = new Day01(file);
        Assert.assertEquals(day01.part2(), -1);
    }
}