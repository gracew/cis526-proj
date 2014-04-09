#!/usr/bin/env python
import optparse
import glob
import os
import sys
from collections import defaultdict

optparser = optparse.OptionParser()
optparser.add_option("-d", "--data", dest="data", default="data/train")
optparser.add_option("-t", "--test", dest="test", default="data/test")
opts = optparser.parse_args()[0]

# frequencies maps from language --> probability of each word in that language
lang_map = {}

for file in glob.glob(opts.data + "/*"):
    lang_name = os.path.basename(file)
    text_arr = open(file).read().lower().split()
    total_num_words = len(text_arr)
    frequencies = defaultdict(float)
    for word in text_arr:
        frequencies[word] += 1.0
    for word in frequencies:
        frequencies[word] = frequencies[word] / total_num_words
    lang_map[lang_name] = frequencies


for i, line in enumerate(open(opts.test)):
    word_arr = line.lower().split()
    # print line
    lang_guess = ''
    highest_prob = 0.0
    for lang in lang_map:
        current_prob = 0.0
        for word in word_arr:
            if word in lang_map[lang]:
                if (current_prob == 0.0):
                    current_prob = 1.0
                current_prob = current_prob * lang_map[lang][word]
        # print lang, current_prob
        if current_prob > highest_prob:
            highest_prob = current_prob
            lang_guess = lang
    # print 'WINNER'
    print lang_guess
