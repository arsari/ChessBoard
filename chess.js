// npm package require
var prompt = require('prompt-sync')()
var colors = require('colors')

// class definition
function ChessBoard (cols, rows) {
  this.cols = cols
  this.rows = rows
  var board = ''

  // index for control lines
  for (var i = 0; i < this.rows; i++) {
    // index for control characters in lines
    for (var j = 0; j < this.cols; j++) {
      if ((i + j) % 2 === 0) {
        board += ' '.bgWhite
      } else {
        board += ' '.bgBlack
      }
    }
    board += '\n'
  }
  return board
}

// input loop
while (true) {
    // script description and user input prompt
  console.log('\n================================================'.red + 'v1.0.170508'.yellow)
  console.log('This JS script will draw a chess board using the following\ninputs...'.cyan + '(For exit, press 0 or Enter in any of the inputs.)'.gray)
  console.log('-----------------------------------------------------------'.blue)
  var userColumns = Number(prompt('Enter a value for the number of COLUMNS: '.italic.yellow))
  var userRows = Number(prompt('Enter a value for the number of ROWS: '.italic.yellow))
  console.log('===========================================================\n'.red)

  // user inputs evaluation
  if (isNaN(userColumns) || isNaN(userRows)) {
    console.log('*** INPUT ERROR ***'.bgRed + '\n' + 'Input value of Columns and Rows should be a Number.'.bgRed)
  } else if (userColumns === 0 || userRows === 0) {
    console.log('-----------------'.bgMagenta)
    console.log('|'.bgMagenta + '  Good Bye!!!  ' + '|'.bgMagenta)
    console.log('-----------------'.bgMagenta + '\n')
    break
  } else if (userColumns < 3 || userRows < 3) {
    console.log('*** INPUT ERROR ***'.bgRed + '\n' + 'Input value of Columns and Rows should not be less than 3 units.'.bgRed)
  } else {
    // call ChessBoard() class
    var userBoard = ChessBoard(userColumns, userRows)

    // draw board
    console.log(userBoard)
    break
  }
}
