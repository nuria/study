package patmat

import common._

/**
 * Assignment 4: Huffman coding
 *
 */
object Huffman {
  
  
  def main(args:Array[String]){
    println(decodedSecret)
    val quicklyEncoded2 = quickEncode2(frenchCode)("huffmanestcool".toList);
    println(quicklyEncoded2);
    val quicklyEncoded = quickEncode(frenchCode)("huffmanestcool".toList);
    println(quicklyEncoded);
  }

  /**
   * A huffman code is represented by a binary tree.
   *
   * Every `Leaf` node of the tree represents one character of the alphabet that the tree can encode.
   * The weight of a `Leaf` is the frequency of appearance of the character.
   *
   * The branches of the huffman tree, the `Fork` nodes, represent a set containing all the characters
   * present in the leaves below it. The weight of a `Fork` node is the sum of the weights of these
   * leaves.
   */
  // Seems to me that this abstract class is here just to do the match
 /** abstract class CodeTree
  case class Fork(left: CodeTree, right: CodeTree, chars: List[Char], weight: Int) extends CodeTree
  case class Leaf(char: Char, weight: Int) extends CodeTree
 **/
  
 abstract class CodeTree {
   def weight:Int
   def chars:List[Char]
 }
  case class Fork(val left: CodeTree, val right: CodeTree, val chars: List[Char], val weight: Int) extends CodeTree {
    
    
  }
  case class Leaf(val char: Char, val weight: Int) extends CodeTree {
    def chars:List[Char] = List(char)
  }



  // Part 1: Basics
 /** returns total weight of a given huffman tree **/
  def weight(tree: CodeTree): Int = {
     tree match {
       case Fork(l,r,chars,w)=>weight(l)+weight(r)
       case Leaf(char,w)=>w
     }
  }

  // tree match ...
  /**return the list of characters defined in a huffman tree **/
  def chars(tree: CodeTree): List[Char] = {
     tree match {
       case Fork(l,r,c,w)=>chars(l) ++ chars(r)
       case Leaf(char,w)=>char::Nil
     }
  }

  // I added the return type code tree here
  def makeCodeTree(left: CodeTree, right: CodeTree):CodeTree =
    Fork(left, right, chars(left) ::: chars(right), weight(left) + weight(right))



  // Part 2: Generating Huffman trees

  /**
   * In this assignment, we are working with lists of characters. This function allows
   * you to easily create a character list from a given string.
   */
  def string2Chars(str: String): List[Char] = str.toList
  
  /**
   * for List(a,b,c) will return abc
   */
  def chars2String(chars:List[Char]):String= {
      
    def innerToString(list:List[Char],str:String):String = {
       list match  {
        case xs::Nil => str+xs.toString()
        case _=>innerToString(list.tail,list.head.toString())
      }
    }
    innerToString(chars.tail,chars.head.toString())
  }

  /**
   * This function computes for each unique character in the list `chars` the number of
   * times it occurs. For example, the invocation
   *
   *   times(List('a', 'b', 'a'))
   *
   * should return the following (the order of the resulting list is not important):
   *
   *   List(('a', 2), ('b', 1))
   *
   * The type `List[(Char, Int)]` denotes a list of pairs, where each pair consists of a
   * character and an integer. Pairs can be constructed easily using parentheses:
   *
   *   val pair: (Char, Int) = ('c', 1)
   *
   * In order to access the two elements of a pair, you can use the accessors `_1` and `_2`:
   *
   *   val theChar = pair._1
   *   val theInt  = pair._2
   *
   * Another way to deconstruct a pair is using pattern matching:
   *
   *   pair match {
   *     case (theChar, theInt) =>
   *       println("character is: "+ theChar)
   *       println("integer is  : "+ theInt)
   *   }
   */
  def times(chars: List[Char]): List[(Char, Int)] = {
    
    // Returns a new pairs with index incremented
    // Because pairs are inmutable we cannot alter it in place
    def swap(c:Char,p: (Char, Int)): (Char, Int)= {
    	if (p._1==c) {
    	  val pair: (Char, Int) = (c, p._2+1) 
    	  pair
    	  }
    	else p  	
    }
    
    // If list of pairs contains this char in one pair it returns true
    def smartContains(m:Char,freq:List[(Char,Int)]):Boolean={
      var contains = false
      freq.foreach(e=>  if (e._1==m) contains=true);
      contains
    }
    def innerTimes(chars:List[Char],freq:List[(Char,Int)]): List[(Char, Int)]={
      
       if (chars.isEmpty) freq
       else {
        val head = chars.head
         freq match {
        	case l: List[(Char, Int)] if smartContains(head,l) => innerTimes(chars.tail,l.map(x=>swap(head,x)));
        	case l: List[(Char, Int)] => {
        			val pair: (Char, Int) = (head, 1)
        			innerTimes(chars.tail,pair::l)
        		}
          } //end match
         
       } //end else 
    }
     innerTimes(chars,List()); 
     
    
  }

