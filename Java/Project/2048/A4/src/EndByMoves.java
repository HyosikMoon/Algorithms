/**
 * @file: EndByMoves.java
 * @Author: Hyosik Moon - moonh8
 * @Date: April.7th, 2021
 * @Description: module implementing EndCondition interface (I referred to the privous year's assignment4(Bill Song))
 */

package src;

public class EndByMoves implements EndCondition{

    // Declare state variables
    private final int maxMoves;

    /**
     * @brief constructor
     */
    public EndByMoves(){
        this.maxMoves = 2048;
    }

    /**
     * @brief changes the game status
     * @param moves - the number of moves used already
     * @return True or False states
     */
    @Override
    public boolean gameStatus(int moves){
        return !((maxMoves - moves) <= 0);
    }

    /**
     * @brief the string representing the game objective and amount of moves and dots left until game terminates
     * @param moves - the number of moves used already
     * @return message for printing
     */
    @Override
    public String message(int moves){
        return String.format("Number of moves left: %d", (maxMoves - moves));
    }


}
