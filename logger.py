import languages

default_message_queue  = []

def log_message(message, message_queue = default_message_queue):
    # Translate debug messages
    if message.startswith("[DEBUG]"):
        debug_key = message.lower().replace("[debug] ", "debug_")
        translated_message = get_text(debug_key)
        if translated_message != debug_key:  # If translation exists
            message = f"[DEBUG] {translated_message}"
    
    message_queue.append(message)
    if len(message_queue) > 10:
        message_queue.pop(0)


def get_text(key):
    """Get translated text for current language"""
    return languages.translations.get(languages.current_language, languages.translations['English']).get(key, key)