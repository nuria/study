package example
/**
 * Dealing with streams and lazy evaluation
 */
object Week7Examples {
  
  
  def main(args:Array[String]) = {
    println((1 to 100).toStream)
    // all natural numbers
    val naturals = from(0);
    //now all multiples of 4
    val m4 = from(0).map(_*4)
    println(m4.take(10))//will not print anything
    println(m4.take(10).toList)
    
    println(ePrime(from(2)).take(3).toList)
    
    println(sqrtStream(2).take(3).toList)
    
    println(sqrtStream(4).filter(isGoodEnough(_, 4)).take(5).toList)
  }
  
  
 
  
  

  def streamRange(from:Int,to:Int):Stream[Int] = {
    if (from==to ) Stream.Empty
    else Stream.cons(from,streamRange(from+1,to))
    
  }
  
  // modeling infinite data streams 
  // these are all naturals starting at a given number
  def from(n:Int):Stream[Int] ={
    n#::from(n+1);
    
  }
  
  // Sieve of erathostenes to calculate prime numbers
  // start with two the 1st prime number, eliminate all multiples of two
  // the 1t one left is a three, now eliminate all mutiples of three
  // iterate forever, at each step the first number 
  // is a prime number and we eliminate all its mutiples
  
  def ePrime(a:Stream[Int]):Stream[Int] = {
    
    
    a.head#::ePrime(from(a.head+1).filter(_ % a.head !=0))
    
  }
  /** Newton's method for sqrt **/
  
  def sqrtStream(x:Double):Stream[Double] = {
    def improve(guess:Double):Double = {
       (x/guess + guess)/2
    }
    
    // kind of strange, appliying a map operation on a value we are about to define
    lazy val guesses:Stream[Double]  = improve(1) #:: guesses.map(improve)
    guesses
  }
  
  // decide when to terminate calculating square roots
  def isGoodEnough(guess:Double,target:Double):Boolean = {
    
    math.abs((guess*guess)-target) <0.00001  
  }
  
}