from textblob import TextBlob

def SpellCorrection(sentence):
    sentence = TextBlob(sentence)
    result = str(sentence.correct())
    return result
