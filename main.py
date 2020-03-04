
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

def loadFile(message, movies):
	filename = input(message + "\n")
	file = open(filename, "r")
	# TODO: read in the file contents and create movies from the content

def searchByTitle(message, movies):
	criteria = input(message + "\n")
	# TODO: search the movies by title where criteria is the user's search term

def searchByGenre(message, movies):
	criteria = input(message + "\n")
	# TODO: search the movies by genre where criteria is the user's search term

def searchByDirector(message, movies):
	criteria = input(message + "\n")
	# TODO: search the movies by director where criteria is the user's search term

def searchByWriter(message, movies):
	criteria = input(message + "\n")
	# TODO: search the movies by writer where criteria is the user's search term

def searchByStar(message, movies):
	criteria = input(message + "\n")
	# TODO: search the movies by star where criteria is the user's search term

def searchByRunningTime(message, movies):
	criteria = input(message + "\n")
	# TODO: search the movies by running time where criteria is the user's search term

def searchByRating(message, movies):
	criteria = input(message + "\n")
	# TODO: search the movies by rating where criteria is the user's search term

def searchByReleaseYear(message, movies):
	criteria = input(message + "\n")
	# TODO: search the movies by release year where criteria is the user's search term

def printMovies(movies):
	# TODO: print all of the movies in the parameter's list
	pass

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