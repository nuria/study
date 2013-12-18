package week2; /**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/15/13
 * Time: 10:08 AM
 * To change this template use File | Settings | File Templates.
 */

/**
 * First in first out
 */
public class LinkedQueueOfStrings {


    private Node first = null;
    private Node last = null;

    /**
     * inner class
     */
    private class Node {
        String item;
        Node next;

        public Node(String item) {
            this.item = item;
            this.next = null;
        }
    }

    /**
     * enqueue at the end *
     */
    public void enque(String item) {
        Node node = new Node(item);
        Node prior = this.last;
        prior.next = node;
        this.last = node;
        //TODO queue size 1
    }

    /**
     * Return first item
     *
     * @return
     */
    public String dequeue() {
        Node tmp = this.first;
        this.first = tmp.next;
        tmp.next = null;

        return tmp.item;
    }

    public boolean isEmpty() {
        return first == null; //nice, check for initialization condition
    }
}