  /**
   * Returns a list of `Leaf` nodes for a given frequency table `freqs`.
   *
   * The returned list should be ordered by ascending weights (i.e. the
   * head of the list should have the smallest weight), where the weight
   * of a leaf is the frequency of the character.
   */
  def makeOrderedLeafList(freqs: List[(Char, Int)]): List[Leaf] = {
    
    def makeListWithfSortedInput(freqs: List[(Char, Int)],l:List[Leaf]): List[Leaf] = {
      freqs match {
    	  //non empty list
    	  case head::tail => {
    	    val h = freqs.head; 
    	    makeListWithfSortedInput(freqs.tail,l ++ List(new Leaf(h._1,h._2))) 
    	    
    	  } 
    	  //empty list
    	  case Nil =>l
    	 
      }
 
  	}
    makeListWithfSortedInput(freqs.sortBy(_._2),Nil);
  	
}

  /**
   * Checks whether the list `trees` contains only one single code tree.
   * What? One single element?
   * I guess so, returns true if list only has one element
   */
  def singleton(trees: List[CodeTree]): Boolean = {
    if (trees== Nil) false
	   trees.tail match {
	     //tail is empty, one element
	     case Nil =>true
	     case head::tail => false
	     
	   }
    
  }

  /**
   * The parameter `trees` of this function is a list of code trees ordered
   * by ascending weights. (1,2,3..)
   *
   * This function takes the first two elements of the list `trees` and combines
   * them into a single `Fork` node. This node is then added back into the
   * remaining elements of `trees` at a position such that the ordering by weights
   * is preserved.
   *
   * If `trees` is a list of less than two elements, that list should be returned
   * unchanged.
   */
  def combine(trees: List[CodeTree]): List[CodeTree] = {
    
    if (trees==Nil) trees
    
    def h = trees.head;
    
    trees.tail match {
      case l:List[CodeTree] if singleton(l)=>l
      case l:List[CodeTree] =>{
        val node = makeCodeTree(trees.head, l.head);
        val newList = l.tail ++ List(node)
         newList.sortBy(_.weight)
      }
    }

  }

  /**
   * This function will be called in the following way:
   *
   *   until(singleton, combine)(trees)
   *
   * where `trees` is of type `List[CodeTree]`, `singleton` and `combine` refer to
   * the two functions defined above.
   *
   * In such an invocation, `until` should call the two functions until the list of
   * code trees contains only one single tree, and then return that singleton list.
   *
   * Hint: before writing the implementation,
   *  - start by defining the parameter types such that the above example invocation
   *    is valid. The parameter types of `until` should match the argument types of
   *    the example invocation. Also define the return type of the `until` function.
   *  - try to find sensible parameter names for `xxx`, `yyy` and `zzz`.
   */
  def until[T]( s:List[T] => Boolean, r: List[T] => List[T])(trees: List[T]): List[T] = {
    if (s(trees)) trees
    else {
      val newList = r(trees);
      until(s,r)(newList)
    }
       
  } 

  /**
   * This function creates a code tree which is optimal to encode the text `chars`.
   *
   * The parameter `chars` is an arbitrary text. This function extracts the character
   * frequencies from that text and creates a code tree based on them.
   */
  def createCodeTree(chars: List[Char]): CodeTree = {
	// create list of frequencies  
    val listOfTuples = times(chars);
    // now with those create leafs
    val listOfLeafs = makeOrderedLeafList(listOfTuples)
    
    
    // trees is a List[CodeTree]
	val reduced = until(singleton, combine)(listOfLeafs)
	reduced.head
  
 }

  // Part 3: Decoding

  type Bit = Int

  /**
   * This function decodes the bit sequence `bits` using the code tree `tree` and returns
   * the resulting list of characters.
   * 
   * Given a sequence of bits to decode, we successively read the 
   * bits, and for each 0, we choose the left branch, and for each 1 we choose the right branch. 
   * When we reach a leaf, we decode the corresponding character 
   * and then start again at the root of the tree
   */
  def decode(tree: CodeTree, bits: List[Bit]): List[Char] = {
     var chars:List[Char] = List();
     
     def getToLeaf(_bits:List[Bit],t:CodeTree):List[Char]={
     
      	t match {
      		//keep traversing, get next bit
      		case Fork(l,r,chars,w) => {
      			if (_bits.head==1)  getToLeaf(_bits.tail,r)
      			else getToLeaf(_bits.tail,l)
      		}
      		//we reached a leaf
      		case Leaf(char,w) => {
      			//add char and start a fresh with bits list   
      		    chars = chars  ++ List(char)
      		    if (_bits!=Nil) getToLeaf(_bits,tree)
      		    else chars
 
      		}
      	} //end match
      
     }
         
     getToLeaf(bits,tree)
    
  }

