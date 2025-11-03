import pyttsx3


engine = pyttsx3.init()

while True:
    speak = input("Enter to speak:")

    if speak != "q":
        engine.say(speak)

        engine.runAndWait()

    else:
        
        speak = "thank you for using robo speaker"
        print("thank you for using robo speaker")
        engine.say(speak)
        engine.runAndWait()
        break  
    
   