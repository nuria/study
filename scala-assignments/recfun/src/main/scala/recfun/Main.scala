package recfun
import common._
import scala.collection.mutable

object Main {
  def main(args: Array[String]) {
    //println("Pascal's Triangle")
    //for (row <- 0 to 10) {
    //for (col <- 0 to row)
    //print(pascal(col, row) + " ")
    //println()
    //}
    //countChange(4, List(1, 2))
    //countChange(4, List(1, 2, 3))
	  //println(balance("())(".toList))
	  //println(balance("hola".toList))
	  //println(balance("m (t (yet) d)\n(ng)".toList))
    println(balance("( (yet))(ng)".toList))
  }

  /**
   * Exercise 1.Pascal triangle
   */
  def pascal(c: Int, r: Int): Int =
    if (r == 0) 1
    else if (c == 0) 1
    else if (c == r) 1
    else pascal(c - 1, r - 1) + pascal(c, r - 1)

  /**
   * We are recursing (-> *****<-)
   */
  def balance(chars: List[Char]): Boolean =  {
       /**
        * checking if a list has no paren recursively, scala style
        * **/
      def noParenthesis(charList: List[Char]):Boolean ={      
        //made it through w/o stopping
        if (charList.isEmpty) true
        else {   
        	if (charList.head =="(".toList(0) || charList.head ==")".toList(0)) false
        	else noParenthesis(charList.tail)    
        }
      }
      
      /** 
       *  Look for the index of ")" or "("
       *  starting from the end 
       */
      def indexOfParenthesis(charList: List[Char],paren :String,index:Int) :Int = {
        //println(">>charlist "+charList.toString+" index "+index)
        
        if (charList.isEmpty) -1
        else if (charList.head==paren.toList(0)) return index
        else indexOfParenthesis(charList.tail,paren,index-1)
      }
           
      def lookAhead(chars:List[Char],paren :String) = {

    	 val indexParen = indexOfParenthesis(chars.reverse,paren,chars.length-1) 
    	 if (indexParen == -1) false
    	 else {
    		//println("index of close ) "+indexParen)
    		//println("chars "+chars)
    		val list = for(i <- 1 to indexParen-1) yield chars(i)     //do not include head
    		
    		balance(list.toList)
         }
      }

       //// juicy function below
    //  println("outer loop"+chars.toString)
       
      if (chars.isEmpty) true
      else if (noParenthesis(chars)) true
      else  {
    	  if (chars.head =="(".toList(0)){
    		  lookAhead(chars,")")
    	  }else if (chars.head ==")".toList(0)){
    	    lookAhead(chars,"(")  
    	  }else {
    		  balance(chars.tail)
    	  }
      }

}

  def countChange(money: Int, coins: List[Int]): Int = {
    if (money == 0) 0
    else if (coins.isEmpty) 0
    else {
      var h = coins.sorted.head;
      var t = coins.sorted.tail;
      if (h > money) 0
      else if (money == h) 1
      else countChange(money - h, coins.sorted) + countChange(money, t)
    }
  }

}
 
