function calcRps(move) {
    let gameCharacters = { 'p': 'paper', 'r': 'rock', 's': 'scissors' },
        chrValues = Object.values(gameCharacters),
        computerMove = chrValues[Math.floor(Math.random() * chrValues.length)];  // Get random character
        
    var computerScore = Number(document.getElementById('computerScore').innerHTML),
        playerScore = Number(document.getElementById('playerScore').innerHTML);
    document.getElementById('computerImage').src = `images/${computerMove}.svg`;

    switch (move) {
        case 'p':
            move = gameCharacters[move];
            if (move == computerMove) {
            } else if (computerMove == 'rock') {
                document.getElementById('playerScore').innerHTML = playerScore + 1;
            } else if (computerMove == 'scissors') {
                document.getElementById('computerScore').innerHTML = computerScore + 1;
            }
            break;

        case 'r':
            move = gameCharacters[move];

            if (move == computerMove) {
            } else if (computerMove == 'scissors') {
                document.getElementById('playerScore').innerHTML = playerScore + 1;
            } else if (computerMove == 'paper') {
                document.getElementById('computerScore').innerHTML = computerScore + 1;
            }
            break;

        case 's':
            move = gameCharacters[move];

            if (move == computerMove) {
            } else if (computerMove == 'paper') {
                document.getElementById('playerScore').innerHTML = playerScore + 1;
            } else if (computerMove == 'rock') {
                document.getElementById('computerScore').innerHTML = computerScore + 1;
            }
    }
}

function play() {
    const rockButton = document.querySelector('#rockButton');
    rockButton.addEventListener('click', (e) => {
        e.preventDefault();
        let playerMove = 'r';
        calcRps(playerMove)
        document.getElementById('playerImage').src = 'images/rock.svg';
    });

    const paperButton = document.querySelector('#paperButton');
    paperButton.addEventListener('click', (e) => {
        let playerMove = 'p';
        calcRps(playerMove)
        document.getElementById('playerImage').src = 'images/paper.svg';
    });

    const scissorsButton = document.querySelector('#scissorsButton');
    scissorsButton.addEventListener('click', (e) => {
        let playerMove = 's';
        calcRps(playerMove)
        document.getElementById('playerImage').src = 'images/scissors.svg';
    });
}