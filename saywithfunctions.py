import gtts
from playsound import playsound

def say_hello(name):
    spoken_name = gtts.gTTS(f"Hello {name}, Nice to meet you")
    spoken_name.save("hello.mp3")
    playsound("hello.mp3")

def main():
    your_name = input("What is your name")
    say_hello(your_name)

main()