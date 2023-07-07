"""
    Language Translator 
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    English to french string translation 
    """
    french_text = MyMemoryTranslator(source='en', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    French to English string translation 
    """
    english_text = MyMemoryTranslator(source='french', target='en').translate(french_text)
    return english_text