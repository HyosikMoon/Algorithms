/**
 * @file: AllTests.java
 * @Author: Hyosik Moon, moonh8(MacID)
 * @Date: Apr 15, 2021
 * @Description: Tests the public interfaces of BoardT, EndByTime, and EndByMoves
 */

package src;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
   TestBoardT.class,	
   TestEndByMoves.class,
   TestEndByTime.class,
})

public class AllTests
{
}
