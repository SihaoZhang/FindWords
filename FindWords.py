import urllib.request

class FindWords:

    def __init__(self):

        self.dict = {}
        self.output = []

    def input(self, chars):

        lowerchars = toLower(chars)

        for char in lowerchars:

            if char not in self.dict:
                self.dict[char] = 1
            else:
                self.dict[char] += 1

    def search(self, wordList):

        for word in wordList:
            if not word or word in self.output :
                continue

            temp = {}
            isWord = True

            for char in word:

                if char not in self.dict:
                    isWord = False
                    break

                if char not in temp:
                    temp[char] = 1
                else:
                    temp[char] += 1

            if not isWord:
                continue

            for char in temp:
                if temp[char] > self.dict[char]:
                    isWord = False

            if isWord:
                self.output.append(word)

def toLower(word):

    lowerWord = word.lower()

    return lowerWord

def getFromWeb(url):

    res = urllib.request.urlopen(url)
    content = res.read().decode('utf-8').split("\n")
    wordList = [toLower(word) for word in content]

    return wordList

def main(url, chars):

    if not url or not chars:
        print("Error: Parameters can not be empty.")
        return

    # Input the wordList url and charaters
    wordList = getFromWeb(url)

    # Initialize the FindWords()
    wordSearch = FindWords()

    # Initialize the input characters
    wordSearch.input(chars)


    # Search all available word in the dictionary
    wordSearch.search(wordList)
    print(wordSearch.output)

    return wordSearch.output
