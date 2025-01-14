import { playBoard, validateEndGame } from "./tools/boardTools";
import { assignPlayers } from "./tools/playerTools";

const [playerOne, playerTwo] = assignPlayers()
const currentPlayer = playerOne

while (playerOne.getTotalSeeds() + playerTwo.getTotalSeeds() > 2) {
    [playerOne.boardHoles, playerTwo.boardHoles] = playBoard(playerOne, playerTwo, currentPlayer);

    currentPlayer = playerTwo === currentPlayer ? playerOne : playerTwo;

    if ((playerOne.getTotalSeeds() === 0 || playerTwo.getTotalSeeds() === 0) && !validateEndGame([...playerOne, ...playerTwo], currentPlayer.side)) break
}

console.log("End of game")