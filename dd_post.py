import requests
from bs4 import BeautifulSoup

HEADERS = {'User-agent': 'Currently building an app'}

class DD_Post:

    def __init__(self, url):
        self.url = url
        self.post_body = self.get_post_body(self.url)


    def get_post_body(self, url):
        post_page = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(post_page.content, 'html.parser')

        post_body = soup.find_all('div', {'class' : 'md'})[1]

        return post_body
