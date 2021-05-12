import requests

def download_html(url):
    '''download the html content of an url'''
    html = requests.get(url)
    return html.content


'''write the downloaded html files with name "movie{n}.html" in a folder "html"'''
# open the urls.txt and read the urls one by one
try:
    with open('urls.txt') as fhand:
        for n, url in enumerate(fhand.readlines()):
            html = download_html(url)
        
                # write the html content to a file
            with open(f'html/movie_{n+1}.html', 'wb') as f:
                f.write(html)

except FileNotFoundError:
    print("The directory 'html' doesn't exist. \nPlease create 'html' folder first.")

