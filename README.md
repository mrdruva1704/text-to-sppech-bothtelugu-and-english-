# text-to-sppech-bothtelugu-and-english-

This code uses the docx, gTTS, and pydub libraries to convert the text in a Word document into a combination of Telugu and English audio. Here's how the code works:

The docx library is used to read in the Word document specified in the code (QWQQ.docx). The text from each paragraph is then extracted and joined together into a single string.

Two instances of the gTTS class are created to convert the text to audio. One instance uses the language code te for Telugu, and the other uses en for English.

The resulting Telugu and English audio files are saved as telugu_audio.mp3 and english_audio.mp3, respectively.

The pydub library is then used to combine the Telugu and English audio files into a single audio file (final_audio.mp3). The combined audio file is exported in the mp3 format.

Note: The gTTS library uses Google's Text-to-Speech API, so an active internet connection is required to run this code. Additionally, the quality of the audio generated may depend on factors such as the quality of the internet connection, the language being spoken, and the speaker's pronunciation.





