import org.testng.annotations.*;
import org.testng.annotations.Test;
import junit.framework.Assert;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/22/13
 * Time: 12:08 AM
 * To change this template use File | Settings | File Templates.
 */


public class RandomizedQueueTest {


    @org.testng.annotations.Test(expectedExceptions = NoSuchElementException.class)

    public void testIsEmpty() throws Exception {

        RandomizedQueue<Integer> q = new RandomizedQueue();
        Assert.assertTrue(q.isEmpty());
        q.enqueue(1);
        Assert.assertFalse(q.isEmpty());
        Assert.assertTrue(q.size() == 1);
        q.dequeue();
        Assert.assertTrue(q.isEmpty());
        q.sample();
    }


    @Test
    public void testEnqueue() throws Exception {

        RandomizedQueue<Integer> q = new RandomizedQueue();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        Assert.assertFalse(q.isEmpty());
        Assert.assertTrue(q.size() == 3);
        q.dequeue();
        q.dequeue();
        q.dequeue();
        Assert.assertTrue(q.isEmpty());

    }


    @Test
    public void testIterator() {
        RandomizedQueue<Integer> q = new RandomizedQueue();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        Iterator<Integer> it = q.iterator();
        Assert.assertTrue(it.hasNext());
        it.next();
        it.next();
        Assert.assertTrue(it.hasNext());
        it.next();
        Assert.assertFalse(it.hasNext());
    }

    @Test
    public void testPrintInRandom() {
        RandomizedQueue<Integer> q = new RandomizedQueue();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(4);
        q.enqueue(5);
        q.enqueue(6);
        System.out.println(q.toString());
        System.out.println(q.dequeue());
        Assert.assertTrue(q.size() == 5);
        System.out.println(q.toString());
        System.out.println(q.dequeue());
        Assert.assertTrue(q.size() == 4);
        System.out.println(q.toString());
        System.out.println(q.dequeue());
        System.out.println(q.toString());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        Assert.assertTrue(q.isEmpty());
    }


    /**
     * Check that iterator() returns correct items after sequence of enqueue() operations *
     */
    @Test(expectedExceptions = java.util.NoSuchElementException.class)
    public void testIteratorEnqueue() {

        RandomizedQueue<Integer> q = new RandomizedQueue();
        q.enqueue(1);
        q.dequeue();
        q.enqueue(3);
        Iterator<Integer> it = q.iterator();
        Assert.assertTrue(it.hasNext());
        q.dequeue();
        Iterator<Integer> it2 = q.iterator();
        Assert.assertFalse(it2.hasNext());
        System.out.println(it2.next());
    }


    @Test
    public void testTwoIterators() {
        RandomizedQueue<Integer> q = new RandomizedQueue();
        for (int i = 0; i < 100; i++) {
            q.enqueue(i);
        }
        Iterator<Integer> it = q.iterator();
        Iterator<Integer> it2 = q.iterator();

        //get 99 items for first iterator
        for (int i = 0; i < 99; i++) {
            it.next();
        }

        Assert.assertTrue(it.hasNext());
        it.next();
        //should have no more
        Assert.assertFalse(it.hasNext());

        //but second iterator should be unaltered
        Assert.assertTrue(it2.hasNext());

    }

}
