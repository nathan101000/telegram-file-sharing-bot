import unittest
from telegram-file-sharing-bot.bot.file_manager import get_file_by_id

class TestFileManager(unittest.TestCase):
    def test_get_file_by_id(self):
        self.assertIsNotNone(get_file_by_id("some_file_id"))

if __name__ == '__main__':
    unittest.main()
