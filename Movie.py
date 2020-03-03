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

    def __str__(self):
        return ("-" * 80) + "\n" + \
               "{}".format(self.title).ljust(55, " ") + "  |  " + \
               "{} h {} min".format(self.getRunningTimeHours(), self.getRunningTimeMins())

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