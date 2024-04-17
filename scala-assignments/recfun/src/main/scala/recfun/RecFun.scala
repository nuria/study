package recfun

object RecFun extends RecFunInterface:

  def main(args: Array[String]): Unit =
    println("Pascal's Triangle")
    for row <- 0 to 10 do
      print(s"${_pascal(row)} ")
      println()

  /** adding two lists
    */

  def addList(l1: List[Int], l2: List[Int]): List[Int] = (l1, l2) match {
    case (_, Nil)             => Nil
    case (Nil, _)             => Nil
    case (h1 :: l1, h2 :: l2) => (h1 + h2) :: addList(l1, l2)

  }

  /** returns rows at n for pascal triangle * */
  def _pascal(n: Int): List[Int] = {

    if n == 0 then {
      List(1)
    } else if n == 1 then {
      List(1, 1)
    } else {

      /** shift prior row and add so we add 0 1 2 1 and 1 2 1 0 to get 1 3 3 1 *
        */
      val shiftLeft: List[Int] = 0 :: _pascal(n - 1)
      val shiftRight: List[Int] = _pascal(n - 1) ::: List(0)
      addList(shiftLeft, shiftRight)
    }
  }

  /** Exercise 1
    */
  def pascal(c: Int, r: Int): Int = {

    def find(c: Int, l: List[Int]): Int = {
      if c == 0 then l.head
      else find(c - 1, l.tail)
    }

    find(c, _pascal(r))

  }

  /** Exercise 2
    */
  def balance(chars: List[Char]): Boolean = {

    // use a counter to represents the number of "("
    def _balance(n: Int, chars: List[Char]): Boolean = {

      // if there are no more "("
      if chars.isEmpty then
        n == 0
        /// mmm.. not sure this addresses it all
      else if chars.head == '(' && !chars.tail.isEmpty then
        _balance(n + 1, chars.tail)
      else if chars.head == ')' then _balance(n - 1, chars.tail)
      else _balance(n, chars.tail)
    }

    _balance(0, chars)

  }

  /** Exercise 3
    */
  def countChange(money: Int, coins: List[Int]): Int = {

    def _count(money: Int, coins: List[Int]): Int = {
      if (money == 0) 0
      else if (coins.isEmpty) 0
      else {
        var h = coins.head;
        var t = coins.tail;
        if (h > money) 0
        else if (money == h) 1
        else countChange(money - h, coins) + countChange(money, t)
      }
    }

    // cheating? this is sorting which is really iterating on linked list
    _count(money, coins.sorted)

  }
