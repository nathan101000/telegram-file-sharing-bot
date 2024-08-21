import unittest
from telegram-file-sharing-bot.bot.keyboards import get_artist_keyboard

class TestKeyboards(unittest.TestCase):
    def test_get_artist_keyboard(self):
        keyboard = get_artist_keyboard()
        self.assertIsNotNone(keyboard)

if __name__ == '__main__':
    unittest.main()
