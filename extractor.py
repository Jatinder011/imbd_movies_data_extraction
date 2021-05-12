# This script is made to extract movies data of top 250 Indian movies
from bs4 import BeautifulSoup
import pandas as pd
import re

import os
import glob


def extractor(html):
    '''This function takes the html file and return the dataframe of
    movie title, released year, length, genre, rating, votes, director,
    writer, stars, certificate and language'''

    soup = BeautifulSoup(html, 'lxml') # make soup by BeautifulSoup to parse the html

    raw_data = {
        'title': Title(soup),
        'year': Year(soup),
        'length': Length(soup),
        'genre': Genre(soup),
        'rating': Rating(soup),
        'votes': Votes(soup),
        'director': Director(soup),
        'writer': Writer(soup),
        'star': Star(soup),
        'language': Language(soup),
        # 'certificate': Certificate(soup)
    }

    single_moive_df = pd.DataFrame(raw_data, index=[0])

    return single_moive_df


def Title(soup):
    '''Extract Title'''
    title = soup.find('h1').get_text() # Take the movie name from h1 tag
    return (re.search('[^\(....\)]+', title).group()) # Remove the year from the title


def Year(soup):
    '''Extract movie released year'''
    for h1 in soup.find_all('h1'): # loop through the h1 tag
        for year in h1.find('a'): # loop through and find a tag containing year
            return year


def Length(soup):
    '''Extract the runtime of the movie'''
    for item in soup.find_all('div', {'class': 'subtext'}): # loop through to find all the items in subtext class of div tag
        for runtime in item.find_all('time'): # find the runtime in time tag
            return (int(re.search('\d+', runtime['datetime']).group())) # get the time in minutes and append it to list


def Genre(soup):
    '''Extract genres in a list'''
    genre = []
    
    for item in soup.find_all('div', {'class': 'subtext'}): # loop through to find all the items in subtext class of div tag
        for genres in item.find_all('a'): # loop through item to find a tags containing genre
            genre.append(genres.get_text().strip()) 

    return [', '.join(genre[:-1])] # return the genre list, removing last item


def Rating(soup):
    '''Extract imbd rating of the movie'''
    for item in soup.find_all('div', {'class': 'ratings_wrapper'}): # iterate through the rating wrapper
        for rating in item.find('span', {'itemprop': 'ratingValue'}):
            return rating


def Votes(soup):
    '''Return total number of votes of a movie'''
    for item in soup.find_all('div', {'class': 'ratings_wrapper'}): # iterate through the rating wrapper
        for votes in item.find('span', {'itemprop': 'ratingCount'}):
            return votes


def Director(soup):
    '''Returns director of the movies'''
    director = []

    for item in soup.find_all('div', {'class': 'credit_summary_item'}): # loop through the credit summary
        try:

            for h4 in item.find('h4'): # find the h4 tag

                if h4 == 'Directors:' or h4 == 'Director:':
                    for directors in item.find_all('a'): # find the a tag containing director name
                        director.append(directors.get_text())
        
        except TypeError:
            pass

    return [', '.join(director)] # return director


def Writer(soup):
    '''Returns writerof the movies'''
    writer = []

    for item in soup.find_all('div', {'class': 'credit_summary_item'}): # loop through the credit summary
        try:

            for h4 in item.find('h4'): # find the h4 tag

                if h4 == 'Writers:' or h4 == 'Writer:':
                    for writers in item.find_all('a'): # find the a tag containing writer name
                        writer.append(writers.get_text())
        
        except TypeError:
            pass

    return [', '.join(writer[:-1])] # return director


def Star(soup):
    '''Returns stars of the movies'''
    star = []

    for item in soup.find_all('div', {'class': 'credit_summary_item'}): # loop through the credit summary
        try:

            for h4 in item.find('h4'): # find the h4 tag

                if h4 == 'Stars:' or h4 == 'Star:':
                    for stars in item.find_all('a'): # find the a tag containing star name
                        star.append(stars.get_text())
        
        except TypeError:
            pass

    return [', '.join(star[:-1])] # return director


def Language(soup):
    '''Return the language of the movie'''
    language = []

    for item in soup.find_all('div', {'class': 'txt-block'}): # loop through text block

        try:

            for h4 in item.find('h4'):
                
                if h4 == 'Language:' or h4 == 'Languages:':
                    for languages in item.find_all('a'): # iterate through items to find a tag containg language
                        language.append(languages.get_text())

        except TypeError:
            pass
    
    return [', '.join(language)]


# def Certificate(soup):
#     '''Return the language of the movie'''
#     certificate = []

#     for item in soup.find_all('div', {'class': 'txt-block'}): # loop through text block

#         try:

#             for h4 in item.find('h4'):
                
#                 if h4 == 'Certificate:' or h4 == 'Certificates:':
#                     for certificates in item.find('span'): # iterate through items to find a tag containg certificate
#                         certificate.append(certificates)

#         except TypeError:
#             pass
    
#     return [', '.join(certificate)]


'''read the html files and with extractor function extract desired movie_data'''
movie_data = []
for filepath in glob.glob(os.path.join('html/*.html')):
    with open(filepath) as f:
        html = f.read()

    movie_data.append(extractor(html))

'''concatenate the movie_data list in dataframe'''
movies_df = pd.concat(movie_data)

'''write it to a .csv file'''
movies_df.to_csv('movies.csv', index=False)

