package week2;

import java.util.Iterator;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/15/13
 * Time: 10:52 AM
 * To change this template use File | Settings | File Templates.
 */
public class FixedCapacityStack<Item> implements Iterable<Item> {

    public int capacity = 1; //original capacity 1 item, we dynamically resize it
    public Item[] items;
    public int current = 0;

    //TODO throw exception if poping from an empty stack
    //TODO about insertion of null items
    public FixedCapacityStack() {

        items = (Item[]) new Object[capacity];
    }

    public void push(Item item) {
        items[current] = item;
        current++;
        // now check if array is about filled in
        // if so create an array of twice the size
        if (current + 1 >= this.capacity) {
            //resize
            this.capacity = 2 * this.capacity;
            resize(this.capacity);

        }
    }


    private void resize(int newCapacity) {

        Item[] newItems = (Item[]) new Object[newCapacity];
        int i = 0;
        for (Item item : items) {
            if (i < newCapacity) {
                newItems[i] = item;
                i = i + 1;
            }
        }
        this.items = newItems;

    }

    public Item pop() {
        current--;
        Item value = items[current - 1];
        items[current - 1] = null;     //free memory, we no longer need it, avoid loitering
        // resize array when it is 1 quarter full

        if (!this.isEmpty() && this.current == items.length / 4) {
            resize(items.length / 2);
        }
        return value;
    }

    public boolean isEmpty() {
        return current == 0;
    }

    @Override
    public Iterator<Item> iterator() {
        return new ReverseArrayIteratorWrapper();
    }

    private class ReverseArrayIteratorWrapper implements Iterator<Item> {

        int i = items.length;

        @Override
        public boolean hasNext() {
            return i > 0;
        }

        @Override
        public Item next() {
            this.i--;
            return items[i];
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException("Remove is unsupported");
        }
    }
}
