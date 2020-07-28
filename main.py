from tkinter import *
import pyttsx3


engine = pyttsx3.init()
rate = engine.getProperty('rate')
set_rate = 120
engine.setProperty('rate', set_rate)

root = Tk()
root.geometry("400x500")
root.config(bg="#856ff8")
root.resizable(0, 0)
root.title("Text To Speech Converter")


def click():
    speakButton.config(state=DISABLED)
    sentence = text.get()
    engine.say(sentence)
    engine.runAndWait()
    engine.stop()
    text.delete(0, END)
    speakButton.config(state = ACTIVE)

def configVoice(num):
    voices = engine.getProperty('voices')

    if num == 0 :
        engine.setProperty('voice', voices[0].id)
        voiceLabel.config(text="Current Voice : " + "Male", bg="#eb34bd")

    if num == 1 :
        engine.setProperty('voice', voices[1].id)
        voiceLabel.config(text="Current Voice : " + "Female", bg="pink")

typeLabel = Label(root, text="Enter Your Text Here :",bg="#9eeb34", font=("15"))
text = Entry(root, width=30, font=("20"), borderwidth=3)
voiceLabel = Label(root, text="Current Voice : " + "Male", bg="#eb34bd", font=("20"))
chooseVoice = Label(root, text="Set your voice :", bg="yellow", font=("2"))
speakButton = Button(root, text = "Speak", bg="orange", fg="black", font=("5"), command = click)
maleVoice = Button(root, text="Male Voice", bg="#eb34bd", fg="black", command = lambda : configVoice(0))
femaleVoice = Button(root, text="Female Voice", bg="pink", fg="black", command = lambda : configVoice(1))
name = Label(root, text="Made by @Niloy Sikdar", bg="#856ff8", font=("Times", "15", "italic"))

typeLabel.pack(pady=25)
text.pack()
speakButton.pack(pady=15)
voiceLabel.pack(pady=15)
name.pack(side=BOTTOM)
chooseVoice.pack(side=LEFT, padx=20)
maleVoice.pack(side=RIGHT, padx=15, pady=5)
femaleVoice.pack(side=RIGHT, padx=5, pady=5)


root.mainloop()