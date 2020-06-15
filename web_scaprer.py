import praw
from dd_post import DDPost
import secret

REDDIT = praw.Reddit(client_id=secret.client_id,
                     client_secret=secret.secret,
                     user_agent= secret.user_agent)

WSB = REDDIT.subreddit('wallstreetbets')

posts = []

for dd_post in WSB.search('DD', time_filter='day', sort='top', limit=4): #FIXME: remove limit when not testing
    #TODO: Filter out posts already aggregated
    post_obj = DDPost(dd_post)
    posts.append(post_obj)