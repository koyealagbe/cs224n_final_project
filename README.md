# CS 224N Final Project: Comparison of NLP Models for a Writer and Genre Style Controlled Movie Screenplay Generator

An NLP model that generates movie screenplays based on genre and director style

This project was done using the resources of Stanford University and the staff of CS 224N. 

To run this project:
1) Run data/scraper.py which will scrape from the IMSDB website to retreive all the screenplays to a dataset.txt file and outputs all the special tokens of <director name> <genre> into the special-tokens.txt file.
2) Run data/data_splitter.py which will split the data into a train, dev, and test datasets written into files.
3) Run data/strip_html.py passing in those files outputted above as arguments in the command line. This program will output three stripped train, dev, and test files. 
4) Then you should have all the dataset files as well as the special-tokens file which can be uploaded to the notebook in models/BuildMovieScreenplayGenerator.ipynb and this notebook can be run in order. 
  
Hope you enjoy our work!
