package example

// Place eight queens in a chessboard 8*8 so no queen is threatened 
// by another
// once we have placed k-1c queens we would place k queen in a place where 
// is not threatened by any other.
// each queen must have its own colum/row and diagonal
object Queen {

  
  def main(args:Array[String]){
    println(nqueens(4))
  }
  
  
  def nqueens(n:Int):Set[List[Int]]={
    
    def isSafe(col:Int,queens:List[Int]):Boolean= {
      val row = queens.length;
      val queensWithRow = (row-1 to 0 by -1) zip queens
      queensWithRow.forall {
        case (c,r) => col != c && Math.abs(c-col)!= row-r
      }
      
      
    }
    
    def placeQueens(k:Int):Set[List[Int]] = {
      if (k==0) Set(List())
      else {
        for {
          queens <- placeQueens(k-1) // this is a list of ints
          col <- 0 until n
          if isSafe(col,queens)
        } yield col :: queens
      }
    }
    placeQueens(n)
  }
  
}