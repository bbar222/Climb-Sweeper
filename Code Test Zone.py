highScoreFile = open("highscore.txt", "r")
a = highScoreFile.readline()
highScoreFile.close()
print(a)