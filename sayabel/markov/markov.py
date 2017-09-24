from random import randint


class MarkovChain():
    def __init__(self):
        self.wordlist = []

    def train(self, training_data):
        words_to_process = training_data.split(' ')
        for i, word in enumerate(words_to_process):
            if(i < len(words_to_process) - 1):
                self.wordlist.append([word, words_to_process[i + 1]])
            else:
                self.wordlist.append([word, ''])

    def clear_data(self, start, length_of_output):
        self.wordlist = []

    def generate(self, length_of_output):
        output = self.wordlist[0][0]
        next_word = output
        output += " "
        while length_of_output > 0:
            next_word = str(self.get_next_word(next_word))
            output += next_word + " "
            if next_word == "":
                break
        return output

    def get_next_word(self, word):
        words_to_choose_from = []

        for i, word_to_eval in enumerate(self.wordlist):
            if word == word_to_eval[0]:
                words_to_choose_from.append(self.wordlist[i][1])
        return words_to_choose_from[randint(0, len(words_to_choose_from) - 1)]
