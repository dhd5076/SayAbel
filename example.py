# NOTE: This function will eventually be the entry to the program, but is currently being used to test functions.
from sayabel.core import generator

# TODO: Setup this file to be the main script


def main():
    #print(generator.generate_title('TIFU', 1000))
    print(generator.from_file_list(['sayabel/texts/biblio/king-james']))

if __name__ == '__main__':
    main()
