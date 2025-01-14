function getBoards(board) {
    boardOne = board.slice(0, 6);
    boardTwo = board.slice(6, 12);

    return [boardOne, boardTwo];
}

function getValidHoles(holes) {
    const validHoles = [];
    for (const hole in holes) {
        if (holes[hole] != 0) validHoles.push(hole);
    }

    return validHoles;    
}

function validateEndGame(boardState, nextSide) {
    const sideBoardState = boardState.slice((nextSide * 6), (6 + (nextSide * 6)));
    const holes = getValidHoles(sideBoardState);
    let compulsoryHole = null;

    for (const hole of holes) {
        if (sideBoardState[hole] > (6 - hole)) compulsoryHole = hole;
    }

    if (compulsoryHole) return compulsoryHole 
    
    return false
}


function validateSelection(currentSide, otherSide, selectedHole) {
    let firstSide
    let secondSide
    currentSide.side === 0 ? firstSide = currentSide : firstSide = otherSide;
    otherSide.side === 1 ? secondSide = otherSide : secondSide = currentSide;
    const currentBoard = [...firstSide.boardHoles, ...secondSide.boardHoles];
    let totalSeeds = 0;
    let seedCount = 0;
    otherSide.boardHoles.forEach(el => totalSeeds += el);

    if (currentSide.isComp) {
        if (totalSeeds === 0) selectedHole = validateEndGame(currentBoard, currentSide.side);
    } else {
        if ((totalSeeds === 0) && (selectedHole != validateEndGame(currentBoard, currentSide.side))) {
            if (selectedHole != validateEndGame(currentBoard, currentSide.side))
                throw Error("Please select the last hole with a seed to continue the game!")
        }
    }

    console.log(`${currentSide.name} picked hole ${selectedHole}`);

    if (0 <= selectedHole && selectedHole < 7) {
        let boardIndex = selectedHole + (currentSide.side * 6);
        seedCount = currentBoard[boardIndex];
        
        if (seedCount === 0) throw Error("Hole has no seeds, Choose another!")
        else {
            currentBoard[boardIndex] = 0;
            return [currentBoard, boardIndex, seedCount]
        };
    } else throw Error("Invalid hole!");

}


function moveAndCapture(currentBoard, boardIndex, seedCount, currentSide) {
    while (seedCount > 0) {
        ++boardIndex
        if (boardIndex > 11) {
            boardIndex = 0
        }
        ++currentBoard[boardIndex]
        --seedCount
    }

    if (currentBoard[boardIndex] === 4) {
        currentSide.captured = currentSide.captured + currentBoard[boardIndex]
        console.log(`${currentSide.name} captured seeds in hole ${boardIndex + 1}`)
        
        currentBoard[boardIndex] = 0;
    }
    return getBoards(currentBoard);
}

function playBoard(playerOne, playerTwo, currentSide, selectedHole) {
    const [updatedBoard, boardIndex, seedCount] = validateSelection(currentSide, currentSide === playerOne ? playerTwo : playerOne, selectedHole);
    
    return moveAndCapture(updatedBoard, boardIndex, seedCount, currentSide);
}