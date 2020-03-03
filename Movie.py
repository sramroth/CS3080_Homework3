class Movie():
    def __init__(self, title, genre, director, writer, stars, \
                 runningTime, rating, releaseDate):
        self.title = title
        self.genre = genre
        self.director = director
        self.stars = stars
        self.runningTime = runningTime
        self.rating = rating
        self.releaseDate = releaseDate

    # def __str__(self):
        #return  + \
               #"{}".format(self.title).ljust(55, " ") + "  |  " + \
               #"{} h {} min".format(self.getRunningTimeHours(), self.getRunningTimeMins()) + "  |  " + \
               #"{}".format(self.rating).rjust(0) + "\n" + \
               
    def getTitle(self):
        return self.title

    def getGenre(self):
        return self.genre

    def getDirector(self):
        return self.director

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

    def formatMovieInfo(self):
        if len(self.title) <= 55:
            titleLine1 = self.title
            titleLine2 = None
            titleLine3 = None
        elif len(self.title) > 55 and len(self.title) <= 90:
            line1BreakIndex = self.title.rfind(" ", 0, 55)
            titleLine1 = self.title[0:line1BreakIndex]
            titleLine2 = self.title[line1BreakIndex + 1:len(self.title)]
            titleLine3 = None
        else:
            line1BreakIndex = self.title.rfind(" ", 0, 55)
            line2BreakIndex = self.title.rfind(" ", line1BreakIndex, 90)
            titleLine1 = self.title[0:self.title.rfind(" ", 0, 55)]
            titleLine2 = self.title[line1BreakIndex + 1:line2BreakIndex]
            titleLine3 = self.title[line2BreakIndex + 1:len(self.title)]

        print(titleLine1)
        print(titleLine2)
        print(titleLine3)