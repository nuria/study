package example

/** object here means that Week3Examples is a singleton **/
object Week3Examples {

  def main( args:Array[String]){
    val tree = new NonEmpty(10,Empty,Empty);
    val tree2 = tree.incl(2)
    println("tree1 contains2"+tree.contains(2))
    println(tree.toString)
    
    
    println("tree2 contains 2"+tree2.contains(2))
    println(tree2)
    val tree3 = tree2.incl(3)
    println(tree2.toString)
    println(tree3.toString)
    tree.incl(43)
     println(tree.toString)
  }
  
  abstract class IntSet {
    /* add a new element */
    def incl(x:Int):IntSet;
    def contains(x:Int):Boolean;
    def union(other:IntSet):IntSet;
  }
  
  // implementing sets as binary trees
  // there are two types of trees the binary tree with an integer and two subtrees
  // and the empty tree
  //invariant: tree is sorted <x, x, >x
  /** this is a singleton, see word object instead of class */
  object Empty extends IntSet {
    def contains(x:Int):Boolean = false;
    def incl(x:Int):IntSet = new NonEmpty(x, Empty,Empty )
    def union(other:IntSet) = other;
    override def toString: String = " {} " 
  }
  
  
  class NonEmpty(val elem:Int,val left:IntSet, val right:IntSet) extends IntSet{
    
    def root = elem;
    def _right = right;
    def _left = left;
    
  
   override def toString: String = " {"+ elem.toString+"" +" {" +this.right.toString()+"}" +"  {"+this.left.toString()+"}}";
    
    def contains(x:Int):Boolean = {
      if (x<elem) left.contains(x)
      else if (x>elem) right.contains(x)
      else true
    }
      
    /**
     * Careful, this include creates
     * a whole new parallel tree, it does not modify the prior one
     * This is called a persistent data structure, even when 
     * there is a modification the "old" data structure is still present
     */
    
    def incl(x:Int):IntSet = {
      if (x< elem) new NonEmpty(elem,left.incl(x),right)
      else if (x>elem) new NonEmpty(elem,left,right.incl(x))
      else this
    }
    
    /** crazy recursion **/
    def union(other:IntSet):IntSet = {
     ((left union right) union other) incl elem
    }    
  }
}

