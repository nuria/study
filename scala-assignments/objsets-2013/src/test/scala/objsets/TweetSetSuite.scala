package objsets

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

@RunWith(classOf[JUnitRunner])
class TweetSetSuite extends FunSuite {
  trait TestSets {
    val set1 = new Empty
    val set2 = set1.incl(new Tweet("a", "a body", 20))
    val set3 = set2.incl(new Tweet("b", "b body", 20))
    val c = new Tweet("c", "c body", 7)
    val d = new Tweet("d", "d body", 9)
    val set4c = set3.incl(c)
    val set4d = set3.incl(d)
    val set5 = set4c.incl(d)
    
    val set6 = set5.incl(new Tweet("e", "a body", 21));
    
    val set7 = new Empty;
    //constrain by length
    // given our impl two tweets from diff users cannot have have = number of chars
    // every tweet of a user is distinct if it has distinct length
    
    val set8 = set7.incl(new Tweet("test1", "test1 body", 1))
    .incl(new Tweet("test2", "test2  body", 2))
    .incl(new Tweet("test3", "test3 | body", 3))
    .incl(new Tweet("test4", "test4 || body", 4))
    .incl(new Tweet("test5", "test2 ||| body", 5))
    .incl(new Tweet("test6", "test3 |||| body", 6))
    .incl(new Tweet("test7", "test4 ||||| body", 7))
    .incl(new Tweet("test8", "test2 ||||||| body", 8))
    .incl(new Tweet("test9", "test3 |||||||body", 9))
    .incl(new Tweet("test10", "test4 |||||||| body", 10))
    .incl(new Tweet("test11", "test2 ||||||||| body", 11))
    .incl(new Tweet("test12", "test3 |||||||||| body", 12))
    .incl(new Tweet("test13", "test4 ||||||||||| body", 13));
    
    val set9 = set7.incl(new Tweet("test1 -2 ", "test1-2 body", 1))
    .incl(new Tweet("test2 -2", "test2-2 | body", 2))
    .incl(new Tweet("test3 -2", "test3-2 || body", 3))
    .incl(new Tweet("test4 -2", "test4-2 ||| body", 4))
    .incl(new Tweet("test5 -2", "test2-2 |||| body", 5))
    .incl(new Tweet("test6 -2", "test3-2 ||||| body", 6))
    .incl(new Tweet("test7 -2", "test4-2 |||||| body", 7))
    .incl(new Tweet("test8 -2", "test2-2 ||||||| body", 8))
    .incl(new Tweet("test9 -2", "test3-2  |||||||body", 9))
    .incl(new Tweet("test10 -2", "test4-2 |||||||| body", 10))
    .incl(new Tweet("test11 -2", "test2-2 ||||||||| body", 11))
    .incl(new Tweet("test12 -2", "test3-2 |||||||||| body", 12))
    .incl(new Tweet("test13 -2", "test4-2 ||||||||||| body", 13));
    
    
    
    
 
  }

  def asSet(tweets: TweetSet): Set[Tweet] = {
    var res = Set[Tweet]()
    tweets.foreach(res += _)
    res
  }

  def size(set: TweetSet): Int = asSet(set).size

 /** test("filter: on empty set") {
    new TestSets {
      assert(size(set1.filter(tw => tw.user == "a")) === 0)
    }
  }

  test("filter: a on set5") {
    new TestSets {
      assert(size(set5.filter(tw => tw.user == "a")) === 1)
    }
  }

  test("filter: 20 on set5") {
    new TestSets {
      assert(size(set5.filter(tw => tw.retweets == 20)) === 2)
    }
  }
  
   test("filter: > 20 retweets") {
    new TestSets {
      assert(size(set5.filter(tw => tw.retweets > 20)) === 0)
    }
  }

  test("union: set4c and set4d") {
    new TestSets {
      assert(size(set4c.union(set4d)) === 4)
    }
  }
  
  **/
  test("big union: set8") {
    new TestSets {
      val startTime = System.currentTimeMillis()
      assert(size(set8.union(set9)) === 26)
     val endTime = System.currentTimeMillis()
      
      System.out.println(endTime-startTime);
    }
  }
  
/**
  test("union: with empty set (1)") {
    new TestSets {
      assert(size(set5.union(set1)) === 4)
    }
  }

  test("union: with empty set (2)") {
    new TestSets {
      assert(size(set1.union(set5)) === 4)
    }
  }
  
   test("most retweets: set5") {
    new TestSets {
      val tweet = set5.mostRetweeted
      assert(tweet.retweets==20)
     
    }
  }
  

  test("descending: set5") {
    new TestSets {
      val trends = set5.descendingByRetweet   
       
     assert(!trends.isEmpty)   
      assert(trends.head.user == "a" || trends.head.user == "b")
    }
  }
  * 
  */
}
