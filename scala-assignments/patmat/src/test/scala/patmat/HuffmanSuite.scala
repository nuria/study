package patmat

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

import patmat.Huffman._

@RunWith(classOf[JUnitRunner])
class HuffmanSuite extends FunSuite {
  trait TestTrees {
    val t1 = Fork(Leaf('a',2), Leaf('b',3), List('a','b'), 5)
    val t2 = Fork(Fork(Leaf('a',2), Leaf('b',3), List('a','b'), 5), Leaf('d',4), List('a','b','d'), 9)
    
    val sampleTree = makeCodeTree(
    		makeCodeTree(Leaf('x', 1), Leaf('e', 1)),
    		Leaf('t', 2)
    )
    
    var sampleTree2 = makeCodeTree(
    		makeCodeTree(Leaf('a', 1), Leaf('b', 2)),
    		Leaf('c', 1)
    )
    var treeList = List(sampleTree,sampleTree2)
  }

  test("weight of a larger tree") {
    new TestTrees {
      assert(weight(t1) === 5)
      assert(weight(t2) === 9)
    }
  }
   test("sample tree weight") {
    new TestTrees {
      assert(weight(sampleTree) === 4)
     
    }
  }

  test("chars of a larger tree") {
    new TestTrees {
      assert(chars(t2) === List('a','b','d'))
      assert(chars(sampleTree) === List('x','e','t'))
    }
  }

  
  test("string2chars(\"hello, world\")") {
    assert(string2Chars("hello, world") === List('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd'))
  }

   test("happy case times(\"hello, hello\")") {
    val t = times(string2Chars("hello, hello"));
    assert(t.contains(('h',2)))
  }
   

  test("makeOrderedLeafList for some frequency table") {
    val orderedLeafList = makeOrderedLeafList(List(('t', 2), ('e', 1), ('x', 3)))
    assert(orderedLeafList === List(Leaf('e',1), Leaf('t',2), Leaf('x',3)))
  }

  test("combine of some leaf list") {
    val leaflist = List(Leaf('e', 1), Leaf('t', 2), Leaf('x', 4))
    assert(combine(leaflist) === List(Fork(Leaf('e',1),Leaf('t',2),List('e', 't'),3), Leaf('x',4)))
  }
  
  test("until of some leaf list") {
    val leaflist = List(Leaf('e', 1), Leaf('t', 2), Leaf('x', 4))
    new TestTrees {
    	val list = until(singleton,combine)(treeList)
    
    	//list should only have one element
    	assert(list.tail==Nil)
    }
  }
  
  test("Code tree creation") {
    val codeTree = createCodeTree(string2Chars("hello, world hello"))
    assert(codeTree.weight==10)
    
  }
  

  test("decode and encode a very short text should be identity") {
    new TestTrees { 
      assert(decode(t1, encode(t1)("ab".toList)) === "ab".toList)
    }
  }
  
  
  test("build code table") {
    new TestTrees { 
      val codeTable = convert(sampleTree);
      println(codeTable)
     assert(codeBits(codeTable)(string2Chars("t").head)==List(1))
  
    }
  }
  
   test("build code table using hashmap") {
    new TestTrees { 
      val codeTable = convert2(sampleTree);      
      assert(codeTable("t")==List(1))
  
    }
  }
  
}
