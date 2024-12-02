package board_tools;

import player_tools.Player;

public class BoardPlay {
    public void validateSelection (Player currentplayer, Player otherPlayer) {
        int[] currentBaoard = new BoardDisplay().mergeBoards(currentplayer.side != 0 ? otherPlayer.boardHoles : currentplayer.boardHoles, (currentplayer.side != 1 ? otherPlayer.boardHoles : currentplayer.boardHoles));
        int seedCount = 0;

        while (seedCount == 0) {

        }
    }

    public void playTurn () {

    }
}
