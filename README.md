![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Terminal Games
- Terminal games is a python project that has a dashboard where you can select to play a variety of games, the current game available is Battleships but the code is left open to add new games with ease.

## Battleships
- Battleships is a game where you guess co-ordinates on a map, the objective is to sink the enemy ships before your own are sunk.
    - In the version I have created, you play against the computer. In it's current state the ships are visible on the enemy board this is mainly for testing purposes as it makes the game run quicker for the project testers.

## Live Deployment
- Terminal games is deployed through Heroku the live deployment is here: [Terminal-Games](https://terminal-games-a4b70cb979e5.herokuapp.com/)
- The repository for this project is on GitHub and is located here: [Terminal-Games-Repository](https://github.com/LiamEdwards931/Terminal-games.git)

## Contents
- [Terminal-Games](#terminal-games)
    - [BattleShips](#battleships)
- [Live-Deployment](#live-deployment)
- [User-Experience](#user-experience)
    - [Features](#features)
    - [Future_features](#future-features)
- [Testing](#testing)
    - [Bugs](#bugs)
    - [Commits](#commits)
- [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Cloning](#cloning-a-repository)



# User experience

- With the project terminal games, I am trying to envoke a positive user experience by giving them a simple landing page in which they can easily access the games they wish to play, by simply pressing the number for the game they want to play they can enjoy the game for example in battleships once this game is over, they can easily go back to the landing page to select another game if they wish too or from here they can simply exit the program.

- With the battleships game I wanted to create 2 boards so you could keep track of your own guesses but also to see where the computer was hitting too, to make the game feel a little bit more authentic.

## Features

This is the starting screen that players will expect when starting terminal games:

![startscreen](readmeimg/startscreen.png)

If the user selects option 0 they see this:

![Option-0](readmeimg/option0.png)

If the user selects option 1. Battleships they come to this screen:

![Option-1](readmeimg/option1.png)

From here the user can play the battleships game by guessing a grid location this, the computer then takes it's turn:

![Guess](readmeimg/guess.png)

Player and Computer guesses are tracked visually on the board, the previous guess was A6 represented by O and hits by an X:
- Computers guess on player board

![Guess-track-player](readmeimg/compguess.png)

- Players guess on computer board

![Guess-track-computer](readmeimg/playerguess.png)

When you beat the Computer at the game you get this message:

![win-screen](readmeimg/winscreen.png)

If player types 'yes' it resets the board with ships in new positions to play again
If the player types 'no' it takes you back to the Terminal Games home page where you can select a game, Battleships again if you like.

Terminal games has input validation - you can only select the options that are available and empty inputs are not allowed.

[home](#terminal-games)

### Future Features
- With the way that I have set the landing page up for terminal games, the future features will be to implement more games that can be easily accessed through the options on the run file.

[home](#terminal-games)

## Testing

- I have tested the terminal games project by: 
    - Running the game and checking each input works as it should.
    - Checking different possibilities in the input field to check my validation is working correctly.
    - Ran and completed the battleship game to ensure that the home screen is working again
    - This also included checking you can re-enter the game after it had been reset. 
    - Took the code line by line to check for any whitespace, indentation issues.
    - Played the game where the computer wins to ensure that it is registering correctly. 
    - Tested the visuals and breaks in the lines to give readability.

[home](#terminal-games)

### BUGS 
- Bug where if user types "no" to exit the game it repeatedly asks without breaking the loop. - fixed by calling the import at the top and the function with the option with the correct syntax. "battleships.battleships()"

- Bug where if user entered empty field it would cause an error - fixed this by wrapping the inputs and main game loop in a while loop looking for a correct validation

[home](#terminal-games)

### Commits 
- Several large commits whilst fixing issues, as I was deleting or rearranging a lot of code to try to get the code running the way that I needed it too.
I didn't commit the changes as I was doing it as the code wasn't behaving in the way that I was expecting it too and wished to commit only when it was working.

[home](#terminal-games)

## Deployment

### Heroku

This project is deployed with Heroku - the steps to deploy are as follows:
- Sign in and click "Create new app"

[Step1](readmeimg/herokustep1.png)

- Name your project and select you region:

[Step2](readmeimg/nametheapp.png)

- Add your buildpack with python going in first and then Node.js second:

[step3](readmeimg/importbuildpack.png)

- Go to deploy and connect your repository for your project using the GitHub Option

[step4](readmeimg/connecttogithub.png)

- Once you have connected deploy from main branch - choose "automatic updates if you want to update as you work on your project" if not press deploy at the bottom

[step5](readmeimg/laststep.png)


### Cloning a repository

1. On your GitHub repository navigate to your repository page.
2. Click on the green button with "CODE" written in it.
3. Go to the HTTPS and copy the URL by pressing the overlapping squares.
4. Open Git Bash.
5. Enter git clone followed by the copied URL.
6. Enter where you would like your repository to be saved too for your local file.
7. Press Enter to finalise the clone.

[home](#terminal-games)


