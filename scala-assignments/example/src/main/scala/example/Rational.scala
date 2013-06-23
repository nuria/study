package example


object rationals{
  
  def main(args:Array[String]){
    val x = new Rational(1,3);
    var y = new Rational(5,7);
    var z = new Rational(3,2);
    println(x.substract(y).substract(z).toString)
    println("hola")
    //new Rational(2)
    println("x="+x.toString)
    println("y="+y.toString)
    println("addition")
    var w = x add y
    println(w)
    
  }
}
class Rational(x:Int,y:Int) {
  /** used to enforce a precondition **/
 require(y!=0,"denominator must be non zero"+y)
  val g = gcd(x,y)
  println(g)
  def numerator=x/g
  def denominator=y/g
  /** if numerator and denominator are called very often
   *  it will pay to turn those into val denominator (only called once)
   */
  
  
  /** other constructor **/
  def this(x:Int) = this(x,1)
  private def gcd(a:Int,b:Int):Int ={
    if (b==0) a
    else gcd(b, a%b)
      
 }
 
 
  def add(r:Rational):Rational={
    new Rational(this.numerator*r.denominator+r.numerator*this.denominator,r.denominator*this.denominator)
    
  }
 
  def < (that:Rational) ={
    if (numerator*that.denominator<denominator*that.numerator) true
    else false
  }
  def max(that:Rational)= {
    if (this < that) that
    else this
  }
  override def toString() = {
    "numerator "+numerator+" denominator"+denominator
  }
  
  // do not write the complicated formula twice
  def unary_- :Rational = new Rational( (-1)*numerator,denominator)
  
  
  def substract(r:Rational)= {
    add(-r)
  }
}

