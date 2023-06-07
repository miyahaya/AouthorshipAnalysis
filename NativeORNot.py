import nltk
from nltk.tokenize import word_tokenize

def  NativeORNot():
    with open('native.txt', 'r') as f:
        non_native_text = f.read()

    non_native_words = word_tokenize(non_native_text)

    non_native_vocab = set(non_native_words)

    num_non_native_words = len(non_native_words)
    num_non_native_vocab = len(non_native_vocab)

    print("Word count is " + format(num_non_native_words) + ". Word counts excluding duplicates is " + format(num_non_native_vocab) + ".")
    print("The more duplicates there are, the more likely they are not native.")

NativeORNot()