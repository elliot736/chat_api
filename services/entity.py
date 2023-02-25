from services.tokenizer import tokenizer
import pickle

modelName = './model/entity_model.sav'
#load model
entity_model = pickle.load(open(modelName, 'rb'))
#load TfidfVectorizer
Tfidf_vect = entity_model[1]
#load Encoder
Encoder = entity_model[2]
#load SVM
SVM = entity_model[0]

def getEntity(msg):
    token= tokenizer(msg, Tfidf_vect)
    prediction = SVM.predict(token)
    result= Encoder.inverse_transform(prediction)
    return result



