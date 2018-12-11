package aoc2018.util;

import org.junit.Assert;
import org.junit.Test;

public class AlgorithmTest {
    @Test
    public void testEditDistance() {
        Assert.assertEquals(1, Algorithm.editDistance("abcd", "aacd"));
        Assert.assertEquals(0, Algorithm.editDistance("abcd", "abcd"));
        Assert.assertEquals(0, Algorithm.editDistance("", ""));
    }
}