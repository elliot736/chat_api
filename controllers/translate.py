import deepl 

auth_key = "967d8c88-5419-cf85-e52c-a10f9093eb3d:fx"
translator = deepl.Translator(auth_key) 

def translate2en(text, target_language = "EN-GB"):
    result = translator.translate_text(text, target_lang=target_language) 
    translated_text = result.text
    return translated_text

def translate2de(text, target_language = "DE"):
    result = translator.translate_text(text, target_lang=target_language) 
    translated_text = result.text
    return translated_text