from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from langdetect import detect
from translate import Translator

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    
)
@app.post("/CMSAI/TranslateLongSynopsis")
def translateLongSynopsis(inputLongSynopsis: str, targetLanguages: List[str] = []):
    
    # Mapping dictionary for language codes to language names
    language_names = {
    'chinese': 'zh',
    'malay': 'ms',
    'english': 'en',
    'indonesian': 'id',
    'filipino':'fil'
                    }

    translations = {}
    detected_language = detect(inputLongSynopsis)

    for targetLanguage in list(set(targetLanguages)):
      #try:- handle any exception for language_name/
      try:
        languageCode = language_names.get(targetLanguage.strip().lower(), 'en') #if any language is unknown, use english language

        #any language outside this is considered to be defaulted in 'English'
        translator = Translator(provider='mymemory', from_lang = detected_language, to_lang=languageCode)
        translation = translator.translate(inputLongSynopsis)
        translations[targetLanguage] = translation

      except AttributeError:
        continue;

    return translations