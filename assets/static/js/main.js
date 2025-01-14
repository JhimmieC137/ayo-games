function getPlayerName(inputId, wrapperId) {
    if (!$(wrapperId).is(":visible")) $(wrapperId).show()
    const inputValue = $(inputId).val();
    console.log(inputValue);
    $(wrapperId).hide();

    return inputValue;
}

function lunchGame(firstPlayer, secondPlayer) {
    $("#player-two-name-disp").text(secondPlayer.name);
    $("#player-one-name-disp").text(firstPlayer.name);
    [...secondPlayer.boardHoles, ...firstPlayer.boardHoles].forEach((el, index) => $(".board-grid").append(`<div class="board-hole"><p class="seeds" data-value=${index}>${el}</p></div>`));
    $("#game-arena").show();
}

function updateBoardDisplay(board) {
    let boardIndex = 11
    $("p.seeds").each((index, element) => {
        if (boardIndex > 5) {
            $(element).text(board[boardIndex]);
            --boardIndex;
        } else {
            $(element).text(board[index - 6]);
        }
    });
}

function computerPlay(players) {
    console.log(players)
    const playableHoles = getValidHoles(players.currentSide.boardHoles);
    const chosenHole = getRandomElement(playableHoles);
    console.log(chosenHole)
    [players.playerOne.boardHoles, players.playerTwo.boardHoles] = playBoard(players.playerOne, players.playerTwo, players.currentSide, chosenHole);
    console.log(players)
    updateBoardDisplay([...players.playerOne.boardHoles, ...players.playerTwo.boardHoles])

    return [players.playerOne, players.playerTwo]
}

$(function() {
    const players = {
        playerOne: null,
        playerTwo: null,
        currentSide: null,  
    };

    $("#player-one-intro").show();

    $(".player-one-pc-selector").on("click", function() {
        players.playerOne = new Player()
        players.playerOne.createPlayer("Comp 1", 0, true)
        $("#player-one-intro").hide();
        $("#player-two-intro").show();
        console.log(players);
    });
    
    $(".player-two-pc-selector").on("click", function() {
        players.playerTwo = new Player()
        players.playerTwo.createPlayer("Comp 2", 1, true)
        $("#player-two-intro").hide();
        console.log(players)
        lunchGame(players.playerOne, players.playerTwo);
        players.currentSide = players.playerOne;
        if (players.currentSide.isComp) [players.playerOne, players.playerTwo] = computerPlay(players);
        players.currentSide = players.playerTwo;
    });

    $("#player-one-intro").submit(function(event) {
        event.preventDefault();
        const playerOneName = getPlayerName("#player-one-name", "#player-one-intro");
        players.playerOne = new Player()
        players.playerOne.createPlayer(playerOneName, 0, false);   
        $("#player-two-intro").show();
    });

    
    $("#player-two-intro").submit(function(event) {
        event.preventDefault();
        const playerTwoName = getPlayerName("#player-two-name", "#player-two-intro");
        players.playerTwo = new Player()
        players.playerTwo.createPlayer(playerTwoName, 1, false);
        lunchGame(players.playerOne, players.playerTwo);
        players.currentSide = players.playerOne;
        if (players.currentSide.isComp) [players.playerOne, players.playerTwo] = computerPlay(players);
        players.currentSide = players.playerTwo;
    }); 


    $(".board-grid").on("click", ".board-hole p.seeds", function () {
        // try {
        [players.playerOne.boardHoles, players.playerTwo.boardHoles] = playBoard(players.playerOne, players.playerTwo, players.currentSide, Number($(this).data('value') - 6));
        updateBoardDisplay([...players.playerOne.boardHoles, ...players.playerTwo.boardHoles])
        players.currentSide === players.playerOne ? players.currentSide = players.playerTwo : players.currentSide = players.playerOne;
        if (players.currentSide.isComp) [players.playerOne, players.playerTwo] = computerPlay(players);
        
        // } catch (error) {
        //     $("#messages .warning p").text(error)
        //     $("#messages .warning").css({"opacity": 1})
        //     setTimeout(() => $("#messages .warning").css({"opacity": 0}), 5000)
        // }
    });    
});