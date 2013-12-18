import org.testng.annotations.*;
import org.testng.annotations.Test;
import junit.framework.Assert;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.AfterClass;

import java.util.Iterator;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/21/13
 * Time: 7:21 PM
 * To change this template use File | Settings | File Templates.
 */
public class DequeTest {


    @Test
    public void TestOneElementQueue() {
        Deque<Integer> q = new Deque<Integer>();
        Assert.assertTrue(q.isEmpty());
        q.addFirst(3);
        q.removeLast();
        Assert.assertTrue(q.isEmpty());
        Assert.assertFalse(q.iterator().hasNext());
    }

    @org.testng.annotations.Test
    public void testIsEmpty() throws Exception {
        Deque<Integer> q = new Deque<Integer>();
        Assert.assertTrue(q.isEmpty());
        q.addFirst(3);
        Assert.assertFalse(q.isEmpty());
        Assert.assertEquals("size should be 1", q.size(), 1);
    }


    @Test
    public void testAddFirst() throws Exception {
        Deque<Integer> q = new Deque<Integer>();
        System.out.println(q.toString());
        Assert.assertTrue(q.isEmpty());
        q.addFirst(1);
        Assert.assertTrue(q.removeFirst().equals(1));
        q.addFirst(1);
        q.addFirst(2);
        q.addFirst(3);
        Assert.assertTrue(q.removeFirst().equals(3));

    }

    @Test
    public void testAddLast() throws Exception {
        Deque<Integer> q = new Deque<Integer>();
        System.out.println(q.toString());
        Assert.assertTrue(q.isEmpty());
        q.addFirst(1);
        Assert.assertTrue(q.removeLast().equals(1));
        q.addFirst(1);
        q.addFirst(2);
        q.addFirst(3);
        Assert.assertTrue(q.removeLast().equals(1));
        q.addLast(4);
        q.addLast(5);
        Assert.assertTrue(q.removeLast().equals(5));

    }


    @Test
    public void testIterator() throws Exception {
        Deque<Integer> q = new Deque<Integer>();
        Iterator<Integer> it = q.iterator();
        Assert.assertFalse(it.hasNext());
        q.addLast(1);
        System.out.println(q.toString());
        // get a new interator, iterator does not update with queue
        it = q.iterator();
        Assert.assertTrue(it.hasNext());
        Assert.assertTrue(it.next().equals(1));

    }
}
