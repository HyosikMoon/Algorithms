/**
 * @file: Demo.java
 * @Author: Hyosik Moon - moonh8
 * @Date: April.7th, 2021
 * @Description: Runs the game (I referred to the privous year's assignment4(Bill Song))
 */

package src;

import java.util.Random;

public class Demo
{
   public static void main(String[] args) {
      UserInterface UI = UserInterface.getInstance();
      GameController game = GameController.getInstance(new BoardT(4, new Random()), UI);
      game.runGame();
  }
}