  /**
   * A Huffman coding tree for the French language.
   * Generated from the data given at
   *   http://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres_en_fran%C3%A7ais
   */
  val frenchCode: CodeTree = Fork(Fork(Fork(Leaf('s',121895),Fork(Leaf('d',56269),Fork(Fork(Fork(Leaf('x',5928),Leaf('j',8351),List('x','j'),14279),Leaf('f',16351),List('x','j','f'),30630),Fork(Fork(Fork(Fork(Leaf('z',2093),Fork(Leaf('k',745),Leaf('w',1747),List('k','w'),2492),List('z','k','w'),4585),Leaf('y',4725),List('z','k','w','y'),9310),Leaf('h',11298),List('z','k','w','y','h'),20608),Leaf('q',20889),List('z','k','w','y','h','q'),41497),List('x','j','f','z','k','w','y','h','q'),72127),List('d','x','j','f','z','k','w','y','h','q'),128396),List('s','d','x','j','f','z','k','w','y','h','q'),250291),Fork(Fork(Leaf('o',82762),Leaf('l',83668),List('o','l'),166430),Fork(Fork(Leaf('m',45521),Leaf('p',46335),List('m','p'),91856),Leaf('u',96785),List('m','p','u'),188641),List('o','l','m','p','u'),355071),List('s','d','x','j','f','z','k','w','y','h','q','o','l','m','p','u'),605362),Fork(Fork(Fork(Leaf('r',100500),Fork(Leaf('c',50003),Fork(Leaf('v',24975),Fork(Leaf('g',13288),Leaf('b',13822),List('g','b'),27110),List('v','g','b'),52085),List('c','v','g','b'),102088),List('r','c','v','g','b'),202588),Fork(Leaf('n',108812),Leaf('t',111103),List('n','t'),219915),List('r','c','v','g','b','n','t'),422503),Fork(Leaf('e',225947),Fork(Leaf('i',115465),Leaf('a',117110),List('i','a'),232575),List('e','i','a'),458522),List('r','c','v','g','b','n','t','e','i','a'),881025),List('s','d','x','j','f','z','k','w','y','h','q','o','l','m','p','u','r','c','v','g','b','n','t','e','i','a'),1486387)

  /**
   * What does the secret message say? Can you decode it?
   * For the decoding use the `frenchCode' Huffman tree defined above.
   */
  val secret: List[Bit] = List(0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1)

  /**
   * Write a function that returns the decoded secret
   */
  def decodedSecret: List[Char] =  {
    
   decode(frenchCode,secret);
  }



  // Part 4a: Encoding using Huffman tree
  // If list of pairs contains this char in one pair it returns true
    def smartContains(m:Char,charList:List[Char]):Boolean = {
      var contains = false
      charList.foreach(e=>  if (e==m) contains=true);
      contains
    }
  /**
   * This function encodes `text` using the code tree `tree`
   * into a sequence of bits.
   * For a given Huffman tree, one can obtain the encoded representation
   * of a character by traversing from the root of the tree to the leaf 
   * containing the character. Along the way, when a left branch is chosen, 
   * a 0 is added to the representation, and when a right branch is chosen,
   * 1 is added to the representation.
   */
  def encode(tree: CodeTree)(text: List[Char]): List[Bit] = {
    var bits:List[Bit] = Nil

    def _encode(t: CodeTree, char:Char,textList:List[Char]):List[Bit]={    
    	  t match {
    		  //keep traversing, get next bit
    	  		case Fork(l,r,chars,w) => {
    	  			// see what branch contains the character
    	  			if (smartContains(char,l.chars)) {    	  			
    	  			  bits = bits ++ List(0)
    	  			    _encode(l,char,textList)  			  
    	  			}
       	            else {  	             
       	               bits = bits ++ List(1)
       	               _encode(r,char,textList)
       	            }
       	            
       	  
    	  		}
    	  	//we reached a leaf, must be the char, start again from top of the tree
    	  	case Leaf(char,w) =>  {
    	  	     if (textList!= Nil) _encode(tree,textList.head,textList.tail)
    	  	     else bits
    	  	}
    	  }
      
    }
    
   _encode(tree, text.head,text.tail);
    
  }


  // Part 4b: Encoding using code table

  type CodeTable = List[(Char, List[Bit])]
  
   /**
   * This function returns the bit sequence that represents the character `char` in
   * the code table `table`.
   */
  def codeBits(table: CodeTable)(char: Char): List[Bit] = { 
   // In order to access the two elements of a pair, you can use the accessors `_1` and `_2`:
     val h = table.head;
      if (h._1==char) h._2
      else codeBits(table.tail)(char)
    
  }
  
