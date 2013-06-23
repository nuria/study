package streams

import common._

/**
 * This component implements a parser to define terrains from a
 * graphical ASCII representation.
 * 
 * When mixing in that component, a level can be defined by
 * defining the field `level` in the following form:
 * 
 *   val level =
 *     """------
 *       |--ST--
 *       |--oo--
 *       |--oo--
 *       |------""".stripMargin
 * 
 * - The `-` character denotes parts which are outside the terrain
 * - `o` denotes fields which are part of the terrain
 * - `S` denotes the start position of the block (which is also considered
     inside the terrain)
 * - `T` denotes the final position of the block (which is also considered
     inside the terrain)
 * 
 * In this example, the first and last lines could be omitted, and
 * also the columns that consist of `-` characters only.
 */
trait StringParserTerrain extends GameDef {

  /**
   * A ASCII representation of the terrain. This field should remain
   * abstract here.
   */
  val level: String

  /**
   * This method returns terrain function that represents the terrain
   * in `levelVector`. The vector contains parsed version of the `level`
   * string. For example, the following level
   * 
   *   val level =
   *     """ST
   *       |oo
   *       |ooo""".stripMargin
   * 
   * is represented as
   * 
   *   Vector(Vector('S', 'T'), Vector('o', 'o'), Vector('o', 'o'))
   *
   * The resulting function should return `true` if the position `pos` is
   * a valid position (not a '-' character) inside the terrain described
   * by `levelVector`.
   */
  def terrainFunction(levelVector: Vector[Vector[Char]]): Pos => Boolean = {
    // let's calculate 1st how far does the game extends
    // if x or y are bigger than that they are out of the space
  
    val length:Int = levelVector.length;
 //   println("item vector length is"+length)
   
    def contained(p:Pos):Boolean = {
      
   //    println("x is"+p.x.toString);
    
      //1st check that we have at least x-1 elements
      if (p.x >= length-1 || p.x<0)  false
      else {
        //now check the y axis
        //get x elements and reverse, the element we are interested in is at the top
        val items:Vector[Vector[Char]] = levelVector.take(p.x+1).reverse;
         
        val xRow:Vector[Char] = items.head;
        if (p.y>=xRow.length-1 || p.y<0) false
        else true
              
      }
    }
    contained
  }

  /**
   * This function should return the position of character `c` in the
   * terrain described by `levelVector`. You can assume that the `c`
   * appears exactly once in the terrain as this is used to find starter and final positions
   *
   * Hint: you can use the functions `indexWhere` and / or `indexOf` of the
   * `Vector` class
   */
  def findChar(c: Char, levelVector: Vector[Vector[Char]]): Pos = {
    
         def _findChar(c: Char, levelVector: Vector[Vector[Char]],level:Int):Pos={
		  val i:Int = levelVector.head.indexOf(c)
		  if(i!= -1) new Pos(level,i)
		  else _findChar(c,levelVector.tail,level+1)
         }
         
         _findChar(c,levelVector,0)
    
  }

  private lazy val vector: Vector[Vector[Char]] =
    Vector(level.split("\n").map(str => Vector(str: _*)): _*)

  lazy val terrain: Terrain = terrainFunction(vector)
  lazy val startPos: Pos = findChar('S', vector)
  lazy val goal: Pos = findChar('T', vector)

}
