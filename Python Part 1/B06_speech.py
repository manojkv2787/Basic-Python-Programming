from asyncore import write
from dis import Instruction
import pyttsx3
engine = pyttsx3.init()
a = input("Say something:")
engine.say(a)
engine.runAndWait()