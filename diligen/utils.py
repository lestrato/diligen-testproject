from re import sub
from collections import Counter

def parse_text(text_input):
    '''
    Given a string parameter 'text_input', parse through this parameter, finding
    and returning most frequent N words and N word pairs and list them.
    Excludes all the non-word characters such as symbols, punctuation, etc.
    Two words are not a pair if there is a line break between them.

    Total runtime complexity: O(n)
    '''
    # split the string into an array on all non-word characters
    word_list = sub("[^\w]", " ",  text_input).split()

    # enumerate all distinct words
    single_word_counts = Counter(word_list).items() # O(n) time

    # get all consecutive pairs of words
    double_word_pairs = [word_list[i]+' '+word_list[i+1] for i in range(len(word_list)-1)] # O(n) time
    # enumerate all distinct pairs of words
    double_word_counts = Counter(double_word_pairs).items() # O(n) time

    return single_word_counts, double_word_counts
