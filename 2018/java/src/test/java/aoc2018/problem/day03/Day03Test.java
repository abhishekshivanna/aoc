package aoc2018.problem.day03;

import org.junit.Assert;
import org.junit.Test;

import java.io.File;

public class Day03Test {

    @Test
    public void shouldReturnNumberOfOverlapUnits() {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day03/test_input").getFile());
        Day03 day = new Day03(9, 11, file);
        Assert.assertEquals(4, day.part1());
    }

    @Test
    public void shouldReturnClaimIdOfNonOverlappingOrder() {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("day03/test_input").getFile());
        Day03 day = new Day03(9, 11, file);
        Assert.assertEquals(3, day.part2());
    }
}