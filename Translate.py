from googletrans import Translator
text = input ('your text')
translator = Translator()
translated = translator.translate(text, src='en',dest='fr')
print(translated.text)
