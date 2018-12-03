package aoc2018.problem.day03;

import java.util.ArrayList;
import java.util.List;

class ClothUnit {
    List<Integer> claims;

    ClothUnit() {
        claims = new ArrayList<>();
    }

    void addClaim(int id) {
        claims.add(id);
    }

    int getNumClaims() {
        return claims.size();
    }

    List<Integer> getAllClaims() {
        return claims;
    }
}