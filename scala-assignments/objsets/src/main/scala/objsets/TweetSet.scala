package objsets

import common._
import TweetReader._
import scala.math.Ordered
import scala.math;


/**
 * A class to represent tweets.
 *  
 */
class Tweet(val user: String, val text: String, val retweets: Int) extends Ordered[Tweet] {
  override def toString: String =
    "\nUser: " + user + " " + "Text: " + text + " [" + retweets + "]\n"
    
    def len:Int = text.length;
  
  	/**
  	 * Compare method to assets
  	 * whether the tweets are equal
  	 */
    def compare(that: Tweet): Int = {
      this.text compare that.text
    }
    
}

/**
 * This represents a set of objects of type `Tweet` in the form of a binary search
 * tree. Every branch in the tree has two children (two `TweetSet`s). There is an
 * invariant which always holds: for every branch `b`, all elements in the left
 * subtree are smaller than the tweet at `b`. The elements in the right subtree are
 * larger.
 *
 * Note that the above structure requires us to be able to compare two tweets (we
 * need to be able to say which of two tweets is larger, or if they are equal). In
 * this implementation, the equality / order of tweets is based on the tweet's text
 * (see `def incl`). Hence, a `TweetSet` could not contain two tweets with the same
 * text from different users.
 * 
 * Actually I think is with the same length of text
 *
 *
 * The advantage of representing sets as binary search trees is that the elements
 * of the set can be found quickly. If you want to learn more you can take a look
 * at the Wikipedia page [1], but this is not necessary in order to solve this
 * assignment.
 *
 * [1] http://en.wikipedia.org/wiki/Binary_search_tree
 */
trait TweetSet {

  /**
   * This method takes a predicate and returns a subset of all the elements
   * in the original set for which the predicate is true.
   *
   * Question: Can we implement this method here, or should it remain abstract
   * and be implemented in the subclasses?
   */
  
   def filter(p: Tweet => Boolean): TweetSet =  filterAcc(p,new Empty());
   

  /**
   * This is a helper method for `filter` that propagates the accumulated tweets.
   */
  def filterAcc(p: Tweet => Boolean, acc: TweetSet): TweetSet

  /**
   * Returns a new `TweetSet` that is the union of `TweetSet`s `this` and `that`.
   *
   * Question: Should we implement this method here, or should it remain abstract
   * and be implemented in the subclasses?
   */
   def union(that: TweetSet): TweetSet

  /**
   * Returns the tweet from this set which has the greatest retweet count.
   *
   * Calling `mostRetweeted` on an empty set should throw an exception of
   * type `java.util.NoSuchElementException`.
   *
   * Question: Should we implment this method here, or should it remain abstract
   * and be implemented in the subclasses?
   */
  def mostRetweeted: Tweet

  /**
   * Returns a list containing all tweets of this set, sorted by retweet count
   * in descending order. In other words, the head of the resulting list should
   * have the highest retweet count.
   *
   * Hint: the method `remove` on TweetSet will be very useful.
   * Question: Should we implment this method here, or should it remain abstract
   * and be implemented in the subclasses?
   */
  def descendingByRetweet: TweetList  

  def isEmpty:Boolean;

  /**
   * The following methods are already implemented
   */

  /**
   * Returns a new `TweetSet` which contains all elements of this set, and the
   * the new element `tweet` in case it does not already exist in this set.
   *
   * If `this.contains(tweet)`, the current set is returned.
   */
  def incl(tweet: Tweet): TweetSet

  /**
   * Returns a new `TweetSet` which excludes `tweet`.
   */
  def remove(tweet: Tweet): TweetSet

  /**
   * Tests if `tweet` exists in this `TweetSet`.
   */
  def contains(tweet: Tweet): Boolean

  /**
   * This method takes a function and applies it to every element in the set.
   */
  def foreach(f: Tweet => Unit): Unit
  
 
  
}

class Empty extends TweetSet {
  def isEmpty: Boolean = true;
  
  override def toString: String ="Empty"

  /**
   * Returns a new `TweetSet` that is the union of `TweetSet`s `this` and `that`.
   */
   def union(that: TweetSet) = that;
 
  def mostRetweeted: Tweet = throw new java.util.NoSuchElementException;
  
  def descendingByRetweet: TweetList = throw new java.util.NoSuchElementException;

  
  def filterAcc(p: Tweet => Boolean, acc: TweetSet): TweetSet = new Empty();

 
   
   def descendingByRetwwet: TweetList = Nil
   

  /**
   * The following methods are already implemented
   */
  

  def contains(tweet: Tweet): Boolean = false

  def incl(tweet: Tweet): TweetSet = new NonEmpty(tweet, new Empty, new Empty)

  def remove(tweet: Tweet): TweetSet = this

  def foreach(f: Tweet => Unit): Unit = ()
}

