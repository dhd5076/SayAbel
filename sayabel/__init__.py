from sayabel.markov import *
from sayabel.reddit import *

def Speak():
    chain = MarkovChain()
    for post in reddit.get_post_list("funny", Sort.HOT):
        chain.train(post.title)
    print(chain.generate(10))