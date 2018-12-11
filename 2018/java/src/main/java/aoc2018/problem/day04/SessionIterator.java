package aoc2018.problem.day04;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


class SessionIterator {

  private List<Input> inputs;
  private int currentIndex;

  SessionIterator(List<Input> inputs) {
    this.inputs = inputs;
    this.currentIndex = 0;
  }

  Session getNextSession() {
    int i = 0, currentGuard = -1, start, end;
    List<Integer> currentSessionMinutes = new ArrayList<>();
    while (this.currentIndex < inputs.size()) {
      if (this.inputs.get(this.currentIndex).content.startsWith("Guard")) {
        if (currentGuard != -1) {
          return new Session(currentGuard, currentSessionMinutes);
        }
        currentGuard = this.inputs.get(this.currentIndex++).getGuardId();
      } else if (this.inputs.get(this.currentIndex).content.startsWith("falls")) {
        start = this.inputs.get(this.currentIndex).getSleepStart();
        this.currentIndex++;
        end = this.inputs.get(this.currentIndex).getSleepEnd();
        this.currentIndex++;
        currentSessionMinutes.addAll(IntStream.range(start, end).boxed().collect(Collectors.toList()));
      }
    }
    return new Session(currentGuard, currentSessionMinutes);
  }

  boolean hasNext() {
    return this.currentIndex < this.inputs.size();
  }
}
