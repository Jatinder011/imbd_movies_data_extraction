## IMDb data extraction
Extract the data from movies page and create a dataframe and save it in a .csv file

I write these programs to extract data for TOP RATED INDIAN MOVIES, but I believe these can be used to extract other data from imdb site.

## This repo includes three scripts:
1. url_generator.py
2. html_reteriver.py
3. extractor.py


### url_generator.py
This script takes url of search query and return a txt file with all the urls of the movies in that search query.

### html_reteriver.py
This script return the html files of each url and save in them in a folder called "html".

### extractor.py
This script get the data about:

1. Movie Title
2. Year of release
3. Length of the movie in minutes
4. Genre
5. Imdb rating
6. Votes 
7. Director/s of the movie
8. Writer/s of the moive
9. Star cast
10. Language

### Working

#### STEP I
if you want to get data from multiple imdb pages
-get the url(s) and manually add the urls in a text file "urls.txt"
or
- run "url_generator.py" script to create a text file with all the urls

#### STEP II
send requests with "html_reteriver.py" to the each url in "urls.txt" and reterive html content to further parse the desired data.

#### STEP III
with "extractor.py" parse the desired data in the form a csv file "movies.csv".