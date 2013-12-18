package week2; /**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/15/13
 * Time: 10:08 AM
 * To change this template use File | Settings | File Templates.
 */

/**
 * Last in first out
 */

import java.util.Iterator;

public class Stack<Item> implements Iterable<Item> {


    private Node first = null;

    @Override
    public Iterator<Item> iterator() {
        return new IteratorItem();
    }

    /**
     * inner class
     */
    private class Node {
        Item item;
        Node next;

        public Node(Item item) {
            this.item = item;
        }

        public Item getItem() {
            return this.item;
        }
    }

    public void push(Item item) {
        Node node = new Node(item);
        node.next = this.first;
        this.first = node;
    }

    public Item pop() {
        Node tmp = this.first;
        this.first = tmp.next;
        tmp.next = null;

        return tmp.item;
    }

    public boolean isEmpty() {
        return first == null; //nice, check for initialization condition
    }


    class IteratorItem implements Iterator<Item> {

        private Node current;

        public IteratorItem() {
            this.current = Stack.this.first;
        }

        @Override
        public boolean hasNext() {
            return this.current.next != null;
        }

        @Override
        public Item next() {

            this.current = this.current.next;
            Item nextItem = this.current.getItem();
            return nextItem;

        }

        @Override
        public void remove() {
            //To change body of implemented methods use File | Settings | File Templates.
            //do nothing
            throw new UnsupportedOperationException("Remove is unsupported");
        }
    }
}
