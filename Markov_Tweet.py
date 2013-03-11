from sys import argv
from markov_class import *
from keys import *
import twitter

script, inputfile = argv

def main():
    order = int(raw_input("What Markov order would you like to use (1-10)? But try number 2."))
    handle = raw_input("Please enter a Twitter handle.")

    filetext = process_file()

    # The number below is determined upon the maximum length of a tweet minus the maximum
    # length of a handle.
    markov = MarkovDict(filetext, order, 123)
    markov.read_text()
    output = markov.output_text()
    print output
    tweet_output(output)

# prompt to open file
def process_file():
    f = open(inputfile)
    # read through the file
    filetext = f.read()
    f.close()
    return filetext

# Put your keys into "DO_ME_twitter_keys" file and rename the file to "keys.py"
def tweet_output(output):
    api = twitter.Api(consumer_key='key_consumer_key',
                      consumer_secret='key_consumer_secret',
                      access_token_key='key_access_token_key',
                      access_token_secret='key_access_token_secret')

    status = api.PostUpdate(output)


if __name__ == "__main__":
    main()
