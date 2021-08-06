import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import calendar
import wikipedia
import pyjokes
import os
import pywhatkit
import smtplib
import time
from te import text
import config3
import config2
from tkinter import*

e = pyttsx3.init("sapi5")
v = e.getProperty("voices")
e.setProperty("voices",v[0].id)

def On():
    def tellDay():
        day = datetime.date.today()
        speak(calendar.day_name[day.weekday()])
        current_time=datetime.datetime.now()

    def tellTime():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        output = "Your current local time is ",current_time
        speak(output)

    def speak(audio):
        e.say(audio)
        print(audio)
        e.runAndWait()

    def comm():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("listening")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1,phrase_time_limit=5)

        try:
            speak("recognizing")
            q = r.recognize_google(audio,language="en-in")
            print(f"user said: {q}")

        except Exception as ex:
            speak("Say that again please...")
            return "none"
        return q

    def wish():
        h = (datetime.datetime.now().hour)

        if h>=0 and h<=12:
            speak("Good Morning")
        elif h>12 and h<18:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        speak("I am jarvis sir your desktop assistant. Please tell how may i help you?")

    if __name__=="__main__":
        wish()
        while True:
            q=comm().lower()

            if "open minecraft app" in q:
                codePath = "C:\\Users\\DELL\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
                os.startfile(codePath)
                speak("opening minecraft")

            elif "open notepad" in q:
                path ="C:\\WINDOWS\\system32\\notepad.exe"
                speak("opening notepad")
                os.startfile(path)

            elif "open code" in q:
                codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                os.startfile(codePath)
                speak("opening Visual Studio Code")

            elif "what is the time" in q:
                tellTime()
                print("user:",q)

            elif "what is the day" in q:
                tellDay()
                print("user:",q)
                continue

            elif "goodbye" in q:
                speak("Good Bye sir!")
                print("user:",q)
                exit()

            elif "get lost" in q:
                speak("Sir, That was rude")
                print("user:",q)
                exit()

            elif "sleep" in q:
                g = int(input("Sleep for how many seconds? "))
                time.sleep(g)

            elif "shut up" in q:
                speak("Sir, that was too rude!")
                print("user:",q)
                exit()

            elif "open youtube" in q:
                print("user:",q)
                speak("Opening youtube ")
                webbrowser.open("www.youtube.com")

            elif "open google" in q:
                speak("Opening Google Chrome ")
                print("user:",q)
                webbrowser.open("www.google.com")

            elif "from wikipedia" in q:
                speak("Checking the wikipedia ")
                print("user:",q)
                qu = q.replace("wikipedia", "")
                result = wikipedia.summary(qu, sentences=4)
                speak("According to wikipedia")
                speak(result)
                print(result)

            elif " what is your name" in q:
                speak("I am Jarvis. Your Virtual Assistant!")
                print("user:",q)
                
            elif "joke" in q:
                speak(pyjokes.get_joke())
                print("user:",q)

            elif "whatsapp message to mum" in q:
                current_min=int(input("Please say the minute in which i have to send: "))   #datetime.datetime.now().minute
                current_hr=int(input("Please say the hour in 24 hrs format in which i have to send: "))#datetime.datetime.now().hour
                speak("what should i say")
                w=input("What shold i write: ")
                pywhatkit.sendwhatmsg("+91 89109 43314",w,current_hr,current_min+2)
                speak("Sending Whatsapp msg to mom")

            elif "play song on youtube" in q:
                speak("which song(please write)?")
                s = input("Which song(pls write): ")
                speak(f"playing {s}")
                pywhatkit.playonyt(s)

            elif "open microsoft teams" in q:
                codePath = "C:\\Users\\DELL\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
                os.startfile(codePath)
                speak("opening Microsoft Teams")

            elif "open command prompt" in q:
                codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python39\\Scripts"
                os.startfile(codePath)
                speak("opening Command Prompt")
                speak("You can access the command promt only after typing cmd in the codepath area.")

            elif "play your and my favourite song" in q:
                speak("playing See you again")
                pywhatkit.playonyt("See you again")

            elif "open instagram" in q:
                print("user:",q)
                speak("Opening instagram ")
                webbrowser.open("www.instagram.com")

            elif "open facebook" in q:
                print("user:",q)
                speak("Opening facebook ")
                webbrowser.open("www.facebook.com")
                
            elif "play video on youtube" in q:
                speak("which video(please write)?")
                s = input("Which video(pls write): ")
                speak(f"playing {s} on youtube")
                pywhatkit.playonyt(s)

            elif "open whatsapp" in q:
                print("user:",q)
                speak("Opening whatsapp ")
                webbrowser.open("https://web.whatsapp.com/")

            elif "open spotify" in q:
                path ="C:\\Users\\DELL\\AppData\\Roaming\\Spotify\\Spotify.exe"
                speak("opening Spotify")
                os.startfile(path)

            elif "open filmora" in q:
                path ="C:\\Program Files\\Wondershare\\Filmora9\\Filmora.exe"
                speak("opening Filmora")
                os.startfile(path)

            elif "open free cam 8" in q:                               
                path ="C:\\Program Files (x86)\\Free Cam 8\\freecam.exe"
                speak("opening FreeCam8")
                os.startfile(path)

            elif "open arduino" in q:
                path ="C:\\Program Files (x86)\\Arduino\\arduino.exe"
                speak("opening Aurduino Builder")
                os.startfile(path)

            elif "open anydesk" in q:
                path ="C:\Program Files (x86)\AnyDesk\AnyDesk.exe"
                speak("opening Anydesk")
                os.startfile(path)

            elif "open scratch desktop" in q:       
                path ="C:\\Program Files (x86)\\Scratch Desktop\\Scratch Desktop.exe"
                speak("opening scratch desktop")
                os.startfile(path)

            elif "my virus protector" in q:       
                path ="C:\\Program Files\\AVAST Software\\Avast\\AvastUI.exe"
                speak("opening Avast Free Antivirus")
                os.startfile(path)

            elif "switch off" in q:
                speak("Switching off sir")
                time.sleep(2)
                print("user:",q)
                exit()
            
            elif "open r studio" in q:       
                path ="C:\\Program Files\\RStudio\\R\\Api.R"
                speak("opening R Studios")
                os.startfile(path)

            elif "whatsapp message to mom" in q:
                current_min=int(input("Please say the minute in which i have to send: "))   #datetime.datetime.now().minute
                current_hr=int(input("Please say the hour in 24 hrs format in which i have to send: "))#datetime.datetime.now().hour
                speak("what should i say")
                w=input("What shold i write: ")
                pywhatkit.sendwhatmsg("+91 98362 33686",w,current_hr,current_min+2)
                speak("Sending Whatsapp msg to mom")

            elif "whatsapp message to sniggy" in q:
                current_min=int(input("Please say the minute in which i have to send: "))   #datetime.datetime.now().minute
                current_hr=int(input("Please say the hour in 24 hrs format in which i have to send: "))#datetime.datetime.now().hour
                speak("what should i say")
                w=input("What shold i write: ")
                pywhatkit.sendwhatmsg("+91 79805 17250",w,current_hr,current_min+2)
                speak("Sending Whatsapp msg to mom")

            elif "whatsapp message to father" in q:
                current_min=int(input("Please say the minute in which i have to send: "))   #datetime.datetime.now().minute
                current_hr=int(input("Please say the hour in 24 hrs format in which i have to send: "))#datetime.datetime.now().hour
                speak("what should i say")
                w=input("What shold i write: ")
                pywhatkit.sendwhatmsg("+917903060471 ",w,current_hr,current_min+2)
                speak("Sending Whatsapp msg to father")

            elif "open discord" in q:       
                path ="C:\\Users\\DELL\\AppData\\Local\\Discord\\app-1.0.9002\\Discord.exe"
                speak("opening discord")
                os.startfile(path)

            elif "open g-mail" in q:
                print(f"user: {q}")
                webbrowser.Chrome.open("www.gmail.com")
                speak("Opening G-mail")

            elif "open google" in q:
                print(f"user: {q}")
                webbrowser.Chrome.open("www.google.com")
                speak("Opening Google")

            elif "mail to mum" in q:
                subject = input("Write the subject: ")
                msg = input("Write the message: ")
                def send_email_to_s(subject, msg):
                    try:
                        server = smtplib.SMTP("smtp.gmail.com:587")
                        server.ehlo()
                        server.starttls()
                        server.login(config2.EMAIL_ADDRESS, config2.PASSWORD)
                        message = "Subject: {}\n\n{}".format(subject, msg)
                        server.sendmail(config3.Mom_email, config3.Mom_email, message)
                        server.quit()
                        print("Success: Email sent to mom!")
                                
                    except:
                        print("Email failed to send.")
                        
                send_email_to_s(subject, msg)

            elif "mail to vayu" in q:
                subject = input("Write the subject: ")
                msg = input("Write the message: ")
                def send_email_to_v(subject, msg):
                    try:
                        server = smtplib.SMTP("smtp.gmail.com:587")
                        server.ehlo()
                        server.starttls()
                        server.login(config2.EMAIL_ADDRESS, config2.PASSWORD)
                        message = "Subject: {}\n\n{}".format(subject, msg)
                        server.sendmail(config3.vayun_email, config3.vayun_email, message)
                        server.quit()
                        print("Success: Email sent to vayun!")
                        
                    except:
                        print("Email failed to send.")
                
                send_email_to_v(subject, msg)

            elif "through mail address" in q:
                m = input("Write the mail: ")
                subject = input("Write the subject: ")
                msg = input("Write the message: ")
                def send_email(subject, msg):
                    try:
                        server = smtplib.SMTP("smtp.gmail.com:587")
                        server.ehlo()
                        server.starttls()
                        server.login(config2.EMAIL_ADDRESS, config2.PASSWORD)
                        message = "Subject: {}\n\n{}".format(subject, msg)
                        server.sendmail(m, m, message)
                        server.quit()
                        print("Success: Email sent!")
                        
                    except:
                        print("Email failed to send.")

                send_email(subject, msg)

            elif "mail to sniggy" in q:
                subject = input("Write the subject: ")
                msg = input("Write the message: ")
                def send_email_to_sn(subject, msg):
                    try:
                        server = smtplib.SMTP("smtp.gmail.com:587")
                        server.ehlo()
                        server.starttls()
                        server.login(config2.EMAIL_ADDRESS, config2.PASSWORD)
                        message = "Subject: {}\n\n{}".format(subject, msg)
                        server.sendmail(config3.sniggy_email, config3.sniggy_email, message)
                        server.quit()
                        print("Success: Email sent to sniggy!")
                        
                    except:
                        print("Email failed to send.")
                
                send_email_to_sn(subject, msg)

            elif "mail to coding brother" in q:
                subject = input("Write the subject: ")
                msg = input("Write the message: ")
                def send_email_to_sn(subject, msg):
                    try:
                        server = smtplib.SMTP("smtp.gmail.com:587")
                        server.ehlo()
                        server.starttls()
                        server.login(config2.EMAIL_ADDRESS, config2.PASSWORD)
                        message = "Subject: {}\n\n{}".format(subject, msg)
                        server.sendmail(config3.Coding_Bhaia, config3.Coding_Bhaia, message)
                        server.quit()
                        print("Success: Email sent to Ariyaman!")
                        speak("Success: Email sent to Ariyaman!")
                        
                    except:
                        print("Email failed to send.")
                
                send_email_to_sn(subject, msg)

            elif "minecraft in browser" in q:
                print("user:",q)
                webbrowser.open("https://minecraft-js.vercel.app/")
                speak("Opening Minecraft in Browser")

            elif "mail to my father" in q:
                subject = input("Write the subject: ")
                msg = input("Write the message: ")
                def send_email_to_f(subject, msg):
                    try:
                        server = smtplib.SMTP("smtp.gmail.com:587")
                        server.ehlo()
                        server.starttls()
                        server.login(config2.EMAIL_ADDRESS, config2.PASSWORD)
                        message = "Subject: {}\n\n{}".format(subject, msg)
                        server.sendmail(config3.father_email, config3.father_email, message)
                        server.quit()
                        print("Success: Email sent to your father!")
                        
                    except:
                        print("Email failed to send.")
                
                send_email_to_f(subject, msg)

            elif "open file explorer" in q:
                codePath = "C:\\Users\\DELL"
                os.startfile(codePath)
                speak("opening File Explorer")

            elif "open file" in q:
                codePath = "C:\\Users\\DELL"
                os.startfile(codePath)
                speak("opening File Explorer")

            elif "open zoom" in q:
                codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk"
                os.startfile(codePath)
                speak("opening Zoom")

            elif "open my google" in q:
                codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
                os.startfile(codePath)
                speak("opening Vayun's Chrome")
                
while True:
    root = Tk()
    root.geometry("170x110")
    root.title("Jarvis")
    Switch_On = Button(root,text = "On",width = 10,command = On, background="green").place(x =50,y=70)
    root.mainloop()

#Under Construction