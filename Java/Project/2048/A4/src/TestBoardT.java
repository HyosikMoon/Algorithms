/**
 * @file: TestBoardT.java
 * @Author: Hyosik Moon, moonh8(MacID)
 * @Date: Apr 15, 2021
 * @Description: Tests the public interfaces of BoardT
 */

package src;

import org.junit.*;
import java.util.*;
import static org.junit.Assert.*;

public class TestBoardT{

    private BoardT board;

    @Before
    public void setUp(){
        board = new BoardT(4, new Random());
    }

    @After
    public void tearDown(){
        this.board = null;
    }

    @Test
    public void testGetStatus(){
        assertTrue(board.getStatus());
    }

    @Test
    public void testSetEndCondition(){
        board.setEndCondition(new EndByMoves());
        assertEquals(board.getMessage(),"Number of moves left: 2048");
    }

    @Test
    public void testSetEndCondition2(){
        board.setEndCondition(new EndByTime());
        assertEquals(board.getMessage(),"Time left(sec): 600");
    }

    // @Test 
    // public void testRemove(){
    //     board1.setEndCondition(new EndByMoves());
    //     ArrayList<String> input = new ArrayList<String>(Arrays.asList("06", "07"));
    //     board1.remove(input);
    //     assertEquals(board1.getMessage(),"Target: # of Red Dots left: 5 , # of Orange Dots left: 3\n Number of moves left: 9");
    // }

    // @Test (expected=IllegalArgumentException.class)
    // public void testRemoveExpection(){
    //     input = new ArrayList<String>(Arrays.asList("16", "25", "26", "27"));
    //     board1.remove(input);
    // }

    // @Test (expected=IllegalArgumentException.class)
    // public void testRemoveExpection1(){
    //     input = new ArrayList<String>(Arrays.asList("86", "25", "26", "27"));
    //     board1.remove(input);
    // }
}