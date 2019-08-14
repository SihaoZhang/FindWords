# FindWords

**FindWords is a function to output all the possible English words from a specific dictionary that could be composed of input characters.**

Language: **Python**
Packages: **urllib**
Environment：**Windows, Linux**
Files: **FindWords.py, runme.sh, TestCase.txt**


## FindWords.py
### main(url, chars)
+ Parameters:
    + **url**(String): the array of integers--dictionary url
    + **chars**(String): input characters
+ Output:
    + **output**(List): all possible words

### getFromWeb(url)
+ Parameters:
    + **url**(String): the array of integers--dictionary url
+ Output:
    + **wordList**(List): word dictionary

### toLower(word):
+ Parameters:
    + **word**(String): word
+ Output:
    + **lowerWord**(String): word in lower case

### FindWords:
#### input(chars):
+ Parameters:
    + **chars**(String): input characters
+ Output: None

#### search(wordList):
+ Parameters:
    + **wordList**(List): word dictionary
+ Output: None

#### self.dict(Dict):
To store the frequency of each character in the input characters.

#### self.output(List):
To store all the possible English words.

## How to run
`./runme.sh`