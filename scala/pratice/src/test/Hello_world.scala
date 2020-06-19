package test
/*
 * This is the main object of my application
 */
object Hello_world {
  
  def buildList(): List[String] = {
    val input = readLine()
    if ( input == "quit") Nil
    else input :: buildList()
  }
  
  def concat_string(words: List[String]): String ={
    if (words.isEmpty) ""
    else words.head + concat_string(words.tail)
  }
  
  def concat_string_pat(words: List[String]): String = words match{
    case Nil => ""
    case h :: t =>  h.head + concat_string_pat(t)
  }
  
  /*
   * This is the main method for the application
   */
  def main(args: Array[String]): Unit = {
    println("What is your name?")
    val name = readLine()
    println("How old are you?")
    val age = readInt()
        
    val lst = buildList()
    println(concat_string(lst))
  }
}