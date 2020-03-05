###########################################################################
# Name: Scott Ramroth
# Date: March 5th, 2020
# Email: sramroth@uccs.edu
# Description: Movie class definition. Creates a searchable "database" of 
# movies based on given csv files.
###########################################################################

import datetime

class Movie():
    #####################################################################
    # __init__ and __str__ 
    #####################################################################
    def __init__(self, title, genre, director, writer, stars, \
                 runningTime, rating, releaseDate):
        self.title = title
        self.genre = genre
        self.director = director
        self.writer = writer
        self.stars = stars
        self.runningTime = int(runningTime)
        self.rating = rating
        self.releaseDate = releaseDate

    def __str__(self):
        return self.formatMovieInfo() 

    #####################################################################
    # Getters 
    #####################################################################     
    def getTitle(self):
        return self.title

    def getGenre(self):
        return self.genre

    def getDirector(self):
        return self.director

    def getWriter(self):
        return self.writer

    def getStars(self):
        return self.stars

    def getRunningTime(self):
        return self.runningTime

    def getRunningTimeHours(self):
        return str(self.runningTime // 60)

    def getRunningTimeMins(self):
        return str("{:02}".format(self.runningTime % 60))

    def getRating(self):
        return self.rating

    def getReleaseDate(self):
        return self.releaseDate

    #####################################################################
    # Class Methods 
    #####################################################################

    # Turn a date in the form MM/DD/YYYY to a properly formatted string
    def formatReleaseDate(self):
        month = int(self.releaseDate.split("/")[0])
        day = int(self.releaseDate.split("/")[1])
        year = int(self.releaseDate.split("/")[2])

        return datetime.datetime(year, month, day).strftime("%B %d, %Y")

    def formatMovieInfo(self):
        # Find the breakpoints of the title (for especially long titles)
        # and format them correctly for the final string
        if len(self.title) <= 55:
            titleLine1 = self.title
            titleLine2 = ""
            titleLine3 = ""
        elif len(self.title) > 55 and len(self.title) <= 90:
            line1BreakIndex = self.title.rfind(" ", 0, 55)
            titleLine1 = self.title[0:line1BreakIndex]
            titleLine2 = self.title[line1BreakIndex + 1:len(self.title)]
            titleLine3 = ""
        else:
            line1BreakIndex = self.title.rfind(" ", 0, 55)
            line2BreakIndex = self.title.rfind(" ", line1BreakIndex, 90)
            titleLine1 = self.title[0:self.title.rfind(" ", 0, 55)]
            titleLine2 = self.title[line1BreakIndex + 1:line2BreakIndex]
            titleLine3 = self.title[line2BreakIndex + 1:len(self.title)]
        
        # Find the breakpoints of the stars list (for especially long names)
        # and format them correctly for the final string
        if len(", ".join(self.stars)) > 71:
            starsBreakIndex = ", ".join(self.stars).rfind(" ", 0, 71)
            starsLine = ", ".join(self.stars)[0:starsBreakIndex] + "\n" + (" " * 9) + \
                        ", ".join(self.stars)[starsBreakIndex + 1:len(", ".join(self.stars))]
        else:
            starsLine = ", ".join(self.stars)

        # Return a properly formatted string for easy viewing of parsed information
        return ("-" * 80) + "\n" + \
               "{}".format(titleLine1).ljust(55, " ") + "  |  " + \
               "{} h {} min".format(self.getRunningTimeHours(), self.getRunningTimeMins()) + "  |  " + \
               "{}".format(self.rating).rjust(5, " ") + "\n" + \
               "{}".format(titleLine2).ljust(35, " ") + "  |  " + \
               "Director:".ljust(10, " ") + self.director + "\n" + \
               "{}".format(titleLine3).ljust(35, " ") + "  |  " + \
               "Writer:".ljust(10, " ") + self.writer + "\n" + \
               "Genre:".ljust(9, " ") + self.genre.ljust(71, " ") + "\n" + \
               "Stars:".ljust(9, " ") + starsLine.ljust(71, " ") + "\n" + \
               "Release:".ljust(9, " ") + self.formatReleaseDate()