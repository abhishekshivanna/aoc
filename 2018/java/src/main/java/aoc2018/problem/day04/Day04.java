package aoc2018.problem.day04;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import javafx.util.Pair;


class Day04 {

  private final File inputFile;
  private List<Input> lines;
  private Map<Integer, GuardProfile> guardProfile;

  Day04(File inputFile) {
    this.inputFile = inputFile;
    this.lines = new ArrayList<>();
    loadInput();
  }

  private void loadInput() {
    String line;

    try (Scanner sc = new Scanner(this.inputFile)) {
      while (sc.hasNextLine()) {
        line = sc.nextLine();
        this.lines.add(new Input(line));
      }
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }
    Collections.sort(this.lines);
    buildGuardProfile();
  }

  private void buildGuardProfile() {
    guardProfile = new HashMap<>();
    GuardProfile currentGuardProfile;
    SessionIterator sleepSessions = new SessionIterator(this.lines);
    Session session;
    while (sleepSessions.hasNext()) {
      session = sleepSessions.getNextSession();
      currentGuardProfile = guardProfile.getOrDefault(session.getGuardId(), new GuardProfile(session.getGuardId()));
      currentGuardProfile.addMinutesToProfile(session.getSessionMinutes());
      guardProfile.put(session.getGuardId(), currentGuardProfile);
    }
  }

  private GuardProfile getMostSleepyGuard() {
    int max = 0;
    GuardProfile mostSleepyGuard = null;
    for (GuardProfile profile : guardProfile.values()) {
      if (mostSleepyGuard == null) {
        mostSleepyGuard = profile;
      } else if (profile.getAllMinutes().size() > mostSleepyGuard.getAllMinutes().size()) {
        mostSleepyGuard = profile;
      }
    }
    return mostSleepyGuard;
  }

  private Pair<Integer, Integer> getMostFreqMinuteAndCountAmongGuards() {
    int maxId = 0, maxMinuteCount = 0, minuteOfMaxCount = 0;
    Pair<Integer, Integer> mostFrequentMinute;
    for (GuardProfile profile : guardProfile.values()) {
      mostFrequentMinute = profile.getMostFreqMinute();
      if (mostFrequentMinute.getValue() > maxMinuteCount) {
        maxMinuteCount = mostFrequentMinute.getValue();
        maxId = profile.getId();
        minuteOfMaxCount = mostFrequentMinute.getKey();
      }
    }
    return new Pair<>(maxId, minuteOfMaxCount);
  }

  public int part1() {
    GuardProfile mostSleepyGuard = getMostSleepyGuard();
    return mostSleepyGuard.getId() * mostSleepyGuard.getMostFrequentMinute();
  }

  public int part2() {
    Pair<Integer, Integer> minuteFreq = getMostFreqMinuteAndCountAmongGuards();
    return minuteFreq.getKey() * minuteFreq.getValue();
  }
}