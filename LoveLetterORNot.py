#Read me. nltkのインポート部分とAnalysisLoveLetter():の部分をそのまま引用してくれればプログラム動きます。サンプルテキストはletter.txtとpaper.txtです。
#This is program to analysis love letter or not.
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer


def LoveLetterORNot():
    #感情分析　Analysis sentimental
    def analysisSentiment(text):
        sia = SentimentIntensityAnalyzer()
    
        total = 0 #Compundｍのトータルスコア
        count = 0 #カウント回数

        for sentence in sentences:
            total += sia.polarity_scores(sentence)['compound']
            count += 1
        return total/count

    #愛情表現を表す単語の出現回数 Number of occurrences of words expressing affection
    def analysisLoveWordsCount(words):
        love_words = ["love", "adore", "miss", "forever", "want", "happiness", "worry", "everything", "always", "kiss", "words", "together", "beloved", "eternal", "support", "hold hands"]

        love_word_count = {}
        count = 0
        for word in love_words:
            love_word_count[word] = 0

        for word in words:
            a = word.lower()
            if a in love_words:
                count += 1
                love_word_count[a] += 1
        print("total: " + str(count))
        for word, count in love_word_count.items():
            print(word + ": " + str(count))
    #output
    with open('loveletter.txt', 'r') as file:
        text = file.read()
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    print("In cace love letter")
    print("compound = " + str(analysisSentiment(sentences)))
    analysisLoveWordsCount(words)

    print(" ")

    print("In cace paper")
    with open('paper.txt', 'r') as file:
        text = file.read()
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    print("compound = " + str(analysisSentiment(sentences)))
    analysisLoveWordsCount(words)

LoveLetterORNot()