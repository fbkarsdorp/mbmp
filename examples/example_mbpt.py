## Example showing functionality of the memory-based part of speech tagger.
## This tagger is trained on the lemmata from the WNT and can therefor be
## used for historical materials. However, since it is only trained on
## lemmata, performance may drop if you try to classify tokens.

from mbmp import MBPT

# intialize the MBPT classifier. Do this within a 'with' environment
# to make sure that in case of any unexpected errors, the connection
# to the server and the server itself are automatically closed.
with MBPT() as classifier:
    # iterate every line in file
    for id,line in enumerate(open('example_words.txt')):
        word = line.strip()
        # try to predict the part of speech category
        pos = classifier.classify(word)
        print '# {0} {1}: {2}'.format(id, word, pos)
