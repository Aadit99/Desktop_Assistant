import pyttsx3          #pip install pyttsx3
import webbrowser
import datetime
import wikipedia        #pip install wikipedia
import speech_recognition as speechrec  #pip install speech recognition

# might need to seperately install pyaudio as pip install pyaudio in case of an error


alexaengine = pyttsx3.init('sapi5')     #make a new instance of pyttsx3 with sapi5 (for windows OS)
allvoices = alexaengine.getProperty('voices')   #get all default voices in the system
alexaengine.setProperty('voice', allvoices[0].id)  #choose a voice..in this device 0 for male and 1 for female

def speak(audio):                            
    alexaengine.say(audio)              #use speaker to input the arguement
    alexaengine.runAndWait()            #actually say the arguement

def takeCommand():
    recognizer = speechrec.Recognizer()   #instance of the Recognizer class in speech recognition package
    with speechrec.Microphone() as source:       #use microphone to take input
        print("Listening...")
        audio = recognizer.listen(source)       #listen the input

    try:
        print("Recognizing...")    
        userQuery = recognizer.recognize_google(audio, language='en-in')  #use google recognizer to understad the query
        print(userQuery)

    except Exception as e: 
        speak("could not listen...")  
        return "None"
    return userQuery          # return the audio as a string

if __name__ == "__main__":
    # while True:
    if 1:
        userQuery = takeCommand().lower()
        if 'wikipedia' in userQuery:
            userQuery = userQuery.replace("wikipedia", "")
            fetched = wikipedia.summary(userQuery, sentences=2)
            speak("Wikipedia says")
            print(fetched)
            speak(fetched)
            
        elif 'open youtube' in userQuery:
            webbrowser.open("youtube.com")
            
        elif 'open google' in userQuery:
            webbrowser.open("google.com")
            
        elif 'open twitter' in userQuery:
            webbrowser.open("twitter.com") 
              
        elif 'open facebook' in userQuery:
            webbrowser.open("facebook.com")   
            
        elif 'the time' in userQuery:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")     
            
        elif 'quit' in userQuery:
            speak("Quitting now")
            exit()
            
            
# CODE CONTRIBUTED BY AADIT NANDAN