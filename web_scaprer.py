import requests
from bs4 import BeautifulSoup
import time
from dd_post import DD_Post

URL='https://ns.reddit.com/r/wallstreetbets/search?sort=top&q=flair%3ADD&restrict_sr=on&t=day'
DD_CLASS = 'search-result search-result-link has-thumbnail has-linkflair linkflair-dd'
WSB_PREFIX = 'https://ns.reddit.com'
HEADERS = {'User-agent': 'Currently building an app'}

#FIXME: Uncomment to use with online data
# time.sleep(2)

# page=requests.get(URL, headers = HEADERS)
# print(page)

# with open('Wall-Street-Bets-DD-Tracker/page_response.txt', 'w') as outfile:
#     outfile.write(page.text)

#use while testing to avoid spamming
with open('Wall-Street-Bets-DD-Tracker/page_response.txt', 'r') as infile:
    data = infile.read()

soup = BeautifulSoup(data, 'html.parser') #FIXME: replace with page.content when launched

all_posts = soup.find('div', class_='contents')

dd_post_list = []

for dd_post in all_posts.find_all('div', {'class' : DD_CLASS}): #guarantees it's a DD post
    #TODO: Filter out posts already aggregated
    full_url = WSB_PREFIX + dd_post.find('a')['href']
    post_obj = DD_Post(full_url)

        