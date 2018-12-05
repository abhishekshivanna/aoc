package aoc2018.problem.day04;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import javafx.util.Pair;


public class GuardProfile {
  private int id;
  private List<Integer> allMinutes;
  private Set<Integer> uniqueMinutes;

  GuardProfile(int id) {
    this.id = id;
    this.allMinutes = new ArrayList<>();
    this.uniqueMinutes = new HashSet<>();
  }

  int getId() {
    return id;
  }

  public List<Integer> getAllMinutes() {
    return allMinutes;
  }

  void addMinutesToProfile(List<Integer> minutes) {
    allMinutes.addAll(minutes);
    uniqueMinutes.addAll(minutes);
  }

  Set<Integer> getUniqueMinutes() {
    return uniqueMinutes;
  }

  int getMostFrequentMinute() {
    int max_freq = 0, max_minute = 0, temp;
    Map<Integer, Integer> map = new HashMap<>();
    for (int minute : allMinutes) {
      temp = map.getOrDefault(minute, 0) + 1;
      if (temp > max_freq) {
        max_freq = temp;
        max_minute = minute;
      }
      map.put(minute, temp);
    }
    return max_minute;
  }

  Pair<Integer, Integer> getMostFreqMinute() {
    int mostFrequentMinute = getMostFrequentMinute();
    return new Pair<>(mostFrequentMinute, Collections.frequency(allMinutes, mostFrequentMinute));
  }
}
