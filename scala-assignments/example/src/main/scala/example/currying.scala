package example

object currying {

  def main(args:Array[String])= {
    val even=(a:Int)=>a%2==0;
    val asc = 1::2::3::4::5::Nil;
    
    val result = process(even)(asc)
    println(result);
    
    val l = 1::2::3::Nil;
    
   val r2 = l.foldLeft(0)((b:Int, a:Int)=>b+a);
   println(r2)
  }
  
  
  
  
  //see http://www.codecommit.com/blog/scala/function-currying-in-scala
  def process[A](filter:A=>Boolean)(list:List[A]):List[A]= {
   lazy val recurse = process(filter)_
    
    list match {
      case head::tail=>if (filter(head)){
                  head::recurse(tail)
                }else {
                  process(filter)(tail)//recurse(tail) also works
                }
      case Nil=>Nil
     
    }
  }
}