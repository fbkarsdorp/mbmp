#! /usr/env/python

from mbmp import MBMA

# initialize a classifier. By doing this within a so-called
# 'with' environment, we can be sure that in case of any unexpected
# errors, the connection to the server is closed and the TimblServer is
# killed.
with MBMA() as classifier:
    # iterate every line in file
    for id,line in enumerate(open('example_words.txt')):
        # strip and then split the line at a tab
        word = line.strip()
        if len(word.split()) == 1: # filter multi-word-units
            print '# {0} {1}:\n'.format(id, word)
            # classify the given word
            result = classifier.classify(word)
            # parse the given outcomes using a CKY Parser
            trees = list(classifier.trees(result))
            if trees:
                for i,tree in enumerate(trees, mrepr='lemmas-and-tokens'):
                    # strip op lexical information of POS-tags
                    print '   {0} {1}'.format(i, tree.pprint(margin=800))
            else:
                print '   {0} {1}'.format(0, classifier.pprint_parse(result))