   /**
   * Given a code tree, create a code table which contains, for every character in the
   * code tree, the sequence of bits representing that character.
   *
   * Hint: think of a recursive solution: every sub-tree of the code tree `tree` is itself
   * a valid code tree that can be represented as a code table. Using the code tables of the
   * sub-trees, think of how to build the code table for the entire tree.
   */
  def convert(tree: CodeTree): CodeTable = {
    var table:CodeTable = Nil
    
    def calculateTable(t:CodeTree,bits:List[Bit]):CodeTable = {
      
    t match {
      case Fork(l,r,chars,w)=>{
        //pass through intermediate nodes
       
         calculateTable(l,bits ++ List(0))
         calculateTable(r,bits ++ List(1))
        
      }
      case Leaf(char,w)=>{
          val pair:(Char,List[Bit]) = (char,bits)
          val list = List(pair);
          table = table ++ list
          table
      }
    }
    }
    calculateTable(tree,Nil)
  }
    
  
  
  
  /**
   * This function takes two code tables and merges them into one. Depending on how you
   * use it in the `convert` method above, this merge method might also do some transformations
   * on the two parameter code tables.
   */
  def mergeCodeTables(a: CodeTable, b: CodeTable): CodeTable = {
    // val pair: (Char, Int) = ('c', 1)
    val newElementList:CodeTable = List(b.head) 
    
    b.tail match {
      case Nil => { a ++ newElementList}
      case _ =>{
        mergeCodeTables( a ++ newElementList,b.tail)
      }
      
    }
    
  }
  
  
   /**
   * This function encodes `text` according to the code tree `tree`.
   *
   * To speed up the encoding process, it first converts the code tree to a code table
   * and then uses it to perform the actual encoding.
   */
  def quickEncode(tree: CodeTree)(text: List[Char]): List[Bit] = { 
    val codeTable:List[(Char, List[Bit])] = convert(tree);
    
    def encodeText(t:List[Char],bits:List[Bit]):List[Bit] = {
      val bitsForHead:List[Bit] = codeBits(codeTable)(t.head)
      
      t match {
        case xs::Nil =>{
          bits ++ bitsForHead
        }
        case _=>{
          val newBitsequence = bits ++ bitsForHead
         encodeText(t.tail,bits ++ bitsForHead)
        }
      } //end match
      
    }
    
    encodeText(text,Nil)
    
  }
  
  
  /////////////////////////////////////////////////////////////////////////////

  type CodeTable2 = Map[String, List[Bit]] //making this an inmutable map
  /**
   * This function returns the bit sequence that represents the character `char` in
   * the code table `table`.
   */
  def codeBits2(table: CodeTable2)(char: Char): List[Bit] = {
      table(char.toString())
  }

  /**
   * Given a code tree, create a code table which contains, for every character in the
   * code tree, the sequence of bits representing that character.
   *
   * Hint: think of a recursive solution: every sub-tree of the code tree `tree` is itself
   * a valid code tree that can be represented as a code table. Using the code tables of the
   * sub-trees, think of how to build the code table for the entire tree.
   */
  def convert2(tree: CodeTree): CodeTable2 = {
    var table:Map[String, List[Bit]] = Map.empty;
    
    def buildCodeTable(t:CodeTree, bits:List[Bit]):CodeTable2 = {
      	  t match {
    		  //keep traversing, get next bit
    	  		case Fork(l,r,chars,w) => {
    	  		  table = table.updated(chars2String(chars),bits);
    	  		  buildCodeTable(l,bits ++ List(0))
    	  		  buildCodeTable(r,bits ++ List(1))
    	  		}
    	  		case Leaf(char,w)=>{
    	  		  //start from the top again
    	  		  table = table.updated(char.toString,bits);
    	  		  table
    	  		}
      	  }
    }
    buildCodeTable(tree,Nil)
    
  }

  

  /**
   * This function encodes `text` according to the code tree `tree`.
   *
   * To speed up the encoding process, it first converts the code tree to a code table
   * and then uses it to perform the actual encoding.
   */
  def quickEncode2(tree: CodeTree)(text: List[Char]): List[Bit] = {    
    val codeTable:Map[String,List[Bit]] = convert2(tree);
    
    def encodeText(t:List[Char],bits:List[Bit]):List[Bit] = {
      val bitsForHead:List[Bit] = codeTable(t.head.toString())
      
      t match {
        case xs::Nil =>{
          bits ++ bitsForHead
        }
        case _=>{
          val newBitsequence = bits ++ bitsForHead
         encodeText(t.tail,bits ++ bitsForHead)
        }
      } //end match
      
    }
    
    encodeText(text,Nil)
    
  }
}
