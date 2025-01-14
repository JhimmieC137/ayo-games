class Player {
    constructor() {
        this.boardHoles = null;
        this.captured = null;
        this.name = null;
        this.side = null;
        this.isComp = null
    }

    createPlayer(name, side, isComp) {
        this.name = name;
        this.side = side;
        this.isComp= isComp;
        this.boardHoles = [4, 4, 4, 4, 4, 4]
        this.captured = 0;
    }

    getTotalSeeds() {
        let totalSeeds = 0;
        this.boardHoles.forEach(() => ++totalSeeds);
        
        return totalSeeds;
    }

    
}


function assignPlayers(playerOneName, playerTwoName) {
    const playerOne = new Player();
    playerOne.createPlayer(typeof playerOneName === 'string'? playerOneName : "Comp 1", 0, typeof playerOneName === 'string'? false : true);
    
    const playerTwo = new Player();
    playerTwo.createPlayer(typeof playerTwoName === 'string'? playerTwoName : "Comp 1", 1, typeof playerTwoName === 'string'? false : true);

    return [playerOne, playerTwo];
}