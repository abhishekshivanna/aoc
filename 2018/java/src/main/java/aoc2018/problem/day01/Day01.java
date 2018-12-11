package aoc2018.problem.day01;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class Day01 {

    private final File inputFile;
    private Set<Integer> set;

    Day01(File inputFile) {
        this.inputFile = inputFile;
        this.set = new HashSet<>();
    }

    int part1() {
        int sum = 0;
        try (Scanner sc = new Scanner(this.inputFile)) {
            while (sc.hasNextLine()) {
                sum += Integer.parseInt(sc.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return sum;
    }

    int part2() {
        this.set.add(0);
        int sum = 0;
        while (true) {
            try (Scanner sc = new Scanner(this.inputFile)) {
                while (sc.hasNextLine()) {
                    sum += Integer.parseInt(sc.nextLine());
                    if (this.set.contains(sum)) {
                        return sum;
                    }
                    this.set.add(sum);
                }
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }
    }
}
