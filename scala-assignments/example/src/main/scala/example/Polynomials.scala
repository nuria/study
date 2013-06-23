package example

object Polynomials {

  
  def main(args:Array[String]){
    val p1 = new Poly(Map(1 ->1, 2 ->2,3->3));
    val p2 = new Poly(Map(0->1,1->1));
    
    val p3 = p1.add(p2)
    println(p3)
    
  }
  /**
   * Polynomials can be represented as a map of 
   * exponents to coefficients so 1+x+56x2
	 would be 0->1, 1->1, 2->56
	 
   */
  
  class Poly(val terms0:Map[Int,Double]) {
  
    val terms:Map[Int,Double] = terms0.withDefaultValue(0.0)
    
  	def add(other:Poly):Poly={
	  new Poly(other.terms.foldLeft(this.terms)(addTerm))
  }
    
    
    def addTerm(terms:Map[Int,Double],term:(Int,Double)):Map[Int,Double]= {
      println(terms)
      println(term)
      terms.map((t:(Int,Double)) => if (t._1==term._1) (t._1,t._2+term._2)  else t)
    }
    
   
     
    override def toString:String = {
      
      val listOfStrings = for ((exp,coef) <- this.terms.toList.sorted ) yield "Exp"+exp.toString()+"Coef"+coef.toString()
       listOfStrings.mkString("+");
     }
  
  }

}