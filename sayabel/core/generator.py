from sayabel import markov
from sayabel.core.main import red_con_instance


def generate_post_title(subreddit, post_count):
    post_list = red_con_instance.get_hot_posts(subreddit, post_count)
    title_chain = markov.MarkovChain()

    for post in post_list:
        title_chain.train(post.title)

    return title_chain.generate()


def generate_post_text(subreddit, post_count):
    post_list = red_con_instance.get_hot_posts(subreddit, post_count)
    title_chain = markov.MarkovChain()

    for post in post_list:
        title_chain.train(post.text)

    return title_chain.generate()


def from_file_list(file_name_list):
    chain = markov.MarkovChain()
    for file_name in file_name_list:
        chain.train(open(file_name).read())
    return chain.generate()
