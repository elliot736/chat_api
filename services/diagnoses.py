import json
db = open('./services/db.json', 'r')

data = json.load(db)

def getDiagnoses (entity, intent):
    entity = entity[0]
    intent = intent[0]
    diagnoses= data[entity][intent]
    # print(entity, intent)
    return diagnoses

# print(getDiagnoses('printer', 'performance'))


    