class NonEmpty(val elem: Tweet, val left: TweetSet, val right: TweetSet) extends TweetSet {
  def root = elem;
  
    def isEmpty: Boolean = {
       left.isEmpty && right.isEmpty && this.remove(root) == this
      
      
      
    }
	
  override def toString: String = root.toString+left.toString()+right.toString();
  
    
   /**
   * This method takes a predicate and returns a subset of all the elements
   * in the original set for which the predicate is true.
   * 
   */   
  def filterAcc(p: Tweet => Boolean, acc: TweetSet): TweetSet = {
    
    if(p(root)){
      right.filterAcc(p, left.filterAcc(p,acc)).incl(root)     
    }else {   
     right.filterAcc(p, left.filterAcc(p,acc));
    }
    
  }
  
  
 
  /**
   * Returns a new `TweetSet` that is the union of `TweetSet`s `this` and `that`.
   *
   */
   def union(that: TweetSet): TweetSet = {   
     // idea, walk the whole new set adding element by element
     // this below is slower taht cheking for empties
    // that.union(left).union(right).incl(root)
 
    if (!this.isEmpty && left.isEmpty && right.isEmpty)
       that.incl(root)
     else if (right.isEmpty)
       that.union(left).incl(root)
      else if (left.isEmpty)
       that.union(right).incl(root)
     else 
       that.union(right).union(left).incl(root)
     
   
       
     
   }
  
  def mostRetweeted: Tweet = {
   var mostRetweeted:Tweet = root;
   
   if (!right.isEmpty ) {
	   val rmost = right.mostRetweeted;
   		if (rmost.retweets > root.retweets) mostRetweeted = rmost;
   }
      
   if (!left.isEmpty) {
	   val lmost = left.mostRetweeted;
	   if (lmost.retweets > mostRetweeted.retweets) mostRetweeted = lmost
   }
   
     mostRetweeted
  }
  
  def descendingByRetweet:TweetList = {   
    val mostR = this.mostRetweeted
    val newTree = this.remove(mostR)   
    
    if (newTree.isEmpty)
    	new Cons(mostR, Nil);
    else 
    	new Cons(mostR, newTree.descendingByRetweet);
    
  }
 
  /**
   * The following methods are already implemented
   */

  def contains(x: Tweet): Boolean =
    if (x.text < elem.text) left.contains(x)
    else if (elem.text < x.text) right.contains(x)
    else true

  /**
   * Adds an element to the set, returns a whole new set
   */
  def incl(x: Tweet): TweetSet = {
    if (x.text < elem.text) new NonEmpty(elem, left.incl(x), right)
    else if (elem.text < x.text) new NonEmpty(elem, left, right.incl(x))
    else this
  }
   
  

  def remove(tw: Tweet): TweetSet =
    if (tw.text < elem.text) new NonEmpty(elem, left.remove(tw), right)
    else if (elem.text < tw.text) new NonEmpty(elem, left, right.remove(tw))
    else left.union(right)

  def foreach(f: Tweet => Unit): Unit = {
    f(elem)
    left.foreach(f)
    right.foreach(f)
  }
}

trait TweetList {
  def head: Tweet
  def tail: TweetList
  def isEmpty: Boolean
  def foreach(f: Tweet => Unit): Unit =
    if (!isEmpty) {
      f(head)
      tail.foreach(f)
    }
}

object Nil extends TweetList {
  def head = throw new java.util.NoSuchElementException("head of EmptyList")
  def tail = throw new java.util.NoSuchElementException("tail of EmptyList")
  def isEmpty = true
}

class Cons(val head: Tweet, val tail: TweetList) extends TweetList {
  def isEmpty = false
}


object GoogleVsApple {
  val google = List("android", "Android", "galaxy", "Galaxy", "nexus", "Nexus")
  val apple = List("ios", "iOS", "iphone", "iPhone", "ipad", "iPad")

  
  def contains(l:List[String],t:Tweet): Boolean = {
	val word = l.head;
    
    if (t.text.contains(word) ) true
    else contains(l.tail,t)
	  
  }
  
  def containsGoogle(t:Tweet) =(t:Tweet) => contains(google,t)
   
  
  
  lazy val googleTweets: TweetSet = {
    allTweets.filter((t:Tweet) => contains(google,t))
    
  }
 
  lazy val appleTweets: TweetSet = {
     allTweets.filter((t:Tweet) => contains(apple,t))
  }

  /**
   * A list of all tweets mentioning a keyword from either apple or google,
   * sorted by the number of retweets.
   */
  lazy val trending: TweetList = {
    googleTweets.union(appleTweets).descendingByRetweet;
  }
}

object Main extends App {
  println("executing...")
  // Print the trending tweets
  GoogleVsApple.trending foreach println
}
