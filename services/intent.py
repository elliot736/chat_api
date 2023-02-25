import pickle
from services.tokenizer import tokenizer
modelName = './model/intent_model.sav'
intent_model = pickle.load(open(modelName, 'rb'))
#load TfidfVectorizer
Tfidf_vect = intent_model[1]
#load Encoder
Encoder = intent_model[2]
#load SVM
SVM = intent_model[0]

def getIntent(msg):
    token= tokenizer(msg, Tfidf_vect)
    prediction = SVM.predict(token)
    result= Encoder.inverse_transform(prediction)
    return result



