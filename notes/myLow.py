from pyspark import SparkConf, SparkContext

# Creates a python dictionary
# Use this to convert movie ID's to movie names
# while printing out the final results

def loadMovieNames():
	movieNames ={}
	with open("u.time", encoding= "ISO-8859-1") as f:
		for line in f:
			fields = line.split('|')
			movieNames[int(fields[0])] = fields[1]
	return movieNames

# Take each line of u.data and convert it to (movieID, (ratings, 1.0))
# This way we can add up all of the ratings for each movie, and
# the total number of ratings for each movie /which lets us compute the average

def parseInput(line):
	fields = line.split()
	return (int(fields[1]), (float(fields[2], 1.0))

if __name__ == "__main__":
	# The main script - create our SparkContext
	conf = SparkConf().setAppName("WorstMovie")
	sc = SparkContext(conf = conf)

	# Load up our movie id -> movie name lookup table
	movieNames = loadMovieNames()

	# Load up the raw u.data file
	lines = sc.textFile("u.data")

	# Convert to (movieID, (ratings, 1.0))
	movieRatings = lines.map(parseInput) #takes everyline

	# Reduce to (movieID, (sumofRatings, totalRatings))
	ratingTotalsAndCount = movieRatings.reduceByKey(lambda movie1, movie2: (movie1[0] + movie2[0] + movie1[1] + movie2[1]))

	# Map to (movieID, averageRating)
	averageRatings = ratingTotalsAndCount.mapValues(lambda totalAndCount : totalAndCount[0] / totalAndCount[1])

	# Sorted by average rating
	sortedMovies = averageRatings.sortBy(lambda x: x[1])

	# Take the top 10 results
	results = sortedMovies.take(10)

	# Print them out
	for result in results:
		print(movieNames[result[0], result[1])

