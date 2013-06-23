package example

object Water {

  def main(args:Array[String]) = {
    val problem = new Pouring(Vector(4,9))
    println(problem.moves)
    println(problem.pathSets.take(3).toList)
    println(problem.solutions(6))
    
  }
  /**
   * We are going to generate all possible move sequences by tiers
   * and stop when we get to the desired state
   */
  class Pouring(capacity:Vector[Int]) {
    
    //let's work on states first, states are vectors of integers really
    type State = Vector[Int];
    
    // initial state is all empty glasses
    // so we will have a vector with the same length as the capacity one
    // but with all zeros
    val initialState:State = capacity.map(x=>0) 
    
    trait Move {
      def change(s:State):State
    }
    case class Empty(glass:Int) extends Move {
      //updated returns a copy of the vector with one updated element 
      def change(s:State) = s.updated(glass,0)
    }
    case class Filled(glass:Int) extends Move {
      def change(s:State) = s.updated(glass,capacity(glass))
      
    }
    case class Pour(from:Int,to:Int) extends Move {
      def change(s:State) = {
        // amount is the smallest of the free space of the glass into which we pour
        // and the amount of the glass we pour from
        val amount = s(from) min capacity(to)-s(to)
        
        
        s.updated(from,s(from)-amount).updated(to,s(to)+amount)
      }
      
    }
    
    val glasses = 0  until capacity.length
    
    //generate the set of moves
    val emptyMoves = (for (g <- glasses) yield Empty(g)) 
    val filledMoves =  (for (g <- glasses) yield Filled(g)) 
    val pourMoves =  (for (from <-glasses; to<-glasses if from!=to) yield(Pour(to,from)))
    
    val moves = emptyMoves ++ filledMoves ++ pourMoves
    
    // now let's go for paths
    // which are sequences of moves 
    // last move in the path comes 1st in the history list
    class Path(history:List[Move])  {
      
      //what state does it lead to?
      def endState:State = trackState(history)
      def _endState = (history foldRight initialState) (_ change _)
      def trackState(xs:List[Move]):State = {
        xs match {
          case Nil => initialState
          case move::t => move change trackState(t)
          
        }
        
      }
      
      def extend(move:Move):Path = new Path(move::history)
      
      override def toString = (history.reverse mkString " ")+"-->" +endState
     
 
    }
    
      val initialPath = new Path(Nil);
      
      
      /** now how do we generate the paths **/
      //make sure not to walk repeated paths
      def from(paths:Set[Path],explored:Set[State]):Stream[Set[Path]] = 
        if (paths.isEmpty ) Stream.empty;
        else {
          val more = for {
            path <-paths
          //for each path we generate a new one by extending the current path
            // for each of the possible moves we apply that operation extend to the path 
            //and it gives us a new path
            next <- moves.map(path.extend)
            if !(explored contains next.endState)
          } yield next
          paths #::from(more,explored++ (more.map(_.endState)))
        }  
      
      
      val pathSets = from(Set(initialPath),Set(initialState)) //all paths of length 1 that start with initial path, second pass
    		  								// all paths of length 2 that starts with the path one.. etc
      
      
      def solutions(target:Int):Stream[Path] = {
        for {
          pathSet <- pathSets;
          path <- pathSet
          if path.endState contains target
        } yield path
        
      }
  }     
}