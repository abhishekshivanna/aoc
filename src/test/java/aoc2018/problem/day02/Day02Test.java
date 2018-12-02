package aoc2018.problem.day02;

import org.junit.Assert;
import org.junit.Test;

import java.io.File;
import java.io.FileNotFoundException;


public class Day02Test {

    @Test
    public void shouldReturnCheckSum() throws FileNotFoundException {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day02/test_input_1").getFile());
        Day02 day02 = new Day02(file);
        Assert.assertEquals(12, day02.part1());
    }

    @Test
    public void shouldReturnCommonPartsOfStringsWithEditDistanceOf1() throws FileNotFoundException {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day02/test_input_2").getFile());
        Day02 day02 = new Day02(file);
        Assert.assertEquals("fgij", day02.part2());
    }
}