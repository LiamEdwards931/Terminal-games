# Testing detail
## On program start:
- Expected: On Terminal Game start user should have a welcome message and input field to declare option:
    - Testing - This was tested by running the program in terminal and in heroku
    - Result - The feature ran as expected and gave ther user an input field and welcome message.

- Expected: When a user enters the number 0, 1, 2 or 3 in the input field a new screen based on option is available
    - Testing - Tested input validation, made sure no other inputs other than the specified are allowed including blank inputs.
    - Result - No input other than 0,1,2 or 3 are permitted and shows error message when entered. When the correct input is entered, screen chosen activates.

## Battleships 'test' 'Option 1':
- Expected: Prints welcome message, and an input stating 'press enter to begin'
    - Testing - Went into this option on startup, went into a different option and came back into option 1, restarted a play on option1
    - Result - Feature performs as expected, and user sees the welcome and input through each time of playing. 

- Expected: Once player has pressed enter to play 2 boards print to the terminal player and computer
    - Testing - Ran through this on restart and exiting and re-entering the Game, showing the ships 'S' in different positions each time for both boards
    - Result - Board prints to the terminal each time on enter being input to begin.

- Expected: Player must input a column A-H this then asks for another input for the row
    - Testing - Entered columns outside of the scope such as G, input blank space, input number, input lowercase c
    - Result - input validaion works and will not accept the column outside of the scope of a-h but will convert any lowercase to upper.

- Expected: Player must input a row 1-8 this then registers a mark on the board showing the position the player has chose either an x or o
    - Testing - Entered text in the box, entered numbers outside of the scope and also entered a blank field
    - result- input validation works and will not accept rows outside of its specificed scope, integers only.

- Expected: Once a player has given a valid position on the grid the location input will have a visible marker O for miss X for hit.
    - Testing - Entered each column and Each row for game 1 from A1 - H8. repeated this on restarting the game and also going to home menu and re-entering game.
    - Result - Board re-prints with the updated guess in the appropriate rows and columns. using O for misses and X for hits.

- Expected: On each turn a message displays showing if you have hit or missed a ship, this also applying for the computers turn. 
    - Testing - Checked for appropriate comments on hits and misses on each turn. ensuring both are correctly displaying. 
    - Result - Messages display on each turn with the appropriate comment displaying if you have hit or missed a ship, the same applying to the computer.

- Expected: Once 4 ships have been hit the game will display the winning message and ask if you would like to play again with the options yes or no
    - Testing - Played through the game on first playthrough, on restart and also on exiting and re-entering the game.
    - Result - Each time the game ends the appropriate message comes through.

- Expected: On the game over options input yes or no, yes will restart the game and no will take you back to terminal games screen
    - Testing - Tested input validation for the yes or no, checked the appopriate action is taken on yes or no and also repeated on restarting the game and exiting and re-entering. 
    - Result - Each time the game is played whether first, restart, or exit and entering the game on a win displays the correct input, blank inputs are invalid and no options except yes or no will be accepted.

## Battleships main game

Any and all tests in the previous section were also performed in this code aswell, to re-read go [back](#battleships-test-option-1)

- Expected: Once the game has ended an input will display asking for your name to display your time it took you to win.
    - Testing - Tested input validation and if the input was correctly working for the player update and first run, restart run and exit and enter run.
    - Result - Blank inputs are not allowed, player name correctly updates on the win screen.

- Expected: Once the game has ended and a name has been input you will get a message saying how long it took you to win e.g "You won in 48 seconds"
    - Testing - Tested the game on first run, restart run and exit and enter run to ensure time was always being displayed on a playthrough.
    - Result - Time on a game win is correctly updating

- Expected: Once the game has ended and the user has entered a name the score will append to a file called leaderboard.txt that is viewable from the main menu
    - Testing - Went through the game twice to check appended entries, then exited played again and then restart the game and then checked the appended entries again.
    - Result - all entries that I had made were successfully pushed into the txt file and available to view in option 3. Battleship Leaderboard.


I have tested all of these entries as thoroughly as I could and believe I have not missed any of the features.

[Back_to_main_README](README.md)




