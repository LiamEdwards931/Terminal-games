# BUGS 
- Bug where if user types "no" to exit the game it repeatedly asks without breaking the loop. - fixed this by rather than calling the function in the main home screen, importing it when a user selects to play the game in the terminal games home screen as this was causing the game to continuously loop.

- Bug where if user entered empty field it would cause an error - fixed this by wrapping the inputs and main game loop in a while loop looking for a correct validation
