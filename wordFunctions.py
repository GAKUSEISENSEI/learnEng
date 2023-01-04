import config

def getWord(number):
    with open(config.pathToFile, "r") as file:

        for i in range(number):
            if i == number - 1:
                return file.readline(20).rstrip()
            else:
                file.readline(20)