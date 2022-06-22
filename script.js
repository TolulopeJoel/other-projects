function calcRps(move) {
    let gameCharacters = { 'p': 'paper', 'r': 'rock', 's': 'scissors' },
    chrValues = Object.values(gameCharacters),
    computerMove = chrValues[Math.floor(Math.random() * chrValues.length)];
    var computerScore = Number(document.getElementById('computerScore').innerHTML), playerScore = Number(document.getElementById('playerScore').innerHTML);
    document.getElementById('computerImage').src = `images/${computerMove}.svg`;

    if (move == 'p') {
        move = gameCharacters[move];
        if (move == computerMove) {
            document.querySelector('.vs').innerHTML = '🎀'
        } else if (computerMove == 'rock') {
            document.querySelector('.vs').innerHTML = 'VS'
            document.getElementById('playerScore').innerHTML = playerScore + 1;
        } else if (computerMove == 'scissors') {
            document.querySelector('.vs').innerHTML = 'VS'
            document.getElementById('computerScore').innerHTML = computerScore + 1;
        }

    } else if (move == 'r') {
        move = gameCharacters[move];

        if (move == computerMove) {
            document.querySelector('.vs').innerHTML = '🎀'
        } else if (computerMove == 'scissors') {
            document.querySelector('.vs').innerHTML = 'VS'
            document.getElementById('playerScore').innerHTML = playerScore + 1;
        } else if (computerMove == 'paper') {
            document.querySelector('.vs').innerHTML = 'VS'
            document.getElementById('computerScore').innerHTML = computerScore + 1;
        }

    } else if (move == 's') {
        move = gameCharacters[move];

        if (move == computerMove) {
            document.querySelector('.vs').innerHTML = '🎀'
        } else if (computerMove == 'paper') {
            document.querySelector('.vs').innerHTML = 'VS'
            document.getElementById('playerScore').innerHTML = playerScore + 1;
        } else if (computerMove == 'rock') {
            document.querySelector('.vs').innerHTML = 'VS'
            document.getElementById('computerScore').innerHTML = computerScore + 1;
        }
    }
}

function play() {

    const rockButton = document.querySelector('#rockButton');
    rockButton.addEventListener('click', function (e) {
        e.preventDefault();
        let playerMove = 'r';
        calcRps(playerMove)
        document.getElementById('playerImage').src = 'images/rock.svg';
    });

    const paperButton = document.querySelector('#paperButton');
    paperButton.addEventListener('click', function (e) {
        let playerMove = 'p';
        calcRps(playerMove)
        document.getElementById('playerImage').src = 'images/paper.svg';
    });

    const scissorsButton = document.querySelector('#scissorsButton');
    scissorsButton.addEventListener('click', function aba(e) {
        let playerMove = 's';
        calcRps(playerMove)
        document.getElementById('playerImage').src = 'images/scissors.svg';
    });
}

// onload="playerName = Math.floor(Math.random() * players.length);document.getElementById('otherPlayer').innerHTML = players[playerName].toUpperCase()"