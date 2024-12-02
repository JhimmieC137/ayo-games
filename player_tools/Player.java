package player_tools;

import utils.*;

import java.util.ArrayList;

public class Player {

    public String name;
    public int[] boardHoles;
    public int side;
    public int capturedSeeds;
    public boolean isComp = false;

    public Player createPlayer(String name, Integer side, Boolean isComp) {
        this.name = name;
        this.side = side;
        this.isComp = isComp;
        this.boardHoles = new int[]{4, 4, 4, 4, 4, 4};
        this.capturedSeeds = 0;

        return this;
    }

    public Integer totalSeeds() {
        Integer sumSeed = 0;
        for (Integer seed : boardHoles) sumSeed+=seed;

        return sumSeed;
    }

    public ArrayList<Player> assignPlayers() {
        int iter = 0;
        ArrayList<Player> players = new ArrayList<>();

        while (iter < 2){
            String prompt = "Input a name for Player_%d\nPress <Enter> to select computer as player: ";
            String playerName = new Validators().validateStringInput(String.format(prompt, iter+1), true);
            Player player = new Player().createPlayer(playerName.isEmpty() ? String.format("Comp_%s", iter+1) : playerName, iter, playerName.isEmpty());
            System.out.println(player.name + " selected as player " + (iter+1));
            players.add(player);
            iter++;
        }

        return players;

    }
}

