/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/20/13
 * Time: 7:12 AM
 * To change this template use File | Settings | File Templates.
 */

import java.util.Iterator;

/**
 * A randomized queue is similar to a stack or queue, except that the item removed is chosen uniformly at random from items in the data structure.
 * Create a generic data type RandomizedQueue that implements the following API:
 */
public class RandomizedQueue<Item> implements Iterable<Item> {


    private Item[] items;

    private int capacity = 1; //original capacity 1 item, we dynamically resize it

    private int current = 0;


    /**
     * construct an empty randomized queue  *
     */
    public RandomizedQueue() {
        items = (Item[]) new Object[capacity];
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

    /**
     * is the queue empty? *
     */
    public boolean isEmpty() {
        return this.current == 0;
    }

    /**
     * return the number of items on the queue *
     */
    public int size() {

        return this.current;
    }

    /**
     * add the item *
     */
    public void enqueue(Item item) {
        assertNotNull(item);
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

    /**
     * delete and return a random item *
     */
    public Item dequeue() {
        if (this.isEmpty()) {
            throw new java.util.NoSuchElementException("Empty queue");
        }

        int r;

        if (current == 1) {
            r = 0;
        } else {
            r = StdRandom.uniform(current);
        }

        //swap current-1 item with r item and return r item


        Item value = items[r];
        Item last = items[current - 1];
        //move last item to position 'r'
        items[r] = last;
        items[current - 1] = null;

        // make array smaller when it it is 1 quarter full, at the same time remove nulls
        // also if emptycount is 1/4 of array
        if (!this.isEmpty() && (this.current == items.length / 4)) {
            int newCapacity = items.length / 2;
            resize(newCapacity);
        }
        current--;
        return value;

    }


    /**
     * return (but do not delete) a random item *
     */
    public Item sample() {
        if (this.isEmpty()) {
            throw new java.util.NoSuchElementException("Queue is empty");
        }

        int r = StdRandom.uniform(current);
        return items[r];
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
     * /** return an independent iterator over items in random order *
     */
    public Iterator<Item> iterator() {
        return new RandomizedIterator();
    }


    private class RandomizedIterator implements Iterator<Item> {

        private int current;
        private Item[] items;


        public RandomizedIterator() {
            items = RandomizedQueue.this.items;
            StdRandom.shuffle(items);
            this.current = RandomizedQueue.this.size() - 1;
        }

        @Override
        public boolean hasNext() {
            return this.current >= 0;
        }

        @Override
        public Item next() {
            if (this.current < 0) {
                throw new java.util.NoSuchElementException(" No items to return");
            }

            Item next = items[current];
            this.current--;
            return next;

        }

        @Override
        public void remove() {

            throw new UnsupportedOperationException(" Not supported");
        }
    }
}

