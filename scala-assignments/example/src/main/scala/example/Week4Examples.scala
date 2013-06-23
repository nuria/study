package example


  

object Week4Examples {
  
  
  def main(args:Array[String]){
    println(f.apply(7))
    val result = eval(new Sum(new Number(1),new Number(2)))
    println(result);
    
   val sorted = insertionsort(List(4,3,2,1));
   println(sorted);
  }
  // anonymous functions
  // this is an anonymous class instance
  val f = new Function1[Int,Int] {
    def apply (x:Int)=x*x
  }

  ///// decomposition //////
  /// functional exmaple ////
  trait Expr {
    //clasiffication methods
    def isNumber:Boolean //kind of akward right? anticipating class types
    def isSum: Boolean
    //accessor methods 
    def numValue: Int
    def leftOpt:Expr
    def rightOpt:Expr
    
  }
  
  class Number(n:Int) extends Expr {
    def isNumber:Boolean = true
    def isSum: Boolean = false
    def numValue: Int = n
    def leftOpt:Expr = throw new Error
    def rightOpt:Expr = throw new Error
  }
  
  class Sum(e1:Expr,e2:Expr)  extends Expr{
     def isNumber:Boolean = false
     def isSum: Boolean = true
     def numValue: Int = throw new Error;
     def leftOpt:Expr = e1
     def rightOpt:Expr = e2
     
  }
  
  //takes one of these expressions and returns the number it represents
  def eval(e:Expr):Int = {
    if (e.isNumber) e.numValue
    else if (e.isSum) eval(e.leftOpt) + eval(e.rightOpt)
    else throw new Error("operation unknown");
    
  }
  
  
  ////// decomposition OO example
  // how would we do a *b+a*c =>a (b+c)
  // involves the whole subtree not a single object, not easy to do
  trait OExpr {
    def eval:Int
  }
  class ONum(n:Int) extends OExpr {
    def eval:Int = n
  }
  class OSum(e1:OExpr,e2:OExpr) extends OExpr {
    def eval:Int = e1.eval+e2.eval;
  }
  
  
  ///// now using pattern matching
  trait PExpr {
    
    
  }
  case class PNumber(n:Int) extends PExpr {}
  
  case class PSum(e1:PExpr,e2:PExpr) extends PExpr{}
  
  def peval(e:PExpr):Int = e match {
    case PNumber(n:Int) => n
    case PSum(e1:PExpr,e2:PExpr) => peval(e1)+peval(e2)
  }

  //eval can also be inside the trait
  //and use matching
  
  //helpfull if small class hierachy but loads of methods
  //OO solution is better if you would have loads of child classes
  trait PExpr2 {
    
    def peval:Int = this match {
    	case PNumber2(n) => n
    	case PSum2(e1,e2) => e1.peval+e2.peval
    }
    
     def show:String = this match {
    	case PNumber2(n) => n.toString();
    	case PSum2(e1,e2) => e1.toString() +"+"+e2.toString()
    }
  }
  
  case class PNumber2(n:Int) extends PExpr2 {}
  case class PSum2(e1:PExpr2,e2:PExpr2) extends PExpr2 {}
  
  
  /////// insertion sort 
  def insertionsort(xs:List[Int]):List[Int] = { xs match {
    case Nil=>Nil
    case y::ys=>insert(y,insertionsort(ys))
  }
  }
 
  /** inserts an element in a list already sorted **/
  def insert(y:Int,ys:List[Int]):List[Int] = {
    ys match {
      case Nil=>y::Nil
      case z::zs =>
        if (y<z) y::z::zs
        else z::insert(y,zs)
    }
    }
 
  
  
}