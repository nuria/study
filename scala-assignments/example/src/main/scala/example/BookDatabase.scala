package example

object BookDatabase {
  
  def _main(args:Array[String]) = {
    val books:Set[Book]= Set(Book(title="Atlas de Madri",authors=List("pepito","juanito")),
        Book(title="Atlas de BCN",authors=List("pepita","juanita")),
        Book(title="Comiditarica",authors=List("lola","lolita")),
        Book(title="Mas comidita rica",authors=List("mama","papa")),
        Book(title="Programing in the mornings",authors=List("pepito","juanito")),
        Book(title="Programing in the evenings",authors=List("pepito","juanito"))
    );
    println(findTwoBooksAuthors(books))
    
    println(flatMap(List('1','2','3'),(x:Char) => List(x+"2")))
  }

  
  case class Book(title:String, authors:List[String]);
  
  
  
  def allWithThisWordIntheTittle(word:String,books:Set[Book]):Set[Book] = {
    
    for (b<-books if b.title.indexOf(word)>0) yield b
    
  }
  
  ///Find the name of two authors which have written at least two books
  // below code compares everything with everything
  def findTwoBooksAuthors(books:Set[Book]):Set[String] = {
    for {
      
      b1 <- books
      b2 <- books
      if b1.title < b2.title
        a1 <- b1.authors
        a2 <- b2.authors
      if a1==a2
    } yield a1
  }
  
  //write map (for lists) in terms of for 
  // although is reality goes the other way, the scala compiler transformates
  // for expressions into these
  def mapFun[U,T](list:List[U], f:U => T):List[T]= {
   
    for (x <- list) yield f(x)
    
  }
  
  def flatMap[U,T](list:List[U],f:U => Iterable[T]): List[T] = {
     for(x <- list; y <- f(x)) yield y
    
  }
  
  def filter[U](list:List[U],p:U => Boolean): List[U] = {
     for(x <- list if p(x)) yield x
    
  }
  
}