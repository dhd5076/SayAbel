from sayabel import markov
from sayabel.core.main import red_con_instance


def generate_title(subreddit, post_count):
    post_list = red_con_instance.get_hot_posts(subreddit, post_count)
    title_chain = markov.MarkovChain()

    for post in post_list:
        title_chain.train(post.title)

    return title_chain.generate()

def generate_custom_philo(file_name_list):
    gen_philo_chain = markov.MarkovChain()
    for file_name in file_name_list:
        gen_philo_chain.train(open(file_name))

def from_file_list(file_name_list):
    chain = markov.MarkovChain()
    for file_name in file_name_list:
        chain.train(open(file_name).read())

def generate_plato():
    text_file = open('philo/plato-phaedrus-clean')
    text_data = text_file.read()
    text_data += open('philo/plato-the-republic').read()
    text_data += open('philo/plato-sophist-dirty').read()
    output_chain = markov.MarkovChain()

    output_chain.train(text_data)
    return output_chain.generate()
