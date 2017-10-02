from sayabel import markov
from sayabel.core.main import red_con_instance


def generate_title(subreddit, post_count):
    post_list = red_con_instance.get_hot_posts(subreddit, post_count)
    title_chain = markov.MarkovChain()

    for post in post_list:
        title_chain.train(post.title)

    return title_chain.generate()
