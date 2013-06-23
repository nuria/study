package example

import common._
import scala.collection.mutable
object Lists {
  
  
  def main (args:Array[String]){
    println(list1(1))
    println(list2(3,4))
  }
  /**
   * This method computes the sum of all elements in the list xs. There are
   * multiple techniques that can be used for implementing this method, and
   * you will learn during the class.
   *
   * For this example assignment you can use the following methods in class
   * `List`:
   *
   *  - `xs.isEmpty: Boolean` returns `true` if the list `xs` is empty
   *  - `xs.head: Int` returns the head element of the list `xs`. If the list
   *    is empty an exception is thrown
   *  - `xs.tail: List[Int]` returns the tail of the list `xs`, i.e. the the
   *    list `xs` without its `head` element
   *
   *  ''Hint:'' instead of writing a `for` or `while` loop, think of a recursive
   *  solution.
   *
   * @param xs A list of natural numbers
   * @return The sum of all elements in `xs`
   */
	def sum(xs: List[Int]): Int = {
			if (xs.isEmpty)
				0
			else 
			  xs.head +sum(xs.tail)
    
  }

  /**
   * This method returns the largest element in a list of integers. If the
   * list `xs` is empty it throws a `java.util.NoSuchElementException`.
   *
   * You can use the same methods of the class `List` as mentioned above.
   *
   * ''Hint:'' Again, think of a recursive solution instead of using looping
   * constructs. You might need to define an auxiliary method.
   *
   * @param xs A list of natural numbers
   * @return The largest element in `xs`
   * @throws java.util.NoSuchElementException if `xs` is an empty list
   */
  def max(xs: List[Int]): Int = {
    if (xs.isEmpty) throw new java.util.NoSuchElementException
    if (xs.length ==1) xs.head
    else if (xs.head >= max(xs.tail))
    	xs.head
    else 
    	max(xs.tail)
  }
  
   val list2 = new Function2[Int,Int,List[Int]] {
    def apply (x:Int,y:Int)=x::y::Nil
  }
  
  val list1 = new Function1[Int,List[Int]] {
  
    def apply (x:Int) = x::Nil
  }
  
  
 
  
 
  
  ///////////////////////////////////////////////
   /**
   * Exercise 3
   */
  def countChange2(money: Int, coins: List[Int]): Int = {
    if (money == 0) 0
    else if (coins.isEmpty) 0
    var sequences = mutable.Set[String]()
    coins.sorted
    countChangeSeq(money, coins, "");

    def countChangeSeq(money: Int, coins: List[Int], sequence: String): Unit = {

      val usefulCoins = coins map { _.toInt } filter { _ <= money }

      if (usefulCoins.length == 1) {

        var newSequence: String = sequence.concat(usefulCoins(0).toString).toList.sorted.mkString
        if (!sequences.contains(newSequence)) {
          sequences.add(newSequence)
        }
      } else {
        for (c <- usefulCoins) {
          if (money - c == 0) {
            var newSequence: String = sequence.concat(c.toString).toList.sorted.mkString
            if (!sequences.contains(newSequence)) {
              sequences.add(newSequence)
            }

          } else {
            println(money)
            println(usefulCoins)
            countChangeSeq(money - c, usefulCoins, sequence.concat(c.toString))
          }
        }

      }
    }

    // println(sequences)
    sequences.size
  }

  /**Sum with anonymous functions **/
  
  def sumA(f:Int=>Int,a:Int,b:Int):Int= {
    if (a> b) 0
    else f(a)+sumA(x=>x,a+1,b)
    
    
  }
  
  
  
}
