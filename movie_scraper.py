import requests
import json
from bs4 import BeautifulSoup

RESULTS_PER_PAGE = 50
MAXIMUM_RESULTS = 1000
base_url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=1980-01-01,1989-12-31&countries=us'
scraper_runing = True
movie_data = []
page_start_value = '01'

while(scraper_runing):
    url_addition = f'&start={page_start_value}&ref_=adv_nxt'
    url = f'{base_url}{url_addition}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_items = soup.find_all('div', class_='lister-item-content')
    for item in movie_items:
        try:
            title = item.find('h3', class_='lister-item-header').find('a').text.strip()
        except AttributeError:
            continue

        try:
            release_year = item.find('span', class_='lister-item-year').text.strip('()')
        except AttributeError:
            release_year = 'N/A'

        try:
            rating = item.find('span', class_='certificate').text.strip()
        except AttributeError:
            rating = 'N/A'

        try:
            runtime = item.find('span', class_='runtime').text.strip()
        except AttributeError:
            runtime = 'N/A'

        try:
            description = item.find_all('p', class_='text-muted')[-1].text.strip()
        except AttributeError:
            description = 'N/A'

        try:
            director = item.find('p', class_='').find_all('a')[0].text.strip()
        except AttributeError:
            director = 'N/A'

        try:
            genre = item.find('span', class_='genre').text.strip()
        except AttributeError:
            genre = 'N/A'

        try:
            stars_tag = item.find('p', class_='').find_all('a')
            stars = [a.text.strip() for a in stars_tag[1:]]
        except AttributeError:
            stars = 'N/A'

        movie_data.append({
            'Title': title,
            'Release Year': release_year,
            'Rating': rating,
            'Runtime': runtime,
            'Description': description,
            'Director': director,
            'Genre': genre,
            'Stars': ', '.join(stars)
        })
    
    next_page = int(page_start_value) + RESULTS_PER_PAGE
    page_start_value = str(next_page)
    if int(page_start_value) > MAXIMUM_RESULTS:
        scraper_runing = False
 
with open('movie_data.json', 'w') as json_file:
    json.dump(movie_data, json_file)
print(f'{len(movie_data)} movies have been scraped and added.')