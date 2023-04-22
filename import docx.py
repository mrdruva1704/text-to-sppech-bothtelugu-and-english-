import docx
from gtts import gTTS
from pydub import AudioSegment

# Read in the Word document
doc = docx.Document('QWQQ.docx')
text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
telugu_tts = gTTS(text, lang='te') # 'te' is the language code for Telugu
english_tts = gTTS(text, lang='en') # 'en' is the language code for English
telugu_tts.save('telugu_audio.mp3')
english_tts.save('english_audio.mp3'
telugu_audio = AudioSegment.from_file('telugu_audio.mp3')
english_audio = AudioSegment.from_file('english_audio.mp3')
combined_audio = telugu_audio + english_audio
combined_audio.export('final_audio.mp3', format='mp3')
