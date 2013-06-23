package example

object LastWeekExamples {
  
  def main(args: Array[String]){
  /*  val newList = removeAt(List(1,2,3,4),1)
    println(newList)
    val sortedMaybe = mergeSort(List(2,1,3,7,9,4));
    println(sortedMaybe);
   
    println("square elements")
    println(squareElements(List(2,5)))
    println(List ("a","a", "b", "a"));
    println("packing");
    val packed = pack(List ("a","a", "b", "a"))
    println(packed)
     
    val encoded = encode(List ("a","a", "b", "a"))
    println(encoded)
    * 
    
    
    val sum = sum2(List(1,1,1,1))
    println(sum)
    val anothersum = sum3(List(1,1,1,1))
    println(anothersum)
    
    val len = lenFun(List(1,1,1,1))
    println(len)
    
    val upper = "Hello".filter(x=>x.isUpper)
    println(upper.toString)
    **/
    val combinationsList = combinations(3,4)
    println(combinationsList)
    
    /**
    val _scalarProduct2 = scalarProduct2(Vector(1,1,1),Vector(2,2,2));
    println(_scalarProduct2)
    
    
    val _scalarProduct = scalarProduct(Vector(1,1,1),Vector(2,2,2));
    println(_scalarProduct)
    
    println("primes")
    println("7" + isPrime(7))
    println("8" + isPrime(8))
    println("13" + isPrime(13))
    
    println(findPrimePairs(4))
      println(findPrimePairs2(4))
      
      
     println("mapssss")
      
     val countryOfCapital = capitals map {
      case (x,y)=>(x,y);
    }
    
    println(countryOfCapital);
    
    println(getCapital("US"))
    println(getCapital("Andorra"))
    * 
    */
  }

  /**
   * For learning sake let's implement
   * init method for a list, returns all but last element
   */
  def init[T](xs:List[T]):List[T] ={
    
    xs match {
      case List()=>throw new Exception() //empty list
      case List(x)=>Nil //only 1 element
      case y::ys => y::init(ys) //2 or more elements
      
    }
  }
  
  def concat[T](l1:List[T],l2:List[T]):List[T] = {
   
    l2 match {
      case Nil => l1
      case x::xs=> x :: concat(xs,l1)
      
    }
  }
  
  def reverse[T](l1:List[T]):List[T] = {  
    l1 match {
      case Nil => Nil
      case List(x) => List(x)
      case x::xs => reverse(xs) ++ List(x)   
    }
  }
  
  /**
   * Remove nth element of a list
   */
  def removeAt[T](l1:List[T],n:Int):List[T] = {
   //happy case
    def _removeAt(before:List[T],after:List[T],k:Int):List[T] = {

    	if (k==0) before ++ after.tail
    	else {
      	  _removeAt(before ++ List(after.head),after.tail,k-1)
    	}
    }
    
    _removeAt(Nil,l1,n)
  }
  
  
  
  def mergeSort(l:List[Int]):List[Int] ={   
    if (l==Nil) return Nil
    val len:Int = l.length
    l match  {
    	case List(x) => List(x)
    	case x::xs => {
 			merge(mergeSort((l take (len/2))),mergeSort((l drop len/2)))((x:Int,y:Int)=>x < y)
     }
    }
  }
  
   /**
     * Merges two sorted lists
     */
    def merge1(l1:List[Int],l2:List[Int]):List[Int] ={
      if (l1==Nil) l2
      else if (l2==Nil) l1
      else {
        if (l1.head < l2.head) List(l1.head) ++ merge1(l1.tail,l2)
            else List(l2.head) ++ merge1(l1,l2.tail)
      }
    }
    
    /** Now merge with patter matching in pairs **/
    def merge2(xs:List[Int],ys:List[Int]):List[Int] = {
      (xs,ys) match {
        case (Nil,ys)=>ys
        case (xs,Nil)=>xs
        case (x::xt,y::yt) => {
          if(x < y) List(x) ++ merge2(xt,ys)
          else List(y) ++ merge2(xs,yt)
        }
      }
    }
      /**
       * generic merge using generics and passing along a comparation function
       * this could also use ord: Ordering instead of lt
       *  def merge[T](xs:List[T],ys:List[T])(implicit ord:Ordering):List[T]
       */
      def merge[T](xs:List[T],ys:List[T])(lt:(T,T) => Boolean):List[T] = {
      (xs,ys) match {
        case (Nil,ys)=>ys
        case (xs,Nil)=>xs
        case (x::xt,y::yt) => {
          if(lt(x,  y)) List(x) ++ merge(xt,ys)(lt)
          else List(y) ++ merge(xs,yt)(lt)
        }
      }
    }
      
      
      // Example: mutiply every elemet of a list by a factor
      // actually let's see a generic map function that takes a  list and a
      // function and applies to all
      // elements of the list
      
