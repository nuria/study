package streams

import common._
import com.sun.xml.internal.ws.server.sei

/**
 * This component implements the solver for the Bloxorz game
 */
trait Solver extends GameDef {

  /**
   * Returns `true` if the block `b` is at the final position
   */
  def done(b: Block): Boolean = {
    b.isStanding && b.b1.equals(goal);//TODO too simple?
  }

  /**
   * This function takes two arguments: the current block `b` and
   * a list of moves `history` that was required to reach the
   * position of `b`.
   * 
   * The `head` element of the `history` list is the latest move
   * that was executed, i.e. the last move that was performed for
   * the block to end up at position `b`.
   * 
   * The function returns a stream of pairs: the first element of
   * the each pair is a neighboring block, and the second element
   * is the augmented history of moves required to reach this block.
   * 
   * It should only return valid neighbors, i.e. block positions
   * that are inside the terrain.
   * 
   */
  def neighborsWithHistory(b: Block, history: List[Move]): Stream[(Block, List[Move])] = {
  // Do not get why it returns a stream cause ad most we would have 4 neighbors
   val legalMoves:List[(Block, Move)] = b.legalNeighbors:List[(Block, Move)];
   
   def makeStream(legal:List[(Block, Move)]): Stream[(Block, List[Move])] = {
     
	legal match {
	  case Nil => Stream.Empty
	  case xs::xt => Stream.cons((legal.head._1, legal.head._2 :: history),makeStream(legal.tail))
	}	   
     
    		    
    }
   
     makeStream(legalMoves);
  }

  /**
   * This function returns the list of neighbors without the block
   * positions that have already been explored. We will use it to
   * make sure that we don't explore circular paths.
   */
  def newNeighborsOnly(neighbors: Stream[(Block, List[Move])],
                       explored: Set[Block]): Stream[(Block, List[Move])] = {
    
    def _filter(neighbor: (Block, List[Move]))={
    	!explored.contains(neighbor._1)
    }
    
    neighbors.filter(_filter(_))  
    
    
  }

  /**
   * The function `from` returns the stream of all possible paths
   * that can be followed, starting at the `head` of the `initial`
   * stream.
   * 
   * The blocks in the stream `initial` are sorted by ascending path
   * length: the block positions with the shortest paths (length of
   * move list) are at the head of the stream.
   * 
   * The parameter `explored` is a set of block positions that have
   * been visited before, on the path to any of the blocks in the
   * stream `initial`. When search reaches a block that has already
   * been explored before, that position should not be included a
   * second time to avoid cycles.
   * 
   * The resulting stream should be sorted by ascending path length,
   * i.e. the block positions that can be reached with the fewest
   * amount of moves should appear first in the stream.
   * 
   * Note: the solution should not look at or compare the lengths
   * of different paths - the implementation should naturally
   * construct the correctly sorted stream.
   */
  def from2(initial: Stream[(Block, List[Move])],
           explored: Set[Block]): Stream[(Block, List[Move])] = {
    
    //First DO check for empties    
    if (initial == Stream.empty) Stream.empty
    
     
    val newNeighbors:Stream[(Block, List[Move])] = for (      
      i <- initial;
      
      // how do we do here to increment explored properly ?, we are using the same 'explored'
      // in all iterations
      neighbor <- newNeighborsOnly(neighborsWithHistory(i._1,i._2),explored)
      
      
    ) yield neighbor
      
       
    if (newNeighbors == Stream.empty){
      //no more neighbors to explore, conclude
      initial
    } else {
      //need to add all new nodes (block positions) to explored,so need to convert stream to a set????      
      val newExplored = _addNodesToExploredSet( newNeighbors, explored);
      
      val paths = initial ++ newNeighbors
    
      
     
      initial ++ newNeighbors ++ from(newNeighbors,newExplored) 
    }
 
  }
  
  /** auxiliary function to increment explored, probably this can be prettier with for syntax **/
    def _addNodesToExploredSet( newNodes:Stream[(Block, List[Move])], exploredSet:Set[Block]):Set[Block] = {     
      if (newNodes == Stream.empty){
        exploredSet
      } else if (!exploredSet.contains(newNodes.head._1)) {
        val newExploredNode:Block = newNodes.head._1;
        _addNodesToExploredSet(newNodes.tail, Set(newExploredNode) ++ exploredSet)
      }else {
        _addNodesToExploredSet(newNodes.tail,  exploredSet)
      }
    }
  
  
  // def from(paths:Set[Path],explored:Set[State]):Stream[Set[Path]] = 
     
     def from(initial: Stream[(Block, List[Move])],
           explored: Set[Block]): Stream[(Block, List[Move])] = {
    
        if (initial.isEmpty ) Stream.empty;
        else {
          val more = for {
            path <-initial
          //for each path we generate a new one by extending the current path
            // for each of the possible moves we apply that operation extend to the path 
            //and it gives us a new path
            next <- newNeighborsOnly(neighborsWithHistory(path._1,path._2),explored)
            
          } yield next
          initial ++ from(more,_addNodesToExploredSet(more,explored))
        } 
     }
  /**
   * The stream of all paths that begin at the starting block.
   */
  lazy val pathsFromStart: Stream[(Block, List[Move])] = from(Stream.cons(( startBlock,List()) ,Stream.empty), Set(startBlock))

  /**
   * Returns a stream of all possible pairs of the goal block along
   * with the history how it was reached.
   */
  //I think this is a subset of the paths from pathsFromStart that reach the goal
  // will be of this form for level1
  //Set((Block(Pos(4,7),Pos(4,7)),List(Down, Down, Right, Right, Right, Right)),
  //(Block(Pos(4,7),Pos(4,7)),List(Right, Right, Down, Down, Right, Right)), (Block(Pos(4,7),Pos(4,7)),List(Right, Right, Right, Right, Down, Down)))

  lazy val pathsToGoal: Stream[(Block, List[Move])] = {
    //lazy val goal: Pos = findChar('T', vector)
    def _filterPathIncludesGoal(pair:(Block, List[Move])):Boolean = {
      val block:Block = pair._1;        
      if ( block.isAtPositionStanding(goal)) true
      else false
    }
    pathsFromStart.filter(_filterPathIncludesGoal(_));
  }

  /**
   * The (or one of the) shortest sequence(s) of moves to reach the
   * goal. If the goal cannot be reached, the empty list is returned.
   *
   * Note: the `head` element of the returned list should represent
   * the first move that the player should perform from the starting
   * position.
   */
  lazy val solution: List[Move] = {
    if (pathsToGoal.isEmpty) List()
    
      
     val paths:List[ List[Move]] = pathsToGoal.toList.map(_._2)
     //now find the shortest
    
     def findShortest(remaining:List[List[Move]],shortest:List[Move]):List[Move] = {
       // see length of new head element
      remaining match {
        case Nil => shortest
        case xs:: xt => {
        		if (xs.length < shortest.length) findShortest(xt, xs)
        		else findShortest(xt, shortest)
        }
      }
      
    }
    
     
    findShortest(paths.tail, paths.head)
    
  }
}
