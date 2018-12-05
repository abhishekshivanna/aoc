package aoc2018.problem.day04;

import java.util.List;


class Session {
  private int guardId;
  private List<Integer> sessionMinutes;

  Session(int guardId, List<Integer> sessionMinutes) {
    this.guardId = guardId;
    this.sessionMinutes = sessionMinutes;
  }

  int getGuardId() {
    return guardId;
  }

  List<Integer> getSessionMinutes() {
    return sessionMinutes;
  }
}
