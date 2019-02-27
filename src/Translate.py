# -*- coding: utf-8 -*-

import yaml, os, requests

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class Translator:

    languages = {
        "English": "en",
        "Arabic": "ar",
        "Bulgarian": "bg",
        "Catalan": "ca",
        "Chinese Simplified": "zh-CHS",
        "Chinese Traditional": "zh-CHT",
        "Czech": "cs",
        "Danish": "da",
        "Dutch": "nl",
        "Estonian": "et",
        "Finnish": "fi",
        "French": "fr",
        "German": "de",
        "Greek": "el",
        "Haitian Creole": "ht",
        "Hebrew": "he",
        "Hindi": "hi",
        "Hmong Daw": "mww",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Klingon": "tlh",
        "Klingon (pIqaD)": "tlh-Qaak",
        "Korean": "ko",
        "Latvian": "lv",
        "Lithuanian": "lt",
        "Malay": "ms",
        "Maltese": "mt",
        "Norwegian": "no",
        "Persian": "fa",
        "Polish": "pl",
        "Portuguese": "pt",
        "Romanian": "ro",
        "Russian": "ru",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Spanish": "es",
        "Swedish": "sv",
        "Thai": "th",
        "Turkish": "tr",
        "Ukrainian": "uk",
        "Urdu": "ur",
        "Vietnamese": "vi",
        "Welsh": "cy"
    }

    def __init__(self):
        # Getting the key from tab Keys on Azure portal
        self._key = "TRANSLATE_KEY"
        self.config()
        url4authentication = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        headers4authentication = {'Ocp-Apim-Subscription-Key': self.key}
        resp4authentication = requests.post(url4authentication, headers=headers4authentication)
        self._token = 'Bearer ' + resp4authentication.text
        self._speech_num = 0

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def speech_num(self):
        return self._speech_num

    @speech_num.setter
    def speech_num(self, value):
        self._speech_num = value

    def config(self):
        with open("data/config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        self.key = cfg['API'][self.key]

    def translate(self, to, text, come=None):
        url4translate = 'https://api.microsofttranslator.com/v2/http.svc/Translate'
        if come != None:
            params = {'appid': self._token, 'text': text, 'from': come, 'to': to}
        else:
            params = {'appid': self._token, 'text': text, 'to': to}
        headers4translate = {'Accept': 'application/xml'}
        resp4translate = requests.get(url4translate, params=params, headers=headers4translate)
        parsed_html = BeautifulSoup(resp4translate.text, features="lxml")
        return parsed_html.find('string').text

    def text_to_speech(self, language, text):
        url4texttospeech = 'https://api.microsofttranslator.com/v2/http.svc/Speak'
        headers4translate = {'Accept': 'application/xml'}
        params = {'appid': self._token, 'text': text, 'language': language, 'format': 'audio/wav'}
        resp4texttospeech = requests.get(url4texttospeech, params=params, headers=headers4translate)

        filename = "data/audio/speech%s.wav" % self.speech_num
        self.speech_num += 1
        with open(filename, "wb") as file:
            file.write(resp4texttospeech.content)

        print ("Speech saved to %s" % filename)
        sys.stdout.flush()

