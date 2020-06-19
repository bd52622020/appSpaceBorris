

package object test {
  
  val name:String = "Pat Cook"
  val value:Int = 42
  val age:Double = 33.6
  val isit:Boolean = true
  var year = 23
  year += 1
  val t = (1, 2.55, "Heru")
  val (a, b ,c) = t
  val square = (x:Double) => x * x
  println(square(2))
  val less_than: (Double, Double) => Boolean = _ < _
  
  val fizzbuzz = for(i <- 1 to 20) yield {
    (i%3, i%5) match{
      case (0, 0) => "fizzBuzz"
      case (0, _) => "fizz"
      case (_, 0) => "buzz"
      case _ => i.toString
    }
  }
  
  
  
}