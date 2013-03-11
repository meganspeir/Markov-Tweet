import random

class MarkovDict(object):

    def __init__(self, text, order, output_count):
        self.text = text
        self.order = order
        self.seed_counts = {}
        self.output_count = output_count


#read through filetext to count frequencies based on markov order
    def read_text(self):

        words = self.text.split()

        index = 0
        bound = len(words) - (self.order + 1)

        for token in self.text:
            seed = tuple(words[index:index+self.order])
            next_word = words[index+self.order]

            if seed in self.seed_counts:
                self.seed_counts[seed].append(next_word)

            else:
                self.seed_counts[seed] = [next_word]

            index += 1
            if index == bound:
                return self.seed_counts

# find the most frequent seed
    def define_seed(self):
        maximum = 0

        for seed in self.seed_counts:
            if len(self.seed_counts[seed]) > maximum:
                maximum = len(self.seed_counts[seed])
                start_seed = seed
        return start_seed

# write markov text given a number of characters for output
    def output_text(self):

        start_seed = self.define_seed()
        size = len(" ".join(start_seed))

# TODO Replace the handle with a twitter handle you would like to send your Markov
# text to. Also, would be nice to prompt the user for a twitter handle...eventually.
        output_list = list(start_seed)
        twitter_handle = handle

        while(True):
            if size > self.output_count:
                break

            if start_seed in self.seed_counts:
                random_index = random.randint(0, len(self.seed_counts[start_seed]) -1) # generate a random number constrained by size of the list

                output_list.append(self.seed_counts[start_seed][random_index]) # add new character to the output string
                size += (1 + len(self.seed_counts[start_seed][random_index]))
                start_seed = tuple(output_list[-self.order:])

        return twitter_handle + " ".join(output_list)[0:self.output_count]

