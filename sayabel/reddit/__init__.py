import os
import praw
from configparser import ConfigParser

class RedditConnection:

    def __init__(self):
        self.parser = ConfigParser()
        if config_created() is False:
            self.create_config(True)
        else:
            self.process_config(True)
        self.praw_instance = praw.Reddit(client_id = self.parser.get('Auth', 'client_id'),
                                         client_secret = self.parser.get('Auth', 'client_secret'),
                                         user_agent = self.parser.get('Auth', 'user_agent'))

    def create_config(self, command_line):
        if command_line:
#TODO Check Inputs
            client_id = input("Client ID: ")
            client_secret = input("Client Secret: ")
            user_agent = input("User Agent: ")

            self.parser.add_section('Auth')
            self.parser.set('Auth', 'client_id', client_id)
            self.parser.set('Auth', 'client_secret', client_secret)
            self.parser.set('Auth', 'user_agent', user_agent)
            self.parser.write(open('.config/reddit_auth.ini', 'w'))
            self.process_config(command_line)

    def process_config(self, command_line):
        if command_line:
            self.parser.read('.config/reddit_auth.ini')


    def get_hot_posts(self, subreddit, post_count):
        return self.praw_instance.subreddit(subreddit).hot(limit=post_count)


    def get_top_posts(self, subreddit, post_count):
        return self.praw_instance.subreddit(subreddit).top(limit=post_count)


def config_created():
    return os.path.isfile('.config/reddit_auth.ini')