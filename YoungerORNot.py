import nltk
from nltk.tokenize import word_tokenize

def YongerORNot():
    def analysisYongerWordsCount(words):
        yonger_words = ["lit", "slay", "goals", "savage", "fomo", "farm", "salty", "thirsty", "extra"]

        yonger_word_count = {}
        count = 0
        for word in yonger_words:
            yonger_word_count[word] = 0

        for word in words:
            a = word.lower()
            if a in yonger_words:
                count += 1
                yonger_word_count[a] += 1
        print("total: " + str(count))

        for word, count in yonger_word_count.items():
            print(word + ": " + str(count))

    def Abbreviations(words):

        abbreviations = ['u', 'r', 'lol', 'tbh', 'idk', 'ig', 'omg', 'rn', 'btw' 'fomo'] # 例えば、'u'は'you'の略、'r'は'are'の略、'lol'は'laugh out loud'の略

        count = 0
        for word in words:
            a = word.lower()
            if a in abbreviations:
                count += 1

        print("Number of abbreviations and acronyms：", count)


    

    with open('younger.txt', 'r') as file:
        text = file.read()
    words = word_tokenize(text)

    analysisYongerWordsCount(words)
    Abbreviations(words)

YongerORNot()
