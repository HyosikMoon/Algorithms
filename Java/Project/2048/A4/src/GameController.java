/**
 * @file: GameController.java
 * @Author: Hyosik Moon - moonh8
 * @Date: April.7th, 2021
 * @Description: controller module that handles inputs and links model and view module (I referred to the privous year's assignment4(Bill Song))
 */

package src;

// Import java libraries
import java.util.Random;
import java.util.Scanner;

public class GameController{

    // Define state variables
    private BoardT model;
    private UserInterface view;
    private static GameController controller = null;

    //Define environment variable
    private Scanner keyboard = new Scanner(System.in);

    /**
     * @brief constructor
     * @param model - model module (BoardT)
     * @param view - view module (UseInterface)
     */
    private GameController(BoardT model, UserInterface view){
        this.model = model;
        this.view = view;
    }

    /**
     * @brief public static method for obtaining a single instance
     * @return the single GameController object
     */
    public static GameController getInstance(BoardT model, UserInterface view) 
    { 
        if (controller == null) 
            controller = new GameController(model, view); 
        return controller; 
    } 

    /**
     * @brief initialize the game
     */
    public void initializeGame(int boardSize){
        this.model = new BoardT(boardSize, new Random());
    }

    /**
     * @brief takes the input from the user through keyboard
     * @return the input
     * @throws IllegalArgumentException Invalid Input
     */
    public String readGameModeInput(){
        String gameMode;
        gameMode = keyboard.nextLine();
        gameMode = gameMode.toLowerCase();
        try{
            if(!gameMode.equals("m") && !gameMode.equals("t") && !gameMode.equals("e"))
                throw new IllegalArgumentException();
        }
        catch (IllegalArgumentException e) {
            System.out.println("Invalid Input");
        }
        return gameMode;
    }

    /**
     * @brief takes the input from the user through keyboard
     * @return the input
     * @throws IllegalArgumentException Invalid Input
     */
    public Integer readBoardSize(){
        int boardsize;
        boardsize = keyboard.nextInt();
        try{
            if(boardsize <= 0)
                throw new IllegalArgumentException();
        }
        catch (IllegalArgumentException e) {
            System.out.println("Invalid Input");
            
        }
        return boardsize;
    }


    /**
     * @brief get directions input from the user
     * @return the direction(enum) corresponding the input value
     * @throws IllegalArgumentException (Input is neither a direction nor e)
     */
    public Direction readDirection(String input){
        Direction direction = Direction.DOWN;
        try {
            if((!input.equals("w") && !input.equals("s") && !input.equals("a") &&!input.equals("d") && !input.equals("e")))
                throw new IllegalArgumentException();
        }
        catch (IllegalArgumentException e) {
            System.out.println("Invalid Input");
        }
        if (input.equals("w")) 
            direction = Direction.UP;
        else if (input.equals("s"))
            direction = Direction.DOWN;
        else if (input.equals("a"))
            direction = Direction.LEFT;
        else if (input.equals("d"))
            direction = Direction.RIGHT;
        return direction;
    }

    /**
     * @brief get the state of the board
     * @return return the game status from the board
     */
    public boolean getStatus(){
        return this.model.getStatus();
    }

    /**
     * @brief Sets the game ending condtion
     * @param input the game mode chosen by the user
     */
    public void setGameMode(String input) {
        if (input.equals("m"))
            model.setEndCondition(new EndByMoves());
        else if (input.equals("t")) {
            EndByTime cond = new EndByTime();
            model.setEndCondition(cond);
            cond.startCountDown();
        }
    }

    /**
     * @brief calculate the elmented based on the input direction
     * @param dirction the direction chosen by a user
     */
    public void setCalculation(Direction direction){
        model.move(direction);
    }

    /**
     * @brief add random tiles after calculation
     * @param direction the direction chosen by a user
     */
    public void replaceCalculated(Direction direction) {
        model.addRandomTile(direction);
    }

    /**
     * @brief updates the view module to display a welcome message
     */
    public void displayWelcomeMessage(){
        view.printWelcomeMessage();
    }

    /**
     * @brief updates the view module to display the board
     */
    public void displayBoard(){
        view.printBoard(model);
    }

    /**
     * @brief updates the view module to display the game mode
     */
    public void displayCondition(){
        view.printCondition(model.getMessage());
    }

    /**
     * @brief updates the view module to display a ending message
     */
    public void displayEnding(){
        view.printEndingMessage();
    }

    /**
     * @brief updates the view module to display a prompt asking the user to select a game mode
     */
    public void displayGameModePrompt(){
        view.printGameModePrompt();
    }

    /**
     * @brief updates the view module to display a prompt asking the user to select a game size
     */
    public void displayBoardSizePrompt(){
        view.printBoardSizePrompt();
    }
   
    /**
     * @brief updates the view module to display a prompt asking the user to enter an direction
     */
    public void displayDirectPrompt(){
        view.printDirectPrompt();
    }

    /**
     * @brief updates the view module to display a congratulation message
     */
    public void displayCongratulation(){
        view.printCongratulation();
    }

    /**
     * @brief runs the game
     */
    public void runGame(){
        String input = "";
        int boardsize = 0;
        String gameMode = "";
        displayWelcomeMessage();

        displayBoardSizePrompt();
        boardsize = readBoardSize();
        initializeGame(boardsize);
        keyboard.nextLine();

        do {
            displayGameModePrompt();
            gameMode = readGameModeInput();
            setGameMode(gameMode);
        } while (!gameMode.equals("m") && !gameMode.equals("t") && !gameMode.equals("e"));

        while (getStatus() == true && !(input.equals("e")) && !(gameMode.equals("e")) && !model.isGameOver() && model.getgameStatus()) {
            System.out.println("");
            displayCondition();
            System.out.println("");
            displayBoard();
            displayDirectPrompt();
            input = keyboard.nextLine();
            if (input.equals("e")) {
                break;
            }
            try {
                if((!input.equals("w") && !input.equals("s") && !input.equals("a") &&!input.equals("d") && !input.equals("e")))
                    throw new IllegalArgumentException();
                Direction direction = readDirection(input);
                setCalculation(direction);
                replaceCalculated(direction);
            }
            catch (IllegalArgumentException e) {
                System.out.println("Invalid Input");
            }
            if (model.getScore() == 2048) {
                displayCongratulation();
            }
        }

        displayBoard();
        displayEnding();
        System.exit(0);
    }
}