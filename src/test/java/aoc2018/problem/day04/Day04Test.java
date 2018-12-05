package aoc2018.problem.day04;

import java.io.File;
import java.util.Arrays;
import org.junit.Assert;
import org.junit.Test;


public class Day04Test {

  @Test
  public void shouldFindMostSleepyGuardIdAndMultiplyWithMostFrequentMinute() {
    ClassLoader classLoader = getClass().getClassLoader();
    File file = new File(classLoader.getResource("day04/test_input").getFile());
    Day04 day = new Day04(file);
    Assert.assertEquals(240, day.part1());
  }

  @Test
  public void shouldReturnGuardWithMostFrequentMinute() {
    ClassLoader classLoader = getClass().getClassLoader();
    File file = new File(classLoader.getResource("day04/test_input").getFile());
    Day04 day = new Day04(file);
    Assert.assertEquals(4455, day.part2());
  }

  @Test
  public void guardProfileShouldReturnMostFrequentMinute() {
    GuardProfile profile = new GuardProfile(1);
    profile.addMinutesToProfile(Arrays.asList(1, 2, 3, 4));
    profile.addMinutesToProfile(Arrays.asList(4, 5, 6, 7));
    Assert.assertEquals(4, profile.getMostFrequentMinute());
    profile.addMinutesToProfile(Arrays.asList(6, 7));
    profile.addMinutesToProfile(Arrays.asList(7, 8, 9, 10));
    Assert.assertEquals(7, profile.getMostFrequentMinute());
  }
}