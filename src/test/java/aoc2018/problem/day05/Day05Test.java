package aoc2018.problem.day05;

import org.junit.Assert;
import org.junit.Test;

import java.io.File;


public class Day05Test {

    @Test
    public void shouldReturnSizeOfShrunkPolymer() {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day05/test_input").getFile());
        Day05 day = new Day05(file);
        Assert.assertEquals(10, day.part1());
    }

    @Test
    public void shouldReturnSizeOfSmallestShrunkPolymer() {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day05/test_input").getFile());
        Day05 day = new Day05(file);
        Assert.assertEquals(4, day.part2());
    }
}