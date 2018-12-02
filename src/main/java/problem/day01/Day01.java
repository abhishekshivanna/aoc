package problem.day01;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class Day01 {

    private final File inputFile;
    Set<Integer> set;

    Day01(File inputFile) {
        this.inputFile = inputFile;
        this.set = new HashSet<>();
    }

    int part1() throws FileNotFoundException {
        int sum = 0;
        try (Scanner sc = new Scanner(this.inputFile)) {
            while (sc.hasNextLine()) {
                sum += Integer.parseInt(sc.nextLine());
            }
        }
        return sum;
    }

    int part2() throws FileNotFoundException {
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
            }
        }
    }
}