      def map[T](xs:List[T],f:(T)=>T):List[T] = {
        xs match {
          case Nil =>xs
          case _ =>f(xs.head) :: map(xs.tail,f)
        }
      }
      
      // also let's define this function as member of a class
    /**  abstract class SmartList[T] extends List {
        
        def map[U](f:(T)=>U):List[U] = {
          this match {
            case Nil =>this
            case x::xt =>f(x) :: this.map(xt)
          }
        }
      } **/
  
      // function that squares all elements of a list, using map defined
      // outside the class
      
      def squareElements(xs:List[Int]):List[Int] ={
    		  
    		  map(xs, (x:Int) => x * x)
      }
      
      
      //selection of all elements satisfiing a condition
      def positiveElements(xs:List[Int]):List[Int] = {
        
        xs match {
          case Nil =>xs
          case xs::xt if (xs > 0) => xs::positiveElements(xt) 
          case xs::xt if (xs <= 0) => positiveElements(xt) 
        }
      }
      
      
      //generalizing poselements with a filter function
      
      def filter[T](xs:List[T],p:(T) => Boolean):List[T] = {
        xs match {
          case Nil =>xs
          case xs::xt if p(xs) => xs::filter(xt,p) 
          case xs::xt => filter(xt,p) 
        }
      }
      //there is a handy partition function too that works like 'filter' and 'filterNot'
      
      //write a function that packs consecutive duplicates of list elements in one list
      // (List ("a","a", "b", "a"), List("a","a"),List("b"),List("a"))
      
      def pack[T](xs:List[T]):List[List[T]] = {
        
        def equals[T](x:T)(y:T)= {
          x == y
        }    
        xs match {
          case Nil =>Nil
          case x::xt => {
           val (lista,listb) = xs.span(equals(xs.head))
           List(lista) ++ pack(listb)
          } 
        }
      }
      
      /**
       * Run length encoding:
       * List ("a","a", "b", "a")=> List("a",2),List("b",1),List("a",1))
       */
       def encode[T](xs:List[T]):List[(T,Int)] = {
   
       
        
        def walkList(l:List[List[T]]):List[(T,Int)] = {
        	l match {
        		case Nil =>Nil
        		case x::xt => {
        			val encodedListElement = (x.head, x.length)
        			encodedListElement :: walkList(xt);
        		} 
        	}
        }
         walkList(pack(xs))
       }
       
       def sum1(xs:List[Int]):Int={
         xs match {
           case Nil=> 0
           case x::xt => x + sum1(xt)
         }
       }
       
       def sum2(xs:List[Int]):Int = {
         xs.foldLeft(0)((x,y)=>x+y)
       }
       // here I think fold right and fold left are equivalent
       def sum3(xs:List[Int]):Int = {
         xs.foldRight(0)((x,y)=>x+y)
       }
       
       //get length of list using fold
       def lenFun(xs:List[Int]):Int ={
         var len:Int = 0;
         
         def _len(x:Int,y:Int):Int = {
           len = len +1
           len 
         }
           
         xs.foldLeft(0)(_len)
        
       }
       
       //list all combinations of numbers x and y where x is drawn from 1..m and y
       // is drawn from 1..n
       def combinations(m:Int,n:Int):Seq[(Int,Int)]={
          val list1 = 1 to m;
          val list2 = 1 to n;
          list1.flatMap((x:Int)=>list2.map(y=>(x,y)))
       }
       
       /**
        * Scalar product of a vector
        */
       def scalarProduct(xs:Vector[Double], ys:Vector[Double]):Double = {
        
         val pairList:Vector[(Double,Double)] = xs zip ys;
         
         val semiSum:Vector[Double] = pairList.map((y:(Double,Double))=>(y._1*y._2))
         
         semiSum.sum
         
       }
       
       // a number is prime if it can only be divided by 
       // itself and 1 
       def isPrime(i:Int):Boolean = {
         //range of possible divisors
         val range = 2 until i        
         !range.exists((x:Int)=>( i % x == 0))   
       }
       
       def findPrimePairs(n:Int):Seq[(Int,Int)] = {
         val comb:Seq[(Int,Int)]= combinations(n,n);
         comb.filter(x=>isPrime(x._1+x._2))
       }
       
       
       /// now find primepairs using for expressions
       def findPrimePairs2(n:Int):Seq[(Int,Int)] = {
         for {
           i <- 1 until n
           j <- 1 until n
           if isPrime(i+j)
         }yield (i,j)
       }
       
       def scalarProduct2(xs:Vector[Double], ys:Vector[Double]):Double = {
        val products = for {
           i <- xs zip ys
          
         }yield(i._1*i._2)
         
         println(products)
         
         products.sum
       }
       ///////////////////// Maps ////////////////////////////////
       
       val capitals = Map("US"->"Washinton","Switerzland"->"Bern");
       
       
       // using options, map data representation
       def getCapital(country:String):String = {
         capitals get(country) match {
           case Some(capital) => capital
           case None => "none"
         }
       }
       
}