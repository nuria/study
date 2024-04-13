package example

object ListExamples {

  def main(args:Array[String]) ={
    val s = singleton[Int](1);
   // println(s)
    val t =singleton(true)
    
    val list = new Cons(1,new Cons(2, new Nil))
  //  println(nth(0,list))
   // println(nth(1,list))
   // nth(-21,list)
    println(List(1));//really List.apply(1)
    
  }
  
  
  trait List[T] {
    def isEmpty:Boolean;
    def head:T;
    def tail:List[T]
    }
  
    /** this defines a parameter and a field of the class */
    class Cons[T](val head: T , val tail:List[T]) extends List[T] {
      def isEmpty:Boolean =false;
      
    }
    class Nil[T] extends List[T] {
      def isEmpty:Boolean=true;
      def head:Nothing = throw new NoSuchElementException;
      def tail:Nothing = throw new NoSuchElementException;
    }
  
    /** functions can also have parameters **/
    
    def singleton[T](elem:T) = {new Cons[T](elem,new Nil())}
    
    /** takes an integer and a list and selects the nth element of the list **/
    def nth[T](index:Int,list:List[T]):T = {
        if (list.isEmpty || index <0) {
          throw new IndexOutOfBoundsException()
        }  else if (0 == index) {
          list.head          
        } else {
          nth(index-1,list.tail)
        } 
      }
     
    
    object List {
       
      
      def apply (x:Int,y:Int)=new Cons(x,new Cons(y,new Nil[Int]))
       
  
      
  
         def apply (x:Int) = new Cons(x,new Nil[Int])
       
  
      
    }
      
    
    
    
}