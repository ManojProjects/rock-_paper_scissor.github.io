function play(userChoice) {
  const choices = ['Rock', 'Paper', 'Scissors'];
  const computerChoice = choices[Math.floor(Math.random() * 3)];
  let result = '';

  if (userChoice === computerChoice) {
    result = "It's a tie!";
  } else if (
    (userChoice === 'Rock' && computerChoice === 'Scissors') ||
    (userChoice === 'Paper' && computerChoice === 'Rock') ||
    (userChoice === 'Scissors' && computerChoice === 'Paper')
  ) {
    result = 'You Win! 🎉';
  } else {
    result = 'Computer Wins! 😄';
  }

  document.getElementById('result').innerHTML =
    `You chose: ${userChoice} <br> Computer chose: ${computerChoice} <br> <b>${result}</b>`;
}
