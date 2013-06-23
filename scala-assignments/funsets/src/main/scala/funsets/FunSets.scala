package funsets

import common._

/**
 * 2. Purely Functional Sets.
 */
object FunSets {
  /**
   * We represent a set by its characteristic function, i.e.
   * its `contains` predicate.
   */
  type Set = Int => Boolean

  /**
   * Indicates whether a set contains a given element.
   */
  def contains(s: Set, elem: Int): Boolean = s(elem)

  /**
   * Returns the set of the one given element.
   * 
   * Actually what it returns is a function that from an element
   * returns true or false
   */
  def singletonSet(elem: Int): Set = {
		  val element = elem;
		  def belongs(elem:Int):Boolean = {
				  elem==element
		  }
    
		  belongs
  }

  /**
   * Returns the union of the two given sets,
   * the sets of all elements that are in either `s` or `t`.
   * 
   * returns a function that given an element of s or t returns true
   */
  def union(s: Set, t: Set): Set = {
    def belongs(elem:Int):Boolean = {
       s(elem) || t(elem)
    }
    belongs
  }

  /**
   * Returns the intersection of the two given sets,
   * the set of all elements that are both in `s` and `t`.
   */
  def intersect(s: Set, t: Set): Set = {
    def belongs(elem:Int):Boolean = {
       s(elem) && t(elem)
    }
    belongs
  }

  /**
   * Returns the difference of the two given sets,
   * the set of all elements of `s` that are not in `t`.
   */
  def diff(s: Set, t: Set): Set = {
    def belongs(elem:Int):Boolean = {
       s(elem) && !t(elem)
    }
    return belongs
  }

  /**
   * Returns the subset of `s` for which `p` holds.
   * 
   * I think here i am returning a funtcion that given s tells you
   * whether p holds
   */
  def filter(s: Set, p: Int => Boolean): Set = intersect(s: Set, p: Int => Boolean)

  /**
   * The bounds for `forall` and `exists` are +/- 1000.
   */
  val bound = 1000

  /**
   * Returns whether all bounded integers within `s` satisfy `p`.
   */
  def forall(s: Set, p: Int => Boolean): Boolean = {
   
    def iter(a: Int): Boolean = {
      //terminate if out of bounds, we got this far
      if (a>bound) true
      else if (s(a) && !filter(s,p)(a)) false
      else iter(a+1)
    }
    iter(bound* (-1))
  }

  /**
   * Returns whether there exists a bounded integer within `s`
   * that satisfies `p`.
   */
  def exists(s: Set, p: Int => Boolean): Boolean = {
    def iter(a: Int): Boolean = {
      //terminate if out of bounds
      if (a>bound) false
      else if (filter(s,p)(a)) true
      else iter(a+1)
    }
    iter(bound*(-1))
  }

  /**
   * Returns a set transformed by applying `f` to each element of `s`.
   */
  def map(s: Set, f: Int => Int): Set = {
    //Set s' contains a value x if there exists a value y in set s such that f(y)=x
  
    def belongs(a:Int):Boolean = {     
      exists(s,x=>f(x)==a)
    }
    
    belongs
  }
  

  /**
   * Displays the contents of a set
   */
  def toString(s: Set): String = {
    val xs = for (i <- -bound to bound if contains(s, i)) yield i
    xs.mkString("{", ",", "}")
  }

  /**
   * Prints the contents of a set on the console.
   */
  def printSet(s: Set) {
    println(toString(s))
  }
}
