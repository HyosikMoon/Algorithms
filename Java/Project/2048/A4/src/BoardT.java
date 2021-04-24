/**
 * @file: BoardT.java
 * @Author: Hyosik Moon - moonh8
 * @Date: April.7th, 2021
 * @Description: a model module for storing the state and status of the game
 * I referred to the website codes: https://github.com/gn03249822/Game-2048/blob/master/Board.java  
 */

package src;

import java.util.*;

public class BoardT {
   public final int NUM_START_TILES = 2;
   public final int TWO_PROBABILITY = 90;
   public final int GRID_SIZE;
   private final Random random;
   private static boolean moved = false;
   private boolean status;
   private EndCondition condition;
   private int[][] grid;
   private int score;
   private int moves;

   /**
    * @brief  Constructs a fresh board with random tiles
    * @details Creates and operates the board for the 2048 games
    * @param boardSize the size of the grid
    * @param random a random(number) generator
    */
   public BoardT(int boardSize, Random random) {
      this.random =random ; 
      this.GRID_SIZE = boardSize;
      this.grid=new int[boardSize][boardSize];
      this.score=0;
      this.moves = 0;
      this.status = true;
      for (int i=0;i<NUM_START_TILES;i++) {
         this.addRandomTile();
      }
   }

   /**
    * @brief the status of the game(board)
    * @return board status
    */
   public boolean getStatus(){
      return this.status;
   }

   /**
   * @brief sets the game ending condition for the game
   * @param condition the game mode
   */
   public void setEndCondition(EndCondition condition){
      this.condition = condition;
   }

   /**
   * @brief get the end condition information
   * @return the current information of the game mode
   */
   public String getMessage(){
      return condition.message(this.moves);
   }

   /**
   * @brief get the end condition status
   * @return the current state of the game
   */
   public boolean getgameStatus(){
      return condition.gameStatus(this.moves);
   }

   /**
    * @brief addRandomTile after board calculation
    * @details initialize the board with random tiles
    */
   public void addRandomTile() {
      //first count the number of available tiles
      int count=0;
      for (int row=0; row<GRID_SIZE;row++) {
         for (int col=0;col<GRID_SIZE;col++) {
            if (this.grid[row][col]==0) {
               count++;
            }
         }
      }
      //after checking all the available tiles,if count=0, exit the method
      if (count==0) {
         return;
      }
      //get a random int called location (0~count-1)
      int location=this.random.nextInt(count);
      //get a random int called value (0~99)
      int value=this.random.nextInt(100);
      //keep track of the number of the empty spaces by numEmp,
      //starting from -1 b/c we number the first empty space as 0
      int numEmp=-1;
      for (int row=0; row<GRID_SIZE;row++) {
         for (int col=0;col<GRID_SIZE;col++) {
            if (this.grid[row][col]==0) { 
               numEmp++;
            }
            //if the location value equals to the numbering of the empty 
            //space,add a random tile
            if (numEmp==location) { //place a 2
               if (value<TWO_PROBABILITY) {
                  this.grid[row][col]=2;
                  numEmp++;
               } else {//place a 4 
                  this.grid[row][col]=4;
                  numEmp++;
               }
            }
         }
      }
   }

