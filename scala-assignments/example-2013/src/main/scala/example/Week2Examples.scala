package example
import math.abs;

object Week2Examples {

  def main(args:Array[String])={
    
   // println(sum((x:Int)=>x,1,3))
   // println(fact(0))
    //println(fact(1))
    //println(fact(4))
    
    //println(fixedPoint(x=>1+x/2)(1))
   // println(sqrt2(2))
    val r = new Rational(1,2);
    
    println(r);
    var r2 = new Rational(1,3)
    r.add(r2).toString
  }
  
  /** Now sum a->b,
   *  using anonymous functions and tail recursion **/
  def sum(f:Int=>Int,a:Int,b:Int):Int = {
    
    def loop(a:Int,acc:Int):Int={
      if (a>b) acc
      else loop(a+1,acc+f(a))
    }
    
    loop(a,0)
  }
  
  /** product of interval of numbers a to b**/
  def product(f:Int=>Int)(a:Int,b:Int):Int = {
    
    def loop(a:Int,acc:Int):Int = {
      if (a>b) acc
      else loop(a+1,acc*f(a))
    }
    
    loop(a,1)
    
  }
  
  /** write factorial in terms of product **/
  
  def identitity=(x:Int)=>x
  
  def fact(x:Int):Int = 
    if (x==0) 0
    else if (x==1) 1
    else product(identity)(1,x)
    
    
    
    
   /** a function that combines both product and sum **/
   def mapReduce(f:Int=>Int,combine:(Int,Int)=>Int,zero:Int)(a:Int,b:Int):Int={    
      if (a>b) 0
      else combine(f(a),mapReduce(f,combine,zero)(a+1,b))
    }
  
  
  def product2(f:Int=>Int)(a:Int,b:Int):Int =  mapReduce(f,(x,y)=>x*y,1)(a,b)
  
  

  /* fixed point function */
  val tolerance= 0.001
  
  def isCloseEnough(x:Double,y:Double):Boolean={
    if (abs((x-y)/x)/x < tolerance) true
    else false
    
  }
  
  def fixedPoint(f:Double=>Double)(firstGuess:Double) = {
    
    def iterate(guess:Double):Double = {
      println(guess)
      var next = f(guess)
      if (isCloseEnough(next,guess)) guess
      else iterate(next)
    }
    
    iterate(firstGuess)
  }
  
  /**this averages two consecutive values y and x/y to pass
   * as next guess to the function so it converges faster
   * sqrt(x) is a fixed point of y=x/y given that y*y =x
   */ 
  def sqrt(x:Double)= {
    fixedPoint(y=>((x/y)+y)/2)(1.0)
  }
  
  /** a function that takes a function and returns another function */
  def stabilizingByAveraging(f:Double=>Double)(x:Double) = (x+f(x))/2
  
  
  def sqrt2(x:Double):Double = {
    val stablilizingf = stabilizingByAveraging(y=>x/y)(x)
    fixedPoint(stabilizingByAveraging(y=>x/y))(1.0)
  }
 
}