import random


class SongsQuiz:
    songs = ["Jingle Bells", "Last Christmas", "Never Gonna Give You Up", "Shape of You",
             "We Wish You a Merry Christmas"]
    usedSongs = []
    quizes = 0
    file = 0
    song = "Jingle Bells"
    TNTSS = []
    TRQ = []

    def chooseSong(self):
        self.song = random.choice(self.songs)
        self.songs.remove(self.song)

    def askQuestion(self):
        self.file = open(self.song + ".txt", "r")
        while True:
            line = self.file.readline()
            if not line:
                break
            print(line.strip())
        print()
        print("Введите название песни")

    def testNotTheSameSong(self):
        if self.song in self.usedSongs or self.song == "":
            self.TNTSS.append(0)
        else:
            self.TNTSS.append(1)
            self.usedSongs.append(self.song)

    def testRightQuestion(self):
        temp = open(self.song + ".txt", "r")
        if str(temp) == str(self.file):
            self.TRQ.append(1)
        else:
            self.TRQ.append(0)

    def testsCheck(self):
        if 0 in self.TNTSS:
            print("testNotTheSameSong: unsuccess")
        else:
            print("testNotTheSameSong: success")
        if 0 in self.TRQ:
            print("testRightQuestion: unsuccess")
        else:
            print("testRightQuestion: success")

    def main(self):
        while self.quizes != 5:
            self.chooseSong(obj)
            self.testNotTheSameSong(obj)
            self.askQuestion(obj)
            self.testRightQuestion(obj)
            self.quizes = self.quizes + 1
        self.testsCheck(obj)


obj = SongsQuiz
obj.main(obj)