   /**
    * @brief addRandomTile after board calculation
    * @details adds a random tile (of value 2 or 4) to a random empty space on the board
    * @param direction used for determining if addition is need or not
    */
   public void addRandomTile(Direction direction) {
      //first count the number of available tiles
      int vacant=0;
      for (int row=0; row<GRID_SIZE;row++) {
         for (int col=0;col<GRID_SIZE;col++) {
            if (this.grid[row][col]==0) {
               vacant++;
            }
         }
      }
      //after checking all the available tiles,if count=0, exit the method
      if (vacant == 0) {
         return;
      }
      //get a random int called value (0~99)
      int value = this.random.nextInt(100);
      //keep track of the number of the empty spaces by numEmp,
      //starting from -1 b/c we number the first empty space as 0
      if (((direction.equals(Direction.UP) && this.canMoveDown()) || 
      (direction.equals(Direction.DOWN) && this.canMoveUp()) || 
      (direction.equals(Direction.LEFT) && this.canMoveRight()) || 
      (direction.equals(Direction.RIGHT) && this.canMoveLeft())) && moved) {
         boolean filled = false;
         for (int row=0; row<GRID_SIZE; row++) {
            for (int col=0; col<GRID_SIZE; col++) {
               if (this.grid[row][col] == 0 && !filled) { 
                  if (value<TWO_PROBABILITY) { 
                     //place a 2
                     if (((double)vacant / (double)(GRID_SIZE * GRID_SIZE)) >= 0.3) {
                        //There are many vacant places, so fill it randomly
                        if (GRID_SIZE >= 6) {
                           int count = GRID_SIZE - 4;
                           while (count > 0) {
                              int randrow = this.random.nextInt(GRID_SIZE);
                              int randcol = this.random.nextInt(GRID_SIZE);
                              if (this.grid[randrow][randcol] == 0) {
                                 this.grid[randrow][randcol] = 2;
                                 filled = true;
                                 count--;
                              }
                           }
                        } else {
                           while (true) {
                              int randrow = this.random.nextInt(GRID_SIZE);
                              int randcol = this.random.nextInt(GRID_SIZE);
                              if (this.grid[randrow][randcol] == 0) {
                                 this.grid[randrow][randcol] = 2;
                                 filled = true;
                                 break;
                              }
                           }
                        }
                     } else {
                        // few #vacant place
                        this.grid[row][col] = 2;
                        filled = true;
                     }
                  } else {
                     //place a 4 
                     this.grid[row][col] = 4;
                     filled = true;
                  }
               }
            }
         }
      } else {
         return;
      }
   }

   /**
    * @brief helper method for move() method
    * @details consists of three parts, move empty tiles / merge tiles / move empty tiles
    */
   private void moveLeft() {
      //use count to move the tiles to the left one by one
      for (int row=0; row<GRID_SIZE; row++){
         int count=0;
         for (int col=0; col<GRID_SIZE; col++) {
            if (this.grid[row][col]!=0) {
               this.grid[row][0+count]=this.grid[row][col];
               //Empty the original tile position once tile is moved 
               if (0+count!=col) {
                  this.grid[row][col]=0;
                  moved = true;
               }
               count++;
            }
         }
      }
      //after move tiles to empty space, add same and adjacent two tiles
      for (int row=0; row<GRID_SIZE; row++) {
         for (int col=0;col<GRID_SIZE-1;col++) {
            if (this.grid[row][col]==this.grid[row][col+1]) {
               // Consecutive 0s considered as not moved
               if (this.grid[row][col] != 0) { 
                  moved = true;
               }
               //add the two tiles with the same value
               this.grid[row][col]+=this.grid[row][col+1];
               this.grid[row][col+1]=0;
               //update the score ONCE!
               int sum=this.grid[row][col];
               this.score+=sum;
               // break; (Add only left most tiles)
            }
         }
      }
      //after adding two tiles, repeat the first for loop
      //in this method to move all the tiles to the left side
      for (int row=0; row<GRID_SIZE; row++) {
         int count=0;
         for (int col=0;col<GRID_SIZE;col++) {
            if (this.grid[row][col]!=0) {
               this.grid[row][0+count]=this.grid[row][col];
               //Empty the original tile position once tile is moved 
               if (0+count!=col) {
                  this.grid[row][col]=0;
                  moved = true;
               }
               count++;
            }
         }
      }
   }

   /**
    * @brief helper method for move() method
    * @details consists of three parts, move empty tiles / merge tiles / move empty tiles
    */
   private void moveRight() {
      //use count to move the tiles to the right one by one
      for (int row=0; row<GRID_SIZE; row++) {
         int count=0;
         for (int col=GRID_SIZE-1;col>=0;col--) {
            if (this.grid[row][col]!=0) {
               this.grid[row][GRID_SIZE-1-count]=this.grid[row][col];
               //empty the original tile position after tile is moved
               if (GRID_SIZE-1-count!=col) {
                  this.grid[row][col]=0;
                  moved = true;
               }
               count++;
            }
         }
      }
      //after move tiles to empty space, add same and adjacent two tiles
      for (int row=0; row<GRID_SIZE; row++) {
         for (int col=GRID_SIZE-1;col>0;col--) {
            if (this.grid[row][col]==this.grid[row][col-1]) {
               // Consecutive 0s considered as not moved
               if (this.grid[row][col] != 0) { 
                  moved = true;
               }
               //add the two tiles with the same value
               this.grid[row][col]+=this.grid[row][col-1];
               this.grid[row][col-1]=0;
               //update the score ONCE!
               int sum=this.grid[row][col];
               this.score+=sum;
               // break;
            }
         }
      }
      //after adding two tiles, repeat the same first for loop
      //in this method to move all the tiles to the right side
      for (int row=0; row<GRID_SIZE; row++) {
         int count=0;
         for (int col=GRID_SIZE-1; col>=0; col--) {
            if (this.grid[row][col]!=0) {
               this.grid[row][GRID_SIZE-1-count]=this.grid[row][col];
               if (GRID_SIZE-1-count!=col) {
                  this.grid[row][col]=0;
                  moved = true;
               }
               count++;
            }
         }
      }
   }

