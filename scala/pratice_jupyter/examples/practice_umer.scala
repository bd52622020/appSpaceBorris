
import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.log4j._
import org.apache.spark.sql.SparkSession._
import org.apache.spark.sql.types._

object Task10 {
    def parseLine(line: String) ={
        val fields = line.split(",")
        var sID = fields(0)
        var entry = fields(2)
        var temp = fields(3).toFloat
        (sID,entry,temp)
    }
   def main(args: Array[String]) {
       //data1
       val txt = sc.textFile("1800.csv")
       val df = txt.map(parseLine)
       val min = df.filter(_._2 == "TMIN").map(x => (x._1,x._3))
       val stationMin = min.reduceByKey((x,y) => if(x < y) x else y)
       val result = stationMin.collect
       for (res <- result){
           println(res._1 + " station has temprature " + res._2 +"\n")
       }
       //data2
       val txt2 = sc.textFile("book.txt")
       val src = txt2.flatMap(line => line.split("\\W+"))
       val src2 = txt2.flatMap(line => line.split("\\W+")).map(x => (x,1)).reduceByKey((x,y) => x+y)
       val src3 = src2.collect
       src.foreach(println)
   }
}


