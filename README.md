# ai_dadjokes
A program for training a neural network to generate dad jokes based on dad jokes from reddit, and for automatically posting them on instagram

Works with python 3.6.8. Comments in the files are partly in finnish, but I can translate them to english if needed

##Breakdown of the files:

###### jokegetter.py

The file downloads all dadjokes from the r/dadjokes subreddit that have more than 5 upvotes 
I manually edited the file to a standard format with VSCode, so that all the jokes are preceeded with "joke:" and have 2 line breaks after them.

###### jokegen.py

Code for training the neural network with the txt file gotten with jokegetter.py with all the dadjokes. The training process can take a lot of time, and therefore i suggest you to use eg google collabs to make the process faster. Tensorflow is used.

###### generate.py

Generates jokes based on the training. There you can adjust the temperature and lenght of the generated sample. Saves the jokes to a csv file, with each joke being separated by a comma. 

###### kuvanteko.py

Code for generating pictures with the text of the joke and a watermark. Discards jokes that are too long and would result in text too small to read.

###### postaa.py

Code for uploading the picture to instagram. Make sure you import your own file with login details.

###### follow.py

Python script for following the followers of predefined instagram accounts with the hopes of them following back using Selenium.
