import requests
from bs4 import BeautifulSoup


# This variable takes the url of an imdb movies list contains results of search or something
url_of_list_of_movies = 'https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=X7N4808F5P0QZ03TKTFJ&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_sm'


start_link = 'https://www.imdb.com'

'''
From the list of searched movies parse end-link manually.
Parsing with BeautifulSoup only provide short link
'''

end_link = '?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=FCEFQEBTN0R6YQY7R367&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1'



# With get request reterive the html content
page = requests.get(url_of_list_of_movies)
html = page.content

# BeautifulSoup parse the html and make it easy to go through the html tags
soup = BeautifulSoup(html, 'html.parser')



def middle_link(soup):
    '''Returns the list of all the "short" links of movies'''
    short_link = []

    for item in soup.find_all('td', {'class': 'titleColumn'}):
        for a in item.find_all('a'):
            short_link.append(a['href'])

    return short_link

def full_link(start_link, middle_link, end_link):
    '''Returns a list of full accessible links of movies'''
    links = []

    for link in middle_link:
        links.append(start_link + link + end_link)

    return links

'''Now save the full accessible links to a text file "urls.txt"'''
with open('urls.txt', 'w') as f:
    for url in full_link(start_link, middle_link(soup), end_link):
        f.write(url + "\n")
