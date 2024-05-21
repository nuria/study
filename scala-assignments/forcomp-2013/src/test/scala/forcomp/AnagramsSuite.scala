package forcomp

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

import Anagrams._

@RunWith(classOf[JUnitRunner])
class AnagramsSuite extends FunSuite {

  test("wordOccurrences: abcd") {
    assert(wordOccurrences("abcd") === List(('a', 1), ('b', 1), ('c', 1), ('d', 1)))
  }

  test("wordOccurrences: Robert") {
    assert(wordOccurrences("Robert") === List(('b', 1), ('e', 1), ('o', 1), ('r', 2), ('t', 1)))
  }

   test("wordOccurrences: Repeated letters mama") {
    assert(wordOccurrences("mama") === List(('a', 2), ('m', 2)))
  }


  test("sentenceOccurrences: abcd e") {
    assert(sentenceOccurrences(List("abcd", "e")) === List(('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)))
  }
  test("sentenceOccurrences: Repeated letters papa  mama") {
    val result:Occurrences = sentenceOccurrences(List("papa", "mama"))
    println(result)
    assert( result === List(('a', 4), ('m', 2), ('p', 2)) )
  }

  test("dictionaryByOccurrences.get: eat") {
    assert(dictionaryByOccurrences.get(List(('a', 1), ('e', 1), ('t', 1))).map(_.toSet) === Some(Set("ate", "eat", "tea")))
  }



  test("word anagrams: married") {
    assert(wordAnagrams("married").toSet === Set("married", "admirer"))
  }

  test("word anagrams: player") {
    assert(wordAnagrams("player").toSet === Set("parley", "pearly", "player", "replay"))
  }


    test("combinations: []") {
    assert(combinations(Nil) === List(Nil))
  }

     test("combinations: one element") {
       val output = List(List(),List(('a',1)));
       val input = List(('a', 1))
       assert(combinations(input).toSet === output.toSet)
  }
    
    test("combinations: 2 elements") {
       val input = List(('a',1),('b',1));
       val output = List(List(('a',1), ('b',1)), List(('a',1)), List(('b',1)), List())
       val result = combinations(input).toSet
       assert(result.toSet === output.toSet)
  }
    
    
    
  test("combinations: abba") {
    val abba = List(('a', 2), ('b', 2))
    val abbacomb = List(
      List(),
      List(('a', 1)),
      List(('a', 2)),
      List(('b', 1)),
      List(('a', 1), ('b', 1)),
      List(('a', 2), ('b', 1)),
      List(('b', 2)),
      List(('a', 1), ('b', 2)),
      List(('a', 2), ('b', 2))
    )
    val result = combinations(abba).toSet;

    assert(combinations(abba).toSet === abbacomb.toSet)
  }

  test("_combinations without (x,1) pair: abba") {
    val abba = List(('a', 2), ('b', 2))
    val abbacomb = List(
      List(),     
      List(('a', 2)),
      List(('a', 1), ('b', 1)),
      List(('a', 2), ('b', 1)),
      List(('b', 2)),
      List(('a', 1), ('b', 2)),
      List(('a', 2), ('b', 2))
    )
    val result = _combinations(abba).toSet;
   

    assert(_combinations(abba).toSet === abbacomb.toSet)
  }
  
  

  test("subtract: lard - r") {
    val lard = List(('a', 1), ('d', 1), ('l', 1), ('r', 1))
    val r = List(('r', 1))
    val lad = List(('a', 1), ('d', 1), ('l', 1))
    assert(subtract(lard, r) === lad)
  }
  

 test("subtract: olive") {
    val olive = List(('o', 1), ('l', 1),('i',1),('v',1),('e',1))
    val r = List(('r', 1))
    val o2 = List(('o', 1))
    val live = List(('l', 1),('i',1),('v',1),('e',1))
    
    assert(subtract(olive, r) === olive)
    assert(subtract(olive, o2) === live)
  }

  test("sentence anagrams: []") {
    val sentence = List()
    assert(sentenceAnagrams(sentence) === List(Nil))
  }

   
   
   test("sentence anagrams: ") {
    val sentence = List("yes","man")
    val l = sentenceOccurrences(sentence);
  
    //for (c <- combinations(l)) yield println(c)

// val l = List(('s',1),('a',1),('n',1),('e',1));
   // val l=List(('s',1),('a',1))
     //println(combinations(l))
    //println(combinations(wordOccurrences("sane")))
    
   val result = sentenceAnagrams(sentence);
  // println(result)
    //assert(sentenceAnagrams(sentence) != List(Nil))
  }
   
   
   test("anagrams: yes ,man"){
     
     val sentence = List("yes","man")
     val result = sentenceAnagrams(sentence);
     
     val output = List(
        List("en", "as", "my"),
        List("en", "my", "as"),
        List("man", "yes"),
        List("men", "say"),
        List("as", "en", "my"),
        List("as", "my", "en"),
        List("sane", "my"),
        List("Sean", "my"),
        List("my", "en", "as"),
        List("my", "as", "en"),
        List("my", "sane"),
        List("my", "Sean"),
        List("say", "men"),
        List("yes", "man")
      )
     
      assert(output.toSet == result.toSet)
   }
    

  test("sentence anagrams: Linux rulez") {
    val sentence = List("Linux", "rulez")
    val anas = List(
      List("Rex", "Lin", "Zulu"),
      List("nil", "Zulu", "Rex"),
      List("Rex", "nil", "Zulu"),
      List("Zulu", "Rex", "Lin"),
      List("null", "Uzi", "Rex"),
      List("Rex", "Zulu", "Lin"),
      List("Uzi", "null", "Rex"),
      List("Rex", "null", "Uzi"),
      List("null", "Rex", "Uzi"),
      List("Lin", "Rex", "Zulu"),
      List("nil", "Rex", "Zulu"),
      List("Rex", "Uzi", "null"),
      List("Rex", "Zulu", "nil"),
      List("Zulu", "Rex", "nil"),
      List("Zulu", "Lin", "Rex"),
      List("Lin", "Zulu", "Rex"),
      List("Uzi", "Rex", "null"),
      List("Zulu", "nil", "Rex"),
      List("rulez", "Linux"),
      List("Linux", "rulez")
    )
    println(anas.toSet)
   
    println(sentenceOccurrences(List("Linux", "rulez")))
   
  }  

}
