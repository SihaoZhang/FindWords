#!/bin/bash
RESULT=$(python -c 'import FindWords; FindWords.main("https://raw.githubusercontent.com/lad/words/master/words","Absc")')
echo $RESULT


