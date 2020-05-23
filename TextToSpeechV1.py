import os
from gtts import gTTS
import docx2txt

# pip install gTTS
# pip install docx2txt

# to play, put this file in the current dir.

#word to text convertor replace docfilename

filename="COVID19anditsimpactonsports"
MY_TEXT = docx2txt.process(filename+".docx")

with open(filename+".txt", "w") as text_file:
    print(MY_TEXT, file=text_file)


# You will need a text file named test.txt

FLIST = open(filename+".txt", "r").read().replace("\n", " ")

print("please wait...processing")
TTS = gTTS(text=str(FLIST), lang='en-us')

# Save to mp3 in current dir.
TTS.save(filename+".mp3")

# Plays the mp3 using the default app on your system
# that is linked to mp3s.
print("Process Done Now File has store in your current dir.")
os.system(filename+".mp3")
