package aoc2018.problem.day03;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Day03 {

    private ClothUnit cloth[][];
    private final File inputFile;

    Day03(int tall, int wide, File inputFile) {
        this.cloth = new ClothUnit[tall][wide];
        this.inputFile = inputFile;
        loadInput();
    }

    private void loadInput() {
        String line;
        Matcher matcher;
        Pattern pattern = Pattern.compile("^#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)$"); // #claimId @ fromLeft,fromTop: tallxwide
        try (Scanner sc = new Scanner(this.inputFile)) {
            while (sc.hasNextLine()) {
                line = sc.nextLine();
                matcher = pattern.matcher(line);
                matcher.find();
                claimDimensions(Integer.parseInt(matcher.group(1)), // claimId
                        Integer.parseInt(matcher.group(3)), // startRow
                        Integer.parseInt(matcher.group(2)), // startColumn
                        Integer.parseInt(matcher.group(5)), // wide
                        Integer.parseInt(matcher.group(4))); // tall
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private void claimDimensions(int claimId, int startY, int startX, int wide, int tall) {
        for (int i=startX; i<startX+tall; i++) {
            for(int j=startY; j<startY+wide; j++){
                if (cloth[i][j] == null) {
                    cloth[i][j] = new ClothUnit();
                }
                cloth[i][j].addClaim(claimId);
            }
        }
    }

    int part1() {
        int overlap=0 ;
        for (ClothUnit[] row : cloth) {
            for (ClothUnit rowColumnUnit : row) {
                if (rowColumnUnit != null && rowColumnUnit.getNumClaims() > 1) {
                    overlap++;
                }
            }
        }
        return overlap;
    }

    int part2() {
        Set<Integer> nonOverlap = new HashSet<>();
        Set<Integer> overlap = new HashSet<>();
        for (ClothUnit[] row : cloth) {
            for (ClothUnit rowColumnUnit : row) {
                if (rowColumnUnit != null) {
                    if (rowColumnUnit.getNumClaims() == 1) {
                        nonOverlap.addAll(rowColumnUnit.getAllClaims());
                    } else {
                        overlap.addAll(rowColumnUnit.getAllClaims());
                    }
                }
            }
        }
        nonOverlap.removeAll(overlap);
        return nonOverlap.iterator().next();
    }

}
