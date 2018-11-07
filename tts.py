
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
from playsound import playsound
  
# The text that you want to convert to audio 
mytext = 'Daniel Heredia! You have violated the law! Pay the court a fine or serve your sentence!'
  
# Language in which you want to convert 
language = 'fr'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
playsound("welcome.mp3")