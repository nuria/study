/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/20/13
 * Time: 7:12 AM
 * To change this template use File | Settings | File Templates.
 */
/**
 * Dequeue. A double-ended queue or deque (pronounced "deck") is a generalization
 * of a stack and a queue that supports inserting and removing items from either
 * the front or the back of the data structure.
 *
 */


import java.util.Iterator;
//import java.lang.StringBuffer;

/**
 * Implementation with a double linked list
 *
 * @param <Item>
 */

public class Deque<Item> implements Iterable<Item> {
    /**
     * construct an empty queue *
     */


    private Node first = null;

    private Node last = null;

    private int size = 0;

    public Deque() {

    }

    /**
     * is the queue empty *
     */
    public boolean isEmpty() {
        return this.first == null;
    }

    /**
     * return number of items in the queue *
     */
    public int size() {
        return this.size;
    }

    /**
     * insert the item at the front *
     */
    public void addFirst(Item item) {
        assertNotNull(item);
        this.size++;

        if (this.last == null) {
            //queue was empty, last and first are the same thing
            this.first = new Node(item);
            this.last = this.first;
        } else {
            Node priorFirst = this.first;
            Node newFirst = new Node(item, priorFirst);
            this.first = newFirst;
            priorFirst.prior = this.first;
        }
    }

    /**
     * insert the item at the end *
     */
    public void addLast(Item item) {
        assertNotNull(item);
        this.size++;
        if (this.last == null) {
            // empty queue
            this.last = new Node(item);
            this.first = this.last;
        } else {
            Node oldLast = this.last;
            Node newLast = new Node(item);
            oldLast.next = newLast;
            this.last = newLast;
            this.last.prior = oldLast;
        }

    }

    /**
     * delete and return the item at the front *
     */
    public Item removeFirst() {
        if (this.isEmpty()) {
            throw new java.util.NoSuchElementException("empty queue");
        }
        Node newFirst = this.first.next;
        Node oldFirst = this.first;

        if (this.first.equals(this.last)) {
            this.last = newFirst;
        }
        this.first = newFirst;

        if (this.first != null) {
            this.first.prior = null;
        }
        this.size--;
        return oldFirst.getItem();

    }

    /**
     * delete and return the item at the end
     * <p/>
     * Doing so without traversing the list means it has to be
     * double linked.
     * *
     */
    public Item removeLast() {

        if (this.isEmpty()) {
            throw new java.util.NoSuchElementException("empty queue");
        }

        Node oldLast = this.last;

        Node priorToLast = this.last.prior;

        if (this.first.equals(this.last)) {
            this.first = priorToLast;
        }
        this.last = priorToLast;
        if (last != null) {
            this.last.next = null;
        }
        this.size--;
        return oldLast.getItem();

    }

    /**
     *
     */
    private void assertNotNull(Item item) {
        if (item == null) {
            throw new java.lang.NullPointerException("no null items allowed");
        }
    }

    /**
     * return iterator over items from front to end *
     */
    public Iterator<Item> iterator() {

        return new IteratorItem();

    }


    /** private String toString() {
     StringBuffer sb = new StringBuffer();
     sb.append("[");
     Iterator<Item> it = this.iterator();

     while (it.hasNext()) {
     sb.append(" " + it.next().toString());
     }

     sb.append("]");
     return sb.toString();
     } **/


    /**
     * Note that the behaviour of the iterator is undefined if we modify the queue while iterating
     */
    private class IteratorItem implements Iterator<Item> {

        private Node current = null;


        public IteratorItem() {
            this.current = Deque.this.first;
        }

        @Override
        public boolean hasNext() {
            //System.out.println(this.current);
            return this.current != null;
        }

        /**
         * We update the  current pointer after we call next *
         */
        @Override
        public Item next() {
            if (this.current == null) {
                throw new java.util.NoSuchElementException(" No items to return");
            }
            Item item = this.current.getItem();
            this.current = this.current.next;

            return item;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException(" Not supported");
        }
    }

    private class Node {
        private Node next = null;
        private Item item;
        private Node prior = null;


        public Node(Item item) {
            this.item = item;
        }

        public Node(Item item, Node next) {
            this.item = item;
            this.next = next;

        }

        public Node(Item item, Node next, Node prior) {
            this.item = item;
            this.next = next;
            this.prior = prior;

        }

        public Item getItem() {
            return item;
        }

        public Node getNext() {
            return next;
        }

    }
}
