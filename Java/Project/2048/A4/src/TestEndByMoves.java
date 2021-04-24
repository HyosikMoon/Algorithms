/**
 * @file: TestBoardT.java
 * @Author: Hyosik Moon, moonh8(MacID)
 * @Date: Apr 15, 2021
 * @Description: Tests the public interfaces of EndByMoves
 */

package src;

import org.junit.*;
import java.util.*;
import static org.junit.Assert.*;

public class TestEndByMoves{

    private EndByMoves cond;

    @Before
    public void setup(){
        cond = new EndByMoves();
    }

    @After 
    public void tearDown(){
        cond = null;
    }

    @Test 
    public void testGameStatus(){
        assertTrue(cond.gameStatus(0));
    }

    @Test 
    public void testGetString(){
        assertEquals(cond.message(0),"Number of moves left: 2048");
    }
}