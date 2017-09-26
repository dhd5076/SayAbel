from sayabel.markov import *
from sayabel.reddit import *
from sayabel.gui import *


def Speak(subreddit):
    chain = MarkovChain()
    for post in reddit.get_post_list(subreddit, Sort.HOT):
        chain.train(post.text)
    print(chain.generate())
