from enum import Enum
import requests

import json

class Sort(Enum):
    TOPALL = "/top/?sort=top&t=all"
    TOPYEAR = "/top/?sort=top&t=year"
    NEW = "/new/"
    HOT = "/"

class Post:
    def __init__(self, title, link, text):
        self.title = title
        self.link = link
        self.text = text


def get_post_list(subreddit, sort):
    raw_response = requests.get("https://www.reddit.com/r/" + subreddit + "/.json",
                                headers = {'User-Agent': 'Sayabel Bot'})
    json_data = raw_response.json()
    post_list = []
    for post in json_data['data']['children']:
        post = post['data']
        post_list.append(Post(post['title'], post['url'], post['selftext']))
    return post_list

def get_comment_list(post):
    pass