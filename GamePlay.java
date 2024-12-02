import board_tools.BoardDisplay;
import player_tools.Player;

import java.util.ArrayList;
import java.util.Arrays;

public class GamePlay {

    public static void  startGame() {
        ArrayList<Player> players = new Player().assignPlayers();
        Player playerOne = players.getFirst();
        Player playerTwo = players.getLast();
        Player currentPlayer = playerOne;

        while (playerOne.totalSeeds() + playerTwo.totalSeeds() > 2) {
            currentPlayer = currentPlayer == playerOne ? playerTwo : playerOne;
        }

    }
}
