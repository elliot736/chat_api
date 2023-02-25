from services.tokenizer import tokenizer
from services.entity import getEntity
from services.intent import getIntent
from services.diagnoses import getDiagnoses
def pipeline(msg):
    
    entity = getEntity(msg)
    intent = getIntent(msg)
    diagnoses = getDiagnoses(entity, intent)
    # print(entity, intent)
    return diagnoses

