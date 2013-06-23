package example
/**
 * Idealized boolean.
 * This is the very tricky implementation of 
 * the primitive type boolean as a class
 */
abstract class IBoolean {
  
  /** 
   *  The idea is that instead of writing if condition a else b
   *  I would write condition.ifThenElse(a,b)
   */
  def ifThenElse[T](t: => T,e: => T):T //abstract method
  
  //always returns 1st argument if boolean is true
 // _true && x should return x
  //_false && x should return false
  def && (x: =>IBoolean) = ifThenElse(x,_false)
  
  //always returns 2nd argument if boolean is false
  //_true || x returns _true
  //_false || x returns x
  def || (x: =>IBoolean) = ifThenElse(_true,x)
  
  //if the boolean is false we return true , if true we return false
  def unary_! : IBoolean = ifThenElse(_false,_true)
  
  
  def == (x:IBoolean):IBoolean = ifThenElse(x,x.unary_!)
  
  def != (x:IBoolean):IBoolean = ifThenElse(x.unary_!,x)
  
  //_true <_false  returns _false (2nd arg)
  // _false <_true returns _true
  // _true <_true returns false
  // -false <-false returns false
  def < (x:Boolean) = {
    if (this == x) _false
    else this.ifThenElse(_false,x)
  }
}

object _true extends IBoolean {
  def ifThenElse[T](t: => T,e: => T):T=t
}

object _false extends IBoolean {
  def ifThenElse[T](t: => T,e: => T):T=e
}