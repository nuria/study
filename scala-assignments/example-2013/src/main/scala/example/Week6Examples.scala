package example

import scala.io.Source;

object Week6Examples {
  
  
  def main (args:Array[String])={
    println(charCode)
    
   println( wordCode("JAVA"))
   println(wordCode("JAva"))
   println(wordsForNum)
  }
  
  /** given a phone number return the "phrases" it could represent **/
  /** right , you need a dictionary**/
  val men:Map[Char,String] = Map(
      '2'->"ABC",
      '3'->"DEF",
      '4'->"GHI",
      '5'->"JKL",
      '6'->"MNO",
      '7'->"PQRS",
      '8'->"TUV",
      '9'->"WXYZ"
      );

  val in = Source.fromURL("http://lamp.epfl.ch/files/content/sites/lamp/files/teaching/progfun/linuxwords.txt")

  val words:List[String] = in.getLines().toList.filter(word=>word forall (char=>char.isLetter))
  
  /** invert map so from chars you can get to the numbers **/
  
  val charCode: Map[Char,Char]= for ((_key, string) <- men;letter <- string) yield (letter, _key)
    
    
  /** maps a string of  with the number you could represent  "Java" -> 5282 **/
  //Attention, using a hash like a function to map the array
  def wordCode(word:String):String = word.toUpperCase().map(charCode)
  
  /** A map of nums and strings that represent them 5282->List("java", "lava", ..) **/
  val wordsForNum: Map[String, Seq[String]] = words.groupBy(wordCode).withDefaultValue(Seq())
  
  /** Return all ways to encode a number as a list of words **/
  /// FOR BASED RECURSION !!!!
  def encode(number:String):Set[List[String]] = {
    // split num in chuncks that can represent words
    if (number.isEmpty()) Set(List())
    else {
      for {
        split <- 1 to number.length()
        word <- wordsForNum(number take split)
        rest<- encode (number drop split)
      } yield(word::rest)
    }.toSet
  }
  encode("7225247386");
}