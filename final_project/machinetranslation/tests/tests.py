import unittest
from translator import translate_french_to_english, translate_english_to_french

class TestTranslationFunctions(unittest.TestCase):
    def test_translate_french_to_english_equal(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"

        result = translate_french_to_english(french_text)

        self.assertEqual(result, expected_english_text)

    def test_translate_french_to_english_not_equal(self):
        french_text = "Bonjour"
        unexpected_english_text = "Hi"

        result = translate_french_to_english(french_text)

        self.assertNotEqual(result, unexpected_english_text)

    def test_translate_english_to_french_equal(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"

        result = translate_english_to_french(english_text)

        self.assertEqual(result, expected_french_text)

    def test_translate_english_to_french_not_equal(self):
        english_text = "Hello"
        unexpected_french_text = "Salut"

        result = translate_english_to_french(english_text)

        self.assertNotEqual(result, unexpected_french_text)

if __name__ == '__main__':
    unittest.main()
