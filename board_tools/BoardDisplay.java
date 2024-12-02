package board_tools;

import player_tools.Player;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Optional;
import java.util.stream.IntStream;

public class BoardDisplay {
    public void printBoardState(Player playerOne, Player playerTwo) {
        System.out.println(Arrays.toString(mergeBoards(playerOne.boardHoles, playerTwo.boardHoles)));
    }

    public int[] mergeBoards(int[] boardOne, int[] boardTwo) {
        return IntStream.concat(Arrays.stream(boardOne), Arrays.stream(boardTwo)).toArray();
    }

    public ArrayList<Integer> getPlayableHoles(ArrayList<Integer> holes) {
        ArrayList<Integer> validHoles = new ArrayList<>();
        for (int iter = 0; iter < holes.size(); iter++) if (holes.get(iter) != 0) validHoles.add(iter+1);

        return validHoles;
    }

    public Optional<Integer> validateEndOfPlay(ArrayList<Integer> boardState, int nextSide) {
        ArrayList<Integer> sideBoardState = new ArrayList<>(boardState.subList((nextSide * 6), 6 + (nextSide * 6)));
        ArrayList<Integer> holes = getPlayableHoles(sideBoardState);
        Integer validatedHoleOfPlay;
        holes.forEach( hole -> {
            if (sideBoardState.get(hole - 1) > (6 - hole)) validatedHoleOfPlay = hole;
        });
        return validatedHoleOfPlay;
    }
}