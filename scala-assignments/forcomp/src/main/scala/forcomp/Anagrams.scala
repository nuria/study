package forcomp

import common._

object Anagrams {

  /** A word is simply a `String`. */
  type Word = String

  /** A sentence is a `List` of words. */
  type Sentence = List[Word]

  /** `Occurrences` is a `List` of pairs of characters and positive integers saying
   *  how often the character appears.
   *  This list is sorted alphabetically w.r.t. to the character in each pair.
   *  All characters in the occurrence list are lowercase.
   *  
   *  Any list of pairs of lowercase characters and their frequency which is not sorted
   *  is **not** an occurrence list.
   *  
   *  Note: If the frequency of some character is zero, then that character should not be
   *  in the list.
   */
  type Occurrences = List[(Char, Int)]

  /** The dictionary is simply a sequence of words.
   *  It is predefined and obtained as a sequence using the utility method `loadDictionary`.
   */
  val dictionary: List[Word] = loadDictionary.filter(word=>word forall (char=>char.isLetter))

  /** Converts the word into its character occurrence list.
   *  
   *  Note: the uppercase and lowercase version of the character are treated as the
   *  same character, and are represented as a lowercase character in the occurrence list.
   */
  def wordOccurrences(w: Word): Occurrences = {
     
     def getCount(c:Char,s:String,i:Int):Int={  
       if (s.isEmpty()) i
       else if (s.head.toLower == c.toLower) getCount(c,s.tail,i+1)
       else  getCount(c,s.tail,i)
       }
       
     
     val result = w.map((c:Char)=>(c.toLower,getCount(c,w,0))).toSet.toList
    //println(result)
     result.sortBy(_._1)
  }

  /** Converts a sentence into its character occurrence list. 
  Sentence=List[Word]  occurrence=List[(Char,Int)] , word is a string **/
  def sentenceOccurrences(s: Sentence): Occurrences = {
  
    def getOcurrenceListRaw(s: Sentence): Occurrences ={
    	s match {
    		case Nil => Nil
    		case xs::xt =>  wordOccurrences(xs) ++ getOcurrenceListRaw(xt)
    	}
    }

    val result = getOcurrenceListRaw(s);

    // Turn result into a map , result has duplicate entries for letters that appaer in two words
    // so "ba" "a"  "a" will return "(a,1)(a,1)(a,1)(b,1)
    // we turn that into a map
    // map a->(a,1)(a,1)(a,1) b->(b,1)
    val map = result.groupBy(_._1)
    println(map)

    //Turns map into  Map(a -> 3, b -> 1) 
    val charToIntMap = 
        for ( 
            (_key, pairlist) <- map
            
        ) yield (_key, pairlist.foldLeft(0)( (i:Int,pair:(Char,Int)) => i+pair._2))

    // this will turn into a list of tuples (a,3)(b,1)
    charToIntMap.toList.sortBy(_._1)
       
    
  }

  /** The `dictionaryByOccurrences` is a `Map` from different occurrences to a sequence of all
   *  the words that have that occurrence count.
   *  This map serves as an easy way to obtain all the anagrams of a word given its occurrence list.
   *  
   *  For example, the word "eat" has the following character occurrence list:
   *
   *     `List(('a', 1), ('e', 1), ('t', 1))`
   *
   *  Incidentally, so do the words "ate" and "tea".
   *
   *  This means that the `dictionaryByOccurrences` map will contain an entry:
   *
   *    List(('a', 1), ('e', 1), ('t', 1)) -> Seq("ate", "eat", "tea")
   *
   */
  lazy val dictionaryByOccurrences: Map[Occurrences, List[Word]] = {
    

    dictionary.groupBy(wordOccurrences).withDefaultValue(List())
    
  }

  /** Returns all the anagrams of a given word. */
  def wordAnagrams(word: Word): List[Word] = {
    dictionaryByOccurrences(wordOccurrences(word)) 
  }

  /** Returns the list of all subsets of the occurrence list.
   *  This includes the occurrence itself, i.e. `List(('k', 1), ('o', 1))`
   *  is a subset of `List(('k', 1), ('o', 1))`.
   *  It also include the empty subset `List()`.
   * 
   *  Example: the subsets of the occurrence list `List(('a', 2), ('b', 2))` are:
   *
   *    List(
   *      List(),
   *      List(('a', 1)),
   *      List(('a', 2)),
   *      List(('b', 1)),
   *      List(('a', 1), ('b', 1)),
   *      List(('a', 2), ('b', 1)),
   *      List(('b', 2)),
   *      List(('a', 1), ('b', 2)),
   *      List(('a', 2), ('b', 2))
   *    )
   *
   *  Note that the order of the occurrence list subsets does not matter -- the subsets
   *  in the example above could have been displayed in some other order.
   */
  def combinations(occurrences: Occurrences): List[Occurrences] = {
  
    //for (o <- occurrences; r<-1 to o._2) yield List((o._1,r))
		  def _inner(occurrences: Occurrences): List[Occurrences]={
				  occurrences match {
				  case Nil => List(List())
				  case x::Nil => {
					  val allAmounts = for (o <- occurrences; r<-1 to o._2) yield List((o._1,r))
					  allAmounts 
				  }
				  case xs::xt => {
					  // all combinations for the tail elements
					  val possibilities: List[Occurrences] = _inner(xt);

				  // single items will have [('a',1)('a',2)] for a xs=('a',2) 
				  val headPossibilities = _inner(List(xs)) 

						  //combinations of possibilties + headPossibilities 
						  val inclusive:List[Occurrences] = for (h <- headPossibilities; p <-possibilities if !possibilities.isEmpty ) yield (h ++ p)


						  val result:List[Occurrences] =  headPossibilities ++ inclusive ++ possibilities 
						  //println(result)
						  result 

				  }

				  }
		  } 
		  
	if (occurrences.isEmpty) List(List())
	else _inner(occurrences) ++ List(List())
    
  }
  
