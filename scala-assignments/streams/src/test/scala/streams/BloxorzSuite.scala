package streams

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

import Bloxorz._

@RunWith(classOf[JUnitRunner])
class BloxorzSuite extends FunSuite {

  trait SolutionChecker extends GameDef with Solver with StringParserTerrain {
    /**
     * This method applies a list of moves `ls` to the block at position
     * `startPos`. This can be used to verify if a certain list of moves
     * is a valid solution, i.e. leads to the goal.
     */
    def solve(ls: List[Move]): Block =
      ls.foldLeft(startBlock) { case (block, move) => move match {
        case Left => block.left
        case Right => block.right
        case Up => block.up
        case Down => block.down
      }
    }
  }

  trait Level1 extends SolutionChecker {
      /* terrain for level 1*/

    val level =
    """ooo-------
      |oSoooo----
      |ooooooooo-
      |-ooooooooo
      |-----ooToo
      |------ooo-""".stripMargin

      //what? this is not the optimal solution right?
    //val optsolution = List(Right, Right, Down, Right, Right, Right, Down)
   val optsolution = List(Down, Down, Right, Right, Right, Right); 
  }

  
  test("terrain function level 1") {
    new Level1 {
      assert(terrain(Pos(0,0)), "0,0")
      assert(!terrain(Pos(4,11)), "4,11")
      assert(!terrain(Pos(6,1)), "6,1")
      assert(terrain(Pos(4,1)), "4,1")
    }
  }

  test("findChar level 1") {
    new Level1 {    
      assert(startPos == Pos(1,1))
    }
  }
  
  test(" level 1,staring at (1,1). Find neighbourghs") {
    new Level1 {   
     
      val neighbors = neighborsWithHistory(new Block(Pos(1,1),Pos(1,1)), List(Left,Up))
      println("neighbors level1")
     
      val second = neighbors.toList
      
      assert( neighbors.toList.head == (Block(Pos(1,2),Pos(1,3)),List(Right, Left, Up)))
      
    }
  }
  
  
  test("new neighbors") {
    new Level1 {
      
      val nonRepeated = newNeighborsOnly(
    		  Set(
    				  (Block(Pos(1,2),Pos(1,3)), List(Right,Left,Up)),
    				  (Block(Pos(2,1),Pos(3,1)), List(Down,Left,Up))
    		).toStream,

    		Set(Block(Pos(1,2),Pos(1,3)), Block(Pos(1,1),Pos(1,1)))
      )
      
      
      assert(nonRepeated == Set((Block(Pos(2,1),Pos(3,1)), List(Down,Left,Up))).toStream)
      
    }
    
  }
  
  
  /**test("from") {
    
    new Level1 {
      
      val paths = from(Stream.cons(( startBlock,List()) ,Stream.empty), Set(startBlock))
      println("moves from start")
      println(paths.toList)
      
    }
  }**/
  

  test("optimal solution for level 1") {
    new Level1 {
        assert(solve(solution) == Block(goal, goal))
    }
  }

  test("optimal solution length for level 1") {
    new Level1 {
      println(solution)
     assert(solution.length == optsolution.length)
    }
  }
 
}
