from dd_post import DDPost
import secret

from collections import Counter
import praw
import re

import pickle

STOP_LIST = {'DD', 'COVID', 'TLDR', 'IF', 'PUTS', 'AND', 'OR', 'TO', 'WHAT', 'US', 'USA'}


def filter_ticker_symbol(post):
    words = post.body.split() 
    sans_special_chars = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in words] #gets rid of special characters
    caps = [re.sub('[^A-Z]+', '', _) for _ in sans_special_chars] #filters for capital letters
    ticker_symbols = [s for s in caps if len(s) > 1 and len(s) <= 4 and s not in STOP_LIST]
    c = Counter(ticker_symbols)
    to_return = []
    for tuple in c.most_common(): #only get capital words that fit above criteria and are mentioned multiple times
        if tuple[1] >= 3:
            to_return.append(tuple[0])

    return to_return


REDDIT = praw.Reddit(client_id=secret.client_id,
                     client_secret=secret.secret,
                     user_agent= secret.user_agent)

WSB = REDDIT.subreddit('wallstreetbets')

posts = []

for dd_post in WSB.search('flair:DD', time_filter='day', sort='top', limit=10): #FIXME: remove limit when not testing
    #TODO: Filter out posts already aggregated
    if (len(dd_post.selftext) != 0):
        post_obj = DDPost(dd_post)
        posts.append(post_obj)

# FIXME: used for testing
# with open('Wall-Street-Bets-DD-Tracker/post_objs.pickle', 'wb') as out:
#     pickle.dump(posts, out)

# posts = pickle.load(open('Wall-Street-Bets-DD-Tracker/post_objs.pickle', 'rb')) #FIXME: remove when done testing

for post in posts:
    print(filter_ticker_symbol(post))