   /**
    * @brief helper method for move() method
    * @details consists of three parts, move empty tiles / merge tiles / move empty tiles
    */
   private void moveUp() {
      //use count to move the tiles to the top one by one
      for (int col=0; col<GRID_SIZE; col++) {
         int count=0;
         for (int row=0; row<GRID_SIZE; row++) {
            if (this.grid[row][col] != 0) {
               this.grid[0+count][col]=this.grid[row][col];
               //empty the original tile position after tile is moved
               if (0+count != row) {
                  this.grid[row][col]=0;
                  moved = true;
               }
               count++;
            }
         }
      }
      //after move tiles to empty space, add same and adjacent two tiles
      for (int col=0; col<GRID_SIZE; col++) {
         for (int row=0;row<GRID_SIZE-1;row++) {
            if (this.grid[row][col] == this.grid[row+1][col]) {
               // Consecutive 0s considered as not moved
               if (this.grid[row][col] != 0) { 
                  moved = true;
               }
               //add the two tiles with the same value
               this.grid[row][col] += this.grid[row+1][col];
               this.grid[row+1][col] = 0;
               //update the score ONCE!
               int sum=this.grid[row][col];
               this.score += sum;
               // break;
            }
         }
      }
      //after adding two tiles, repeat the same first for loop
      //in this method to move all the tiles to the top
      for (int col=0; col<GRID_SIZE; col++) {
         int count=0;
         for (int row=0; row<GRID_SIZE; row++) {
            if(this.grid[row][col] != 0) {
               this.grid[0+count][col] = this.grid[row][col];
               //empty the original tile position after tile is moved
               if(0+count != row) {
                  this.grid[row][col] = 0;
                  moved = true;
               }
               count++;
            }
         }
      }
   }

   /**
    * @brief helper method for move() method
    * @details consists of three parts, move empty tiles / merge tiles / move empty tiles
    */
   private void moveDown() {
      //use count to move the tiles to the bottom one by one
      for (int col=0; col<GRID_SIZE; col++) {
         int count=0;
         for (int row=GRID_SIZE-1; row>=0; row--) {
            if (this.grid[row][col] != 0) {
               this.grid[GRID_SIZE-1-count][col] = this.grid[row][col];
               //empty the original tile position after tile is moved
               if (GRID_SIZE-1-count != row) {
                  this.grid[row][col]=0;
                  moved = true;
               }
               count++;
            }
         }
      }
      //after move tiles to empty space, add same and adjacent two tiles
      for (int col=0; col<GRID_SIZE; col++) {
         for (int row=GRID_SIZE-1; row>0; row--) {
            if (this.grid[row][col] == this.grid[row-1][col]) {
               // Consecutive 0s considered as not moved
               if (this.grid[row][col] != 0) { 
                  moved = true;
               }
               //add the two tiles with the same value
               this.grid[row][col]+=this.grid[row-1][col];
               this.grid[row-1][col]=0;
               //update the score ONCE!
               int sum=this.grid[row][col];
               this.score += sum;
               // break;
            }
         }
      }
      //after adding two tiles, repeat the same first for loop
      //in this method to move all the tiles to the bottom
      for (int col=0; col<GRID_SIZE; col++) {
         int count=0;
         for (int row=GRID_SIZE-1; row>=0; row--) {
            if (this.grid[row][col]!=0) {
               this.grid[GRID_SIZE-1-count][col]=this.grid[row][col];
               //empty the original tile position after tile is moved
               if (GRID_SIZE-1-count != row) {
                  this.grid[row][col]=0;
                  moved = true;
               }
               count++;
            }
         }
      }
   }