  // something going on with the method name, had to aliase it
  // remove combinations of 1 element with (x,1) as those do not lead to any words 
  def _combinations(o:Occurrences):List[Occurrences] = {
    
    combinations(o).filter((ol:Occurrences)=> (!(( ol.length ==1) && ( ol.head._2==1))) )
    
  }

  /** Subtracts occurrence list `y` from occurrence list `x`.
   * 
   *  The precondition is that the occurrence list `y` is a subset of
   *  the occurrence list `x` -- any character appearing in `y` must
   *  appear in `x`, and its frequency in `y` must be smaller or equal
   *  than its frequency in `x`.
   *
   *  Note: the resulting value is an occurrence - meaning it is sorted
   *  and has no zero-entries.
   */
  def subtract(x: Occurrences, y: Occurrences): Occurrences = {
    val letters:List[Char] = for (pair <- x ) yield(pair._1)
    val xFreq:Map[Char,Int] = x.toMap
    val yFreq:Map[Char,Int] = y.toMap;
  
    // the fact that map works that way is kind of amazing
    val reducedFreqMap:Map[Char,Int] = xFreq.map {case(k,v)=> (k, v - yFreq.getOrElse(k,0))}
    
    def rebuild(c:Char):(Char,Int)={
      (c,reducedFreqMap.getOrElse(c,0))
    }
    //now map letters and filter if freq is zero
     letters.map(rebuild).filter(_._2>0)
    
  }

  /** Returns a list of all anagram sentences of the given sentence.
   *  
   *  An anagram of a sentence is formed by taking the occurrences of all the characters of
   *  all the words in the sentence, and producing all possible combinations of words with those characters,
   *  such that the words have to be from the dictionary.
   *
   *  The number of words in the sentence and its anagrams does not have to correspond.
   *  For example, the sentence `List("I", "love", "you")` is an anagram of the sentence `List("You", "olive")`.
   *
   *  Also, two sentences with the same words but in a different order are considered two different anagrams.
   *  For example, sentences `List("You", "olive")` and `List("olive", "you")` are different anagrams of
   *  `List("I", "love", "you")`.
   *  
   *  Here is a full example of a sentence `List("Yes", "man")` and its anagrams for our dictionary:
   *
   *    List(
   *      List(en, as, my),
   *      List(en, my, as),
   *      List(man, yes),
   *      List(men, say),
   *      List(as, en, my),
   *      List(as, my, en),
   *      List(sane, my),
   *      List(Sean, my),
   *      List(my, en, as),
   *      List(my, as, en),
   *      List(my, sane),
   *      List(my, Sean),
   *      List(say, men),
   *      List(yes, man)
   *    )
   *
   *  The different sentences do not have to be output in the order shown above - any order is fine as long as
   *  all the anagrams are there. Every returned word has to exist in the dictionary.
   *  
   *  Note: in case that the words of the sentence are in the dictionary, then the sentence is the anagram of itself,
   *  so it has to be returned in this list.
   *
   *  Note: There is only one anagram of an empty sentence.
   */
  def sentenceAnagrams(sentence: Sentence): List[Sentence] = {
    
    //sentence -> List[Word]
    val occurrences:Occurrences = sentenceOccurrences(sentence);
    
    val dictionaryMapByOcurrences:Map[Occurrences,List[Word]] = dictionaryByOccurrences;
    
    // I think I need an intermediate function
    
    var anagrams:List[Sentence] = Nil
    
     def convertIntoWords( originalOccurrence:Occurrences, wordList:List[Word],combinations:List[Occurrences]):Unit = {   
        
       // println("list of combinations")
      //  println(combinations)
        
        combinations match {
          
          case xs::Nil =>{
            //successful retrieval of words ,base case we are done
            if (xs.isEmpty && originalOccurrence.isEmpty) {
            	anagrams = anagrams ++ List(wordList)
            	
            } 
          }
          case xs::xt => {
            val possibleWords = dictionaryMapByOcurrences(xs); 
            //println("possible words for")
            //println(xs)
            //println(possibleWords)
            val newOccurrence:Occurrences = subtract(originalOccurrence,xs)
            convertIntoWords(originalOccurrence,wordList,xt)
            
            
            
            for (
            		w <- possibleWords          	
            ) yield convertIntoWords(newOccurrence,List(w) ++ wordList,_combinations(newOccurrence))
                 
                 
            	
            
          } //end case
          
        } //end match
        
        
      
    }
 
    def dedupe(l:List[Sentence]):List[Sentence] = {
      l match {
        case Nil => l
        case xs::xt =>  xs:: dedupe(xt.filter((s:Sentence)=>(s!=xs)))
             
      } 
    }
    convertIntoWords(occurrences,List(),_combinations(occurrences))    
    dedupe(anagrams)
  }
  
  
  
  

}
