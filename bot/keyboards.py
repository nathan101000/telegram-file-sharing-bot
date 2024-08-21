from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Sample data structure
artists = ['Artist1', 'Artist2']

def get_artist_keyboard():
    """Returns a keyboard with a list of artists."""
    keyboard = [[InlineKeyboardButton(artist, callback_data=artist)] for artist in artists]
    return InlineKeyboardMarkup(keyboard)

def get_release_keyboard(artist_name):
    """Returns a keyboard with a list of releases for a given artist."""
    releases = ['Album1', 'Single1']  # Replace with dynamic data
    keyboard = [[InlineKeyboardButton(release, callback_data=f"{artist_name}/{release}")] for release in releases]
    return InlineKeyboardMarkup(keyboard)

def get_file_keyboard(artist_name, release_name):
    """Returns a keyboard with a list of files for a given release."""
    files = ['Track1.mp3', 'Track2.mp3']  # Replace with dynamic data
    keyboard = [[InlineKeyboardButton(file, callback_data=f"file_id_of_{file}")] for file in files]
    return InlineKeyboardMarkup(keyboard)
