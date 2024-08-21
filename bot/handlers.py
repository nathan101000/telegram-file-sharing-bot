from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    """Handles the /start command."""
    from .keyboards import get_artist_keyboard
    keyboard = get_artist_keyboard()
    update.message.reply_text('Please choose an artist:', reply_markup=keyboard)

def button(update: Update, context: CallbackContext):
    """Handles button presses in the inline keyboard."""
    query = update.callback_query
    data = query.data.split('/')
    
    if len(data) == 1:
        from .keyboards import get_release_keyboard
        artist_name = data[0]
        keyboard = get_release_keyboard(artist_name)
        query.edit_message_text(text=f"Selected artist: {artist_name}\nChoose a release:", reply_markup=keyboard)
    
    elif len(data) == 2:
        from .keyboards import get_file_keyboard
        artist_name, release_name = data
        keyboard = get_file_keyboard(artist_name, release_name)
        query.edit_message_text(text=f"Selected release: {release_name}\nChoose a track:", reply_markup=keyboard)
    
    else:
        from .file_manager import get_file_by_id
        file_id = data[2]
        query.message.reply_document(get_file_by_id(file_id))
