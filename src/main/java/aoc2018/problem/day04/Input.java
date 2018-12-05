package aoc2018.problem.day04;

import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Input implements Comparable<Input> {
  private static final Pattern pattern = Pattern.compile("^\\[\\d+-(\\d+)-(\\d+)\\s(\\d+):(\\d+)]\\s(.*)$"); // [1518-11-01 00:00] fobar

  int month, date, hour, minute;
  String content, fullContent;

  Input(String line) {
    Matcher matcher = pattern.matcher(line);
    matcher.find();
    this.month = Integer.parseInt(matcher.group(1));
    this.date = Integer.parseInt(matcher.group(2));
    this.hour = Integer.parseInt(matcher.group(3));
    this.minute = Integer.parseInt(matcher.group(4));
    this.content = matcher.group(5);
    this.fullContent = line;
  }

  @Override
  public int compareTo(Input o) {
    return fullContent.compareTo(o.fullContent);
  }

  int getGuardId() {
    Pattern pattern = Pattern.compile("^Guard\\s#(\\d+)\\sbegins\\sshift$");
    Matcher matcher = pattern.matcher(this.content);
    matcher.find();
    if (this.content.endsWith("begins shift")) {
      return Integer.parseInt(matcher.group(1));
    }
    return -1;
  }

  int getSleepStart() {
    if (this.content.endsWith("falls asleep")) {
      return minute;
    }
    return -1;
  }

  int getSleepEnd() {
    if (this.content.endsWith("wakes up")) {
      return minute;
    }
    return -1;
  }
}
