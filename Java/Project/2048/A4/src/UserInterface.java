/**
 * @file: GameController.java
 * @Author: Hyosik Moon - moonh8
 * @Date: April.7th, 2021
 * @Description: view module that displays the status of the game (I referred to the privous year's assignment4(Bill Song))
 */

package src;

public class UserInterface {

    private static UserInterface visual = null;

    /** 
     * @brief constructor
     */
    private UserInterface(){}

    /**
     * @brief public static method for obtaining a single instance
     * @return an UserInterface object
     */
    public static UserInterface getInstance(){
        if (visual == null)
            return visual = new UserInterface();
        return visual;
    }

    /**
     * @brief display a welcome message
     */
    public void printWelcomeMessage(){
        System.out.println("-------------------------------------------------");
        System.out.println("                 Welcome to 2048                 ");
        System.out.println("-------------------------------------------------");
    }

    /**
     * @brief display a prompt asking the user to select a game mode
     */
    public void printGameModePrompt(){
        System.out.println("Select Game Mode: [limited moves mode] or [limited time mode]?");
        System.out.println("Enter m for 2048 limited movements mode, ");
        System.out.println("Enter t for 600s limited time mode (e to exit)");
    }

    /**
     * @brief display a prompt asking the user to select a board size
     */
    public void printBoardSizePrompt(){
        System.out.println("");
        System.out.println("Select the board size (minimum size 2): ");
        System.out.println("Ex: 2, 3, 4, 5, 6, ... ");
    }

    /**
     * @brief display a direction asking the user to enter a direction
     */
    public void printDirectPrompt(){
        System.out.println("Enter direction: w(UP), s(Down), a(Left), d(Right)");
        System.out.println("Ex: w / s / a / d (e to exit)");
    }

    /**
     * @brief display a message to congratulate the achievement of the score 2048
     */
    public void printCongratulation(){
        System.out.println("Congratulation for acheving 2048 !!");
        System.out.println("Set a new record!");
    }

    /**
     * @brief display the game condition
     * @param message the current game condition such as left moves or time
     */
    public void printCondition(String message){
        System.out.print(message);
    }

    /**
     * @brief Display the board on the screen
     * @details print the game board
     * @param boardT the game board
     */
    public void printBoard(BoardT boardT){
        System.out.println(this.toString(boardT));
     }

    /**
     * @brief helper method for printBoard()
     * @details print the game board and game information 
     * @param boardT the game board
     * @return the game board and information 
     */
    public String toString(BoardT boardT) {
    int[][] grid = boardT.getGrid();
    int score = boardT.getScore();
    int GRID_SIZE = boardT.GRID_SIZE;
        StringBuilder outputString = new StringBuilder();
        outputString.append(String.format("Score: %d\n", score));
        for (int row = 0; row < GRID_SIZE; row++) {
            for (int column = 0; column < GRID_SIZE; column++)
                outputString.append(grid[row][column] == 0 ? "    -" :
                        String.format("%5d", grid[row][column]));
            outputString.append("\n");
        }
        return outputString.toString();
    }

    /**
     * @brief display an ending message after user choose to exit the game
     */
    public void printEndingMessage(){
        System.out.println("-------------------------------------------------");
        System.out.println("             Thank You For Playing !!!           ");
        System.out.println("-------------------------------------------------");
    }
}
