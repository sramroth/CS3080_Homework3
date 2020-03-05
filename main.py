###########################################################################
# Name: Scott Ramroth
# Date: March 5th, 2020
# Email: sramroth@uccs.edu
# Description: Creates a searchable "database" of movies based on given 
# csv files. Boilerplate code provided by Dr. Dana Wortman
###########################################################################

import re
import Movie
from Movie import *

###########################################################################
# Functions
###########################################################################
def printMenu(menuItems):
	menuItem = 0
	print("*" * 30)
	for item in menuItems:
		menuItem += 1
		print("%d - %s" % (menuItem, item))
	print("*" * 30)
	return promptForInteger(1, menuItem, 
						    "Please make a selection between 1 and %d:" % menuItem, 
							"Your response must be number between 1 and %d, try again." % menuItem)

def promptForInteger(minimum, maximum, message, errorMessage):
	try:
		response = int(input(message + "\n"))
	except:
		response = -1

	while (response < minimum or response > maximum):
		try:
			response = int(input(errorMessage + "\n"))
		except:
			response = -1
	return response

# Load a file with the name given by the user. 
# Ignore the first line in the file
# Create movie objects for each line in the file
def loadFile(message, movies):
	filename = input(message + "\n")
	file = open(filename, "r")
	for line in file.readlines()[1:]:
		if line.startswith("\""):
			title = line.split("\"")[1]
			data = line.split("\"")[2].split(",")
			movies.append(Movie(title, data[1], data[2], data[3], 
								[data[4], data[5], data[6]], 
								data[7], data[8], data[9].rstrip("\n")))
		else:
			data = line.split(",")
			movies.append(Movie(data[0], data[1], data[2], data[3], 
								[data[4], data[5], data[6]], 
								data[7], data[8], data[9].rstrip("\n")))

# Search the "database" for movies with the given title
def searchByTitle(message, movies):
	criteria = input(message + "\n")
	foundMovies = []
	titleRegex = re.compile(rf".*{criteria}.*", re.IGNORECASE)
	for movie in movies:
		if titleRegex.search(movie.getTitle()) != None:
			foundMovies.append(movie)
	printMovies(foundMovies)

# Search the "database" for movies with the given genre(s)
def searchByGenre(message, movies):
	criteria = input(message + "\n")
	foundMovies = []
	genreRegex = re.compile(rf".*{criteria}.*", re.IGNORECASE)
	for movie in movies:
		if genreRegex.search(movie.getGenre()) != None:
			foundMovies.append(movie)
	printMovies(foundMovies)

# Search the "database" for movies with the given director
def searchByDirector(message, movies):
	criteria = input(message + "\n")
	foundMovies = []
	directorRegex = re.compile(rf".*{criteria}.*", re.IGNORECASE)
	for movie in movies:
		if directorRegex.search(movie.getDirector()) != None:
			foundMovies.append(movie)
	printMovies(foundMovies)

# Search the "database" for movies with the given writer
def searchByWriter(message, movies):
	criteria = input(message + "\n")
	foundMovies = []
	writerRegex = re.compile(rf".*{criteria}.*", re.IGNORECASE)
	for movie in movies:
		if writerRegex.search(movie.getWriter()) != None:
			foundMovies.append(movie)
	printMovies(foundMovies)

# Search the "database" for movies with the given star
def searchByStar(message, movies):
	criteria = input(message + "\n")
	foundMovies = []
	starRegex = re.compile(rf".*{criteria}.*", re.IGNORECASE)
	for movie in movies:
		if starRegex.search(str(movie.getStars())) != None:
			foundMovies.append(movie)
	printMovies(foundMovies)

# Search the "database" for movies with running time less than
# the given running time
def searchByRunningTime(message, movies):
	criteria = input(message + "\n")
	foundMovies = []
	for movie in movies:
		if movie.getRunningTime() < int(criteria):
			foundMovies.append(movie)
	printMovies(foundMovies)

# Search the "database" for movies with the given rating, exactly
def searchByRating(message, movies):
	criteria = input(message + "\n")
	foundMovies = []
	ratingRegex = re.compile(rf"^{criteria}$", re.IGNORECASE)
	for movie in movies:
		if ratingRegex.search(str(movie.getRating())) != None:
			foundMovies.append(movie)
	printMovies(foundMovies)

# Search the "database" for movies with the given release year, exactly
def searchByReleaseYear(message, movies):
	criteria = input(message + "\n")
	foundMovies = []
	yearRegex = re.compile(rf"^{criteria}$")
	for movie in movies:
		if yearRegex.search(movie.getReleaseDate().split("/")[2]) != None:
			foundMovies.append(movie)
	printMovies(foundMovies)

# Print each movie currently in a given list, sorted by title
def printMovies(movies):
	for movie in sorted(movies, key=lambda movie: movie.getTitle()):
		print(movie)

###########################################################################
# Main
###########################################################################
movies = [ ]

response = 0
while response != 11:
	response = printMenu( [ "Load a Movie File", "Search by Title", "Search by Genre", "Search by Director", \
							"Search by Writer", "Search by Star", "Search by Running Time", \
							"Search by Rating", "Search by Release Year", "Print all Movies", "Quit" ] )

	if response == 1:
		movies = [ ]
		loadFile("Please enter the movie filename: ", movies)
	elif response == 2:
		searchByTitle("Please enter the movie title or partial title: ", movies)
	elif response == 3:
		searchByGenre("Please enter the movie genre or partial genre: ", movies)
	elif response == 4:
		searchByDirector("Please enter the Director's name or partial name: ", movies)
	elif response == 5:
		searchByWriter("Please enter the Writer's name or partial name: ", movies)
	elif response == 6:
		searchByStar("Please enter the Star's name or partial name: ", movies)
	elif response == 7:
		searchByRunningTime("Please enter the maximum running time in minutes: ", movies)
	elif response == 8:
		searchByRating("Please enter the movie rating: ", movies)
	elif response == 9:
		searchByReleaseYear("Please enter the release year: ", movies)
	elif response == 10:
		printMovies(sorted(movies, key=lambda movie: movie.getTitle()))
	elif response == 11:
		print("Quitting!")
		exit