import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

authenticator = IAMAuthenticator(API_KEY)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
translator.set_service_url(URL)


def translate_english_to_french(english_text):
    """
    Translate English text to French

    :param english_text: English text to be translated
    :type english_text: str
    :return: Translated French text
    :rtype: str
    """
    response = translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    french_text = response['translations'][0]['translation']
    return french_text


def translate_french_to_english(french_text):
    """
    Translate French text to English

    :param french_text: French text to be translated
    :type french_text: str
    :return: Translated English text
    :rtype: str
    """
    response = translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    english_text = response['translations'][0]['translation']
    return english_text
