from googletrans import Translator, LANGUAGES



def Translation(text:str,lang:str,srcs:str) -> str:
    try:
        translator = Translator()
        translation = translator.translate(text, dest=lang, src='la')
        print(translation)
    except ValueError:
        return False
    else:
        return translation.text


def get_lngs() -> list:
    lang_codes, lang_names, langs = [], [], []
    for languages in LANGUAGES.items():
        lang_codes.append(languages[0])
        lang_names.append(languages[1])
        langs.append(languages)        

    return lang_codes, lang_names, langs


t = Translation("Çeviri Modülü","en","tr") #Yazı İngilizce değil ise Otomatik Çeviri DOĞRU ÇALIŞMIYOR.

if t == "Çeviri Modülü":
    print("[translate_module] Automatic Translation does NOT work CORRECTLY.")
else:
    print("[translate_module] Automatic Translation WORKS CORRECTLY.")
