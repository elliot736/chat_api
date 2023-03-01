from textblob import TextBlob

def SpellCorrection(sentence):
    sentence = TextBlob(sentence)
    result = sentence.correct()
    return result
