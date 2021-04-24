/**
 * @file: EndByTime.java
 * @Author: Hyosik Moon - moonh8
 * @Date: April.7th, 2021
 * @Description: module implementing EndCondition interface (I referred to the privous year's assignment4(Bill Song))
 */

package src;

public class EndByTime implements EndCondition{


    private int timeLeft;
    private Thread t;

    public EndByTime(){
        this.timeLeft = 600;
        t = new Thread(new StartTimer(this));
    }

    class StartTimer implements Runnable {
        private EndByTime t;
        public StartTimer(EndByTime timer){
            this.t = timer;
        }
        public void run() {
            for (int i = 600; i >= 0; i--) {
                t.setTime(i);
                try {
                    // thread to sleep for 1000 milliseconds
                    Thread.sleep(1000);
                } catch (Exception e) {
                    System.out.println(e);
                }
            }
            System.out.println();
            System.out.println("Time Up. Restart the game.");
        }
    }

    /**
     * @brief changes the game status
     * @param num - the number of dots eliminated during this one move
     * @param moves - the number of moves used already
     */
    @Override
    public boolean gameStatus(int moves){
        return !((timeLeft) <= 0);
    }

    /**
     * @brief the string representing the game objective and amount of dots and time left until game terminates
     * @param moves - the number of moves used already
     */
    @Override
    public String message(int moves){
        return String.format("Time left(sec): %d", timeLeft);
    }

    /**
     * @brief sets the time for the count down clock
     * @param time - the preset time
     */
    public void setTime(int time){
        this.timeLeft = time;
    }

    public void startCountDown(){
        t.start();
    }
}