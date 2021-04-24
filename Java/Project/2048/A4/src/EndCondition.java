/**
 * @file: EndCondition.java
 * @Author: Hyosik Moon - moonh8
 * @Date: April.7th, 2021
 * @Description: generic interface for setting the game ending condition used in Strategy pattern (I referred to the privous year's assignment4(Bill Song))
 */

package src;

public interface EndCondition{

    // Declare the interface methods
    public boolean gameStatus(int moves);
    public String message(int moves);
}