from flask import Flask, request, jsonify, send_file
from deep_translator import GoogleTranslator
from gtts import gTTS
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Map languages to gTTS language codes
LANGUAGE_CODES = {
    "en": "en",  # English
    "es": "es",  # Spanish
    "fr": "fr",  # French
    "de": "de",  # German
    "hi": "hi",  # Hindi
    "zh-cn": "zh-cn",  # Chinese (Simplified)
    "ja": "ja",  # Japanese
    "te": "te",  # Telugu
}

@app.route('/generate-voiceover', methods=['POST'])
def generate_voiceover():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        text = data.get('text')
        if not text:
            return jsonify({'error': 'No text provided'}), 400

        language = data.get('language', 'en')  # Default to English if no language is provided

        # Translate text to the desired language using deep-translator
        try:
            if language == "hi":  # Special handling for Hindi
                # Use GoogleTranslator for Hindi with additional checks
                translated_text = GoogleTranslator(source='auto', target='hi').translate(text)
                print(f"Translated Hindi text: {translated_text}")  # Log the translated text
            elif language == "te":  # Special handling for Telugu
                # Use GoogleTranslator for Telugu with additional checks
                translated_text = GoogleTranslator(source='auto', target='te').translate(text)
                print(f"Translated Telugu text: {translated_text}")  # Log the translated text
            else:
                translated_text = GoogleTranslator(source='auto', target=language).translate(text)
        except Exception as e:
            print(f"Translation error: {e}")
            return jsonify({'error': 'Failed to translate text'}), 400

        print(f"Generating voiceover for text: {translated_text} in language: {language}")  # Log the text and language

        # Get the gTTS language code for the selected language
        lang_code = LANGUAGE_CODES.get(language, "en")  # Default to English if language not found

        # Generate speech using gTTS
        tts = gTTS(text=translated_text, lang=lang_code, slow=False)
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)

        print("Voiceover generated successfully")  # Log success
        return send_file(audio_file, mimetype='audio/mpeg')

    except Exception as e:
        print(f"Error generating voiceover: {e}")  # Log the error
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)