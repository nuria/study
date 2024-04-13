package example
/**
 * Natural numbers
 */
abstract class Nat {
  
  def isZero:Boolean
  
  /** throw exception if negative**/
  def predecessor:Nat
  
  def successor:Nat
  
  def + (that:Nat):Nat 
  
  
  def - (that:Nat):Nat
  

}

/** Remember objects are singletons **/
object Zero extends Nat{
  def isZero:Boolean = true;
  
  def predecessor:Nat = throw new Exception();
  
  def + (that:Nat):Nat = that
  
  def - (that:Nat):Nat = if (that.isZero) that else throw new Exception();
  
  def successor = new Succ(this);
}
/** represents natural number 1 bigger than the given one **/
class Succ(n:Nat) extends Nat {
  def isZero:Boolean = false;
  
   def + (that:Nat):Nat = {
     if (that.isZero) this
     else (that - new Succ(Zero)) + new Succ(this)
    
  }
   
   def predecessor:Nat = n
   
   def successor:Nat = new Succ(this)
   
   
 /**  def - (that:Nat):Nat = {
     if (that.isZero) this
     else new Succ(this) -(that -new Succ(Zero))
   }**/
   
    def - (that:Nat):Nat = {
     if (that.isZero) this
     else n - that.predecessor //gret idea, substract 1 from each side!
   }
   
  
}