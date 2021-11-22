import java.util.concurrent.Semaphore;

public class TrafficController {

    private static Semaphore sem = new Semaphore(1,true);

    public void enterLeft() {
        try {
            this.sem.acquire();
        } catch (InterruptedException e) {
            System.out.println("Exception");
        }
    }
    public void enterRight() {
        try {
            this.sem.acquire();
        } catch (InterruptedException e) {
            System.out.println("Exception");
        }
    }
    public void leaveLeft() {
        this.sem.release();
    }
    public void leaveRight() {
        this.sem.release();
    }

}