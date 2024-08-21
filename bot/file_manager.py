import json

# Load the file ID mappings
with open('telegram-file-sharing-bot/data/file_ids.json', 'r') as f:
    file_ids = json.load(f)

def get_file_by_id(file_id):
    """Retrieves the file by its file_id."""
    return file_ids.get(file_id)
