import datetime
class Movie():
    def __init__(self, title, genre, director, writer, stars, \
                 runningTime, rating, releaseDate):
        self.title = title
        self.genre = genre
        self.director = director
        self.writer = writer
        self.stars = stars
        self.runningTime = runningTime
        self.rating = rating
        self.releaseDate = releaseDate

    def __str__(self):
        return self.formatMovieInfo() 

               
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
        return str(self.runningTime % 60)

    def getRating(self):
        return self.rating

    def getReleaseDate(self):
        return self.releaseDate

    def formatReleaseDate(self):
        month = int(self.releaseDate.split("/")[0])
        day = int(self.releaseDate.split("/")[1])
        year = int(self.releaseDate.split("/")[2])

        return datetime.datetime(year, month, day).strftime("%B %d, %Y")

        

    def formatMovieInfo(self):
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
        
        if len(", ".join(self.stars)) > 71:
            starsBreakIndex = ", ".join(self.stars).rfind(" ", 0, 71)
            starsLine = ", ".join(self.stars)[0:starsBreakIndex] + "\n" + (" " * 9) + \
                        ", ".join(self.stars)[starsBreakIndex + 1:len(", ".join(self.stars))]
        else:
            starsLine = ", ".join(self.stars)

        return ("-" * 80) + "\n" + \
               "{}".format(titleLine1).ljust(55, " ") + "  |  " + \
               "{} h {} min".format(self.getRunningTimeHours(), self.getRunningTimeMins()) + "  |  " + \
               "{}".format(self.rating).rjust(0) + "\n" + \
               "{}".format(titleLine2).ljust(35, " ") + "  |  " + \
               "Director:".ljust(10, " ") + self.director + "\n" + \
               "{}".format(titleLine3).ljust(35, " ") + "  |  " + \
               "Writer:".ljust(10, " ") + self.writer + "\n" + \
               "Genre:".ljust(9, " ") + "|".join(self.genre).ljust(71, " ") + "\n" + \
               "Stars:".ljust(9, " ") + starsLine.ljust(71, " ") + "\n" + \
               "Release:".ljust(9, " ") + self.formatReleaseDate()