   /**
    * @brief performs a move operation
    * @details consists of three parts, move empty tiles / merge tiles / move empty tiles
    * @param direction the input direction by the user
    * @return return true if the move is successful otherwise, return false
    */
   public boolean move(Direction direction) {
      moved = false;
      //check the input direction enums and perform the move operation
      if (direction.equals(Direction.LEFT)) {
         this.moveLeft();
         moves++;
         return true;
      }
      if (direction.equals(Direction.RIGHT)) {
         this.moveRight();
         moves++;
         return true;
      }
      if (direction.equals(Direction.UP)) {
         this.moveUp();
         moves++;
         return true;
      }
      if(direction.equals(Direction.DOWN)) {
         this.moveDown();
         moves++;
         return true;
      }
      //return false if the move is not successful
      return false;
   }


   /**
    * @brief check to see if we have a game over
    * @return return true if there is no valid move left, and end the game
    */
   public boolean isGameOver() {
      //check if there is no long any valid move left, then the game is over.
      if (!this.canMoveLeft() && !this.canMoveRight()
          && !this.canMoveUp() && !this.canMoveDown()) {
               return true;
      }
      //return false when the game continues
      return false;
   }

   /**
    * @brief helper method for the canMove() method
    * @return return true if the the board can move left
    */
   private boolean canMoveLeft() {
      for (int row=0;row<GRID_SIZE;row++) {
         //check if there is zero neighboring a nonzero in the grid,if so,
         //the tiles can
         //move to the left; or if they are two tiles with the same value, it
         //can also move to the left
         for (int col=0;col<GRID_SIZE-1;col++) {
            if (this.grid[row][col] == 0 && this.grid[row][col+1] != 0) {
               return true;
            }
            if ( this.grid[row][col] != 0 && 
            this.grid[row][col] == this.grid[row][col+1]) {
               return true;
            }
         }
      }
      return false;
   }

   /**
    * @brief helper method for the canMove() method
    * @return return true if the the board can move right
    */
   private boolean canMoveRight(){
      for (int row=0;row<GRID_SIZE;row++) {
         //check if there is zero neighboring a nonzero in the grid,if so,
         //the tiles can
         //move to the right; or if they are two tiles with the same value, it
         //can also move to the right
         for (int col=GRID_SIZE-1;col>0;col--) {
               if (this.grid[row][col]==0&&this.grid[row][col-1]!=0) {
                  return true;
               }
               if (this.grid[row][col]!=0&&this.grid[row][col] == 
                  this.grid[row][col-1]) {
                  return true;
               }
            }
      }
      return false; 
   }

   /**
    * @brief helper method for the canMove() method
    * @return return true if the the board can move up
    */
   private boolean canMoveUp() {
      for (int col=0;col<GRID_SIZE;col++) {
         //check if there is zero neighboring a nonzero in the grid,if so,
         //the tiles can move up; 
         //or if they are two tiles with the same value, it can also move up
         for (int row=0;row<GRID_SIZE-1;row++) {
            if (this.grid[row][col]==0&&this.grid[row+1][col]!=0) {
               return true;
            }
            if (this.grid[row][col]!=0&&this.grid[row][col] ==
               this.grid[row+1][col]) {
               return true;
            }
         }

      }
      return false;
   }

   /**
    * @brief helper method for the canMove() method
    * @return return true if the the board can move down
    */
   private boolean canMoveDown() {
      for (int col=0;col<GRID_SIZE;col++) {
         //check if there is zero neighboring a nonzero in the grid,if so,
         //the tiles can
         //move down; or if they are two tiles with the same value, it
         //can also move down
         for (int row=GRID_SIZE-1;row>0;row--) {
               if (this.grid[row][col] == 0 && this.grid[row-1][col] != 0) {
                  return true;
               }
               if (this.grid[row][col] != 0 && this.grid[row][col]
                     == this.grid[row-1][col]) {
                  return true;
               }
         }
      }
      return false;
   }

   /**
    * @brief determine if we can move in a given direction
    * @param direction the input direction by the user
    * @return return true if the the board can move in the input direction
    */
   public boolean canMove(Direction direction) {
      //check if the board can move in the passed in direction
      if (direction.equals(Direction.LEFT) && this.canMoveLeft()) {
         return true;
      }
      if (direction.equals(Direction.RIGHT) && this.canMoveRight()) {
         return true;
      }
      if (direction.equals(Direction.UP) && this.canMoveUp()) {
         return true;
      }
      if (direction.equals(Direction.DOWN) && this.canMoveDown()) {
         return true;
      }
      //otherwise,return false(the board cannot move)
      return false;
   }

   /**
    * @brief get the board
    * @return  return the current board
    */
   public int[][] getGrid() {
      return grid;
   }

   /**
    * @brief get the current score of the game
    * @return return the current score
    */
   public int getScore() {
      return score;
